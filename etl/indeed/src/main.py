# standard
import json
import os
import io
import datetime
import logging
import time
import random
import re
import uuid

# aws
import boto3

# web scrape - imported in layer
import requests
import bs4

def CONFIG(env):
    """
    Create ref dict
    """
    if env=='dev':
        None
    elif env=='qa':
        None
    elif env=='prod':
        None
    else:
        raise Exception('Unknown environment.')

    _name = 'Indeed'
    _id = 'etl-indeed'
    _dt = '%Y%m%d'
    _dttm = '%Y%m%d_%H%M%S'
    _now = datetime.datetime.now()
    _region = 'us-east-1'
    _rgn = _region.replace('-','')

    _cfg = {
        'now': _now,
        'arn': '{arn}:{partition}:{service}:{region}:{account-id}:{resource-id}',
        'indeed': {
            'url': 'https://www.indeed.com/jobs?start={NUM}&q={QRY}&l={LOC}',
            'replace': {' ':'%20',',':'%2C'}
        },
        'db': {
            'url': 'https://dynamodb.{}.amazonaws.com'.format(_region),
            'table': _id,
        },
        'email': {
            'Source': os.environ['SENDER'],
            'Destination': {'ToAddresses': os.environ['STAKEHOLDERS'].split(',')},
            'Message': {
                'Subject': {'Data': 'Indeed Weekly Summary','Charset': 'UTF-8'},
                'Body': {'Html': {'Data': None,'Charset': 'UTF-8'}},
            }
        },
        'alert': {
            'TopicArn': os.environ['SNS'],
            'Message': None,
            'Subject': 'Process {}: ' + _name,
        }
    }

    return _cfg

def LOGGER(env):
    """"""
    if env=='dev':
        _lvl = logging.DEBUG
    elif env=='qa':
        _lvl = logging.WARNING
    elif env=='prod':
        _lvl = logging.ERROR
    else:
        raise Exception('Unknown environment.')

    _str = io.StringIO()
    _handler = logging.StreamHandler(_str)
    _log = logging.getLogger()

    _log.setLevel(_lvl)
    _handler.setFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    _log.addHandler(_handler)

    return _log,_str

def URL(url,titles,locations,replace,pages=1):
    """"""
    _urls = []
    for t in titles:
        for l in locations:
            _t = t
            _l = l
            for i,j in replace.items():
                _t = _t.replace(i,j)
                _l = l.replace(i,j)
            for p in range(pages):
                _urls.append({
                    'title': t,'location': l
                    ,'url': url.format(NUM=10*p,QRY=_t,LOC=_l)
                })
    return _urls

def EXTRACT(url):
    """"""
    time.sleep(random.randint(2,6))
    return bs4.BeautifulSoup(requests.get(url).text,'html.parser')

def CLEAN(item):
    """quick function for cleaning scraped text data"""
    _rm = re.compile('[^A-Za-z0-9\&\.\s]+')
    _spc = re.compile('\s{2,}')

    return re.sub(r'\s([."](?:\s|$))', r'\1',_spc.sub(' ',_rm.sub('',item))).strip().upper()

def TRANSFORM(soup):
    """
    in: soup obj
    out: cleaned text
    """
    _url = 'www.indeed.com'
    _skip = ['jobOppId','url_post']
    _data = []

    for row in soup.find_all(name='div',attrs={'class':'row'}):
        _post = {'jobOppId':str(uuid.uuid4())}
        try:
            _post['title'] = row.find(name='a',attrs={'data-tn-element':'jobTitle'}).text
        except:
            _post['title'] = None
        try:
            _post['company'] = row.find(name='a',attrs={'data-tn-element':'companyName'}).text
        except:
            _post['company'] = None
        try:
            _post['rating'] = row.find(name='span',attrs={'class':'ratingsContent'}).text
        except:
            _post['rating'] = None
        try:
            _post['city'] = row.find('div', attrs={'class': 'recJobLoc'})['data-rc-loc'].split(',')[0]
        except:
            _post['city'] = None
        try:
            _post['state'] = row.find('div', attrs={'class': 'recJobLoc'})['data-rc-loc'].split(',')[1]
        except:
            _post['state'] = None
        try:
            _post['salary'] = row.find('nobr').text
        except:
            _post['salary'] = None
        try:
            _post['summary'] = ' '.join([i.text for i in row.find('div',attrs={'class','summary'}).find_all('li')])
        except:
            _post['summary'] = None
    #     try:
    #         _post['duties'] = None
    #     except:
    #         _post['duties'] = None
    #     try:
    #         _post['skills'] = None
    #     except:
    #         _post['skills'] = None
        try:
            _post['url_post'] = _url+row.find(name='a',attrs={'data-tn-element':'jobTitle'})['href']
        except:
            _post['url_post'] = None
    #     try:
    #         _post['url_app'] = None
    #     except:
    #         _post['url_app'] = None

        for k,v in _post.items():
            if (k not in _skip) & (v!=None):
                _post[k] = CLEAN(v)

        _data.append(_post)

    return _data

def LOAD(data,url,table):
    """
    """
    _responses = []
    _db = boto3.resource('dynamodb', endpoint_url=url)
    _tbl = _db.Table(table)
    with _tbl.batch_writer() as b:
        for r in data:
            _r = b.put_item(Item=r)
            if _r:
                _responses.append(_r)
    return _responses

def BODY(data):
    """"""
    _body = 'Here are today\'s job postings:<br><br>'
    _template = '<li><a href=\'{URL}\'>{TITLE} at {COMPANY} in {CITY}, {STATE}</li>'
    _groups = []
    [_groups.append((i['q_title'],i['q_location'])) for i in data if (i['q_title'],i['q_location']) not in _groups]
    for i in _groups:
        _row = '<b>{TTL} in {LOC}</b><br><ul>'.format(TTL=i[0],LOC=i[1])
        for j in data:
            if i==(j['q_title'],j['q_location']):
                _row+=_template.format(
                    URL=j['url_post'],
                    TITLE=j['title'],COMPANY=j['company'],
                    CITY=j['city'],STATE=j['state']
                )
        _body+=(_row+'</ul>')
    return _body

def ALERT(publish,success,err=None):
    """"""
    if success:
        publish['Subject'] = publish['Subject'].format('Success')
        publish['Message'] = 'Process success.'
    else:
        publish['Subject'] = publish['Subject'].format('Failure')
        publish['Message'] = err
    sns = boto3.client('sns')
    return sns.publish(**publish)

def EMAIL(body,package):
    """"""
    package['Message']['Body']['Html']['Data'] = body
    ses = boto3.client('ses')
    return ses.send_email(**package)

# if __name__=="__main__":
def HANDLER(event, context):

    # if not event: # developing locally
    #     with open(os.path.join(os.getcwd(),'metadata.json'),'r') as f:
    #         META = json.load(f)

    START = datetime.datetime.now()
    ENV = 'dev'
    with open(os.path.join(os.getcwd(),'env/{}'.format(ENV)),'r') as f:
        os.environ.update(**json.load(f))
    LOG,FEED = LOGGER(ENV)
    CFG = CONFIG(ENV)
    RESPONSE = {}

    # temporarily use static values -> transition to using event
    if ENV=='dev':
        PARAMS = {
            'titles': ['data scientist'],
            'locations': ['seattle, wa']
        }
    elif ENV=='prod':
        PARAMS = {
            'titles': ['data scientist','business analyst','data analyst','data engineer'],
            'locations': ['seattle, wa','austin, tx','washington, dc','richmind, va','boston, ma']
        }


    try:
        URLS = []
        POSTS = []

        LOG.info('setup complete - generate urls')
        URLS = URL(**PARAMS,**CFG['indeed'])

        for q in URLS:

            LOG.info('get requests')
            q['soup'] = EXTRACT(q['url'])

            LOG.info('transform data')
            for i in TRANSFORM(q['soup']):
                POSTS.append({**{'q_title':q['title'].upper(),'q_location':q['location'].upper()},**i})

        LOG.info('load data to dynamo db')
        response = LOAD(POSTS,**CFG['db'])

        LOG.info('sending notifications')
        EMAIL(BODY(POSTS),CFG['email'])
        ALERT(CFG['alert'],success=True)
        LOG.info('job complete')
        return {
            'status': 'success',
            'data': [{'info': '{} queries containing {} posts completed in {} seconds.'.format(len(URLS),len(POSTS),(datetime.datetime.now()-START).seconds)}]
        }

    except Exception as e:
        _err = str(e)
        LOG.critical(_err)
        ALERT(CFG['alert'],success=False,err=_err)
        return {
            'status': 'failure',
            'error': _err
        }

# print(HANDLER(None,None)) # testing
