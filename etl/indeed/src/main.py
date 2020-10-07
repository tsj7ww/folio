# standard
import json
import os
import io
import sys
import datetime
import logging

# etc
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
    """"""
    if env=='dev':
        None
    elif env=='qa':
        None
    elif env=='prod':
        None
    else:
        raise Exception('Unknown environment.')

    cwd = os.getcwd()
    now = datetime.datetime.now()
    dt = '%Y%m%d'
    dttm = '%Y%m%d_%H%M%S'

    eid = 'tsj7ww'
    proc = 'Indeed'
    pid = 'etl-indeed'

    region = 'us-east-1'
    rgn = region.replace('-','')

    cfg = {
        'now': now,
        'cwd': cwd,
        'pid': pid,
        'proc': proc,
        'region': region,
        'eid': eid,
        'arn': '{arn}:{partition}:{service}:{region}:{account-id}:{resource-id}',
        'indeed': {
            'url': 'https://www.indeed.com/jobs?start={NUM}&q={QRY}&l={LOC}',
            'replace': {' ':'%20',',':'%2C'}
        },
        'db': {
            'url': 'https://dynamodb.{}.amazonaws.com'.format(region),
            'table': pid
        },
        'email': {
            'Source': os.environ['SENDER'],
            'Destination': {'ToAddresses': os.environ['STAKEHOLDERS'].split(',')},
            'Message': {
                'Subject': {'Data': 'Indeed Weekly Summary','Charset': 'UTF-8'},
                'Body': {'Html': {'Data': None,'Charset': 'UTF-8'}}
            }
        },
        'alert': {
            'TopicArn': os.environ['SNS'],
            'Message': None,
            'Subject': 'Process {}: ' + proc
        }
    }

    return cfg

def LOGGER(env):
    """"""
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    logger = logging.getLogger(__name__)

    if env=='dev':
        level = logging.DEBUG
        feed = sys.stdout
    elif env=='qa':
        level = logging.INFO
        feed = io.StringIO()
    elif env=='prod':
        level = logging.WARNING
        feed = io.StringIO()
    else:
        raise Exception('Unknown environment.')

    handler = logging.StreamHandler(feed)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger,feed

def URL(url,titles,locations,replace,pages=1):
    """"""
    logger = logging.getLogger(__name__)

    for t in titles:
        for l in locations:
            _ = {'title': t,'location': l}
            for i,j in replace.items():
                t = t.replace(i,j)
                l = l.replace(i,j)
            for p in range(pages):
                _['url'] = url.format(NUM=10*p,QRY=t,LOC=l)
                logger.info('Generating URL: {}'.format(_['url']))
                yield _

def CLEAN(item):
    """"""
    logger = logging.getLogger(__name__)

    rm = re.compile('[^A-Za-z0-9\&\.\s]+')
    spc = re.compile('\s{2,}')
    base = re.compile(r'\s([."])(?:\s|$)')

    return base.sub(r'\1',spc.sub(' ',rm.sub('',item))).strip().upper()

def EXTRACT(soup):
    """"""
    logger = logging.getLogger(__name__)

    url = 'www.indeed.com'
    skip = ['indeed_id','urlpost']
    data = []

    for row in soup.find_all(name='div',attrs={'class':'row'}):
        post = {'indeed_id':str(uuid.uuid4())}

        try:
            post['title'] = row.find(name='a',attrs={'data-tn-element':'jobTitle'}).text
        except:
            post['title'] = None
        try:
            post['company'] = row.find(name='a',attrs={'data-tn-element':'companyName'}).text
        except:
            post['company'] = None
        try:
            post['rating'] = row.find(name='span',attrs={'class':'ratingsContent'}).text
        except:
            post['rating'] = None
        try:
            post['city'] = row.find('div', attrs={'class': 'recJobLoc'})['data-rc-loc'].split(',')[0]
        except:
            post['city'] = None
        try:
            post['state'] = row.find('div', attrs={'class': 'recJobLoc'})['data-rc-loc'].split(',')[1]
        except:
            post['state'] = None
        try:
            post['salary'] = row.find('nobr').text
        except:
            post['salary'] = None
        try:
            post['summary'] = ' '.join([i.text for i in row.find('div',attrs={'class','summary'}).find_all('li')])
        except:
            post['summary'] = None
    #     try:
    #         post['duties'] = None
    #     except:
    #         post['duties'] = None
    #     try:
    #         post['skills'] = None
    #     except:
    #         post['skills'] = None
        try:
            post['url_post'] = url+row.find(name='a',attrs={'data-tn-element':'jobTitle'})['href']
        except:
            post['url_post'] = None
    #     try:
    #         post['url_app'] = None
    #     except:
    #         post['url_app'] = None

        for k,v in post.items():
            if (k not in skip) & (v!=None):
                post[k] = CLEAN(v)

        data.append(post)

    return data

def LOAD(data,url,table):
    """
    """
    logger = logging.getLogger(__name__)

    fails = []
    db = boto3.resource('dynamodb', endpoint_url=url)
    tbl = db.Table(table)
    with tbl.batch_writer() as b:
        for d in data:
            r = b.put_item(Item=d)
            if r:
                fails.append(r)
    return fails

def BODY(data):
    """"""
    logger = logging.getLogger(__name__)

    body = 'Here are today\'s job postings:<br><br>'
    template = '<li>{TITLE} at {COMPANY} in {CITY}, {STATE} - <a href=\'{URL}\'>Link</a></li>'
    groups = set((i['q_title'],i['q_location']) for i in data)
    for g in groups:
        rows = '<b>{TTL} in {LOC}</b>:<br><ul>'.format(TTL=g[0],LOC=g[1])
        for d in data:
            if g==(d['q_title'],d['q_location']):
                rows+=template.format(
                    URL=d['url_post'],
                    TITLE=d['title'],COMPANY=d['company'],
                    CITY=d['city'],STATE=d['state']
                )
        body+=(row+'</ul>')

    return body

def ALERT(publish,success,err=None):
    """"""
    if success:
        publish['Subject'] = publish['Subject'].format('Success')
        publish['Message'] = 'Process success.'
    else:
        publish['Subject'] = publish['Subject'].format('Failure')
        publish['Message'] = err

    return boto3.client('sns').publish(**publish)

def EMAIL(body,package):
    """"""
    package['Message']['Body']['Html']['Data'] = body
    return boto3.client('ses').send_email(**package)

# if __name__=="__main__":
def HANDLER(event, context):
    """"""
    # if not event: # developing locally
    #     with open(os.path.join(os.getcwd(),'metadata.json'),'r') as f:
    #         META = json.load(f)

    start = datetime.datetime.now()
    env = 'dev'
    with open(os.path.join(os.getcwd(),'env/{}'.format(env)),'r') as f:
        os.environ.update(**json.load(f))

    LOG,FEED = LOGGER(env)
    CFG = CONFIG(env)

    # temporarily use static values -> transition to using event
    if env=='dev':
        fails = None
        params = {
            'titles': ['data scientist'],
            'locations': ['seattle, wa']
        }
    elif env=='prod':
        params = {
            'titles': ['data scientist','business analyst','data analyst','data engineer'],
            'locations': ['seattle, wa','austin, tx','washington, dc','richmind, va','boston, ma']
        }
    else:
        raise Exception('Unknown environment')


    try:
        URLS = None
        POSTS = []

        LOG.info('Setup complete - generate urls.')
        # use generator to minimize downtime between requests
        urls = URL(**params,**CFG['indeed'])

        for q in urls:

            begin = datetime.datetime.now()
            data = None
            _ = {'q_title':q['title'].upper(),'q_location':q['location'].upper()}

            LOG.info('Make get request')
            q['soup'] = bs4.BeautifulSoup(requests.get(q['url']).text,'html.parser')

            LOG.info('Transform soup HTML to data')
            data = [{**_,**i} for i in EXTRACT(q['soup'])]
            POSTS.append(data)

            # LOG.info('Loading {} rows into DynamoDB'.format(len(data)))
            # fails = LOAD(data,**CFG['db'])

            # sleep random intervals to not get caught scraping
            browse = random.randint(2,6)
            t = max((browse - (datetime.datetime.now() - begin).seconds),0)
            LOG.info('Sleeping for {} seconds'.format(t))
            time.sleep(t)

        # LOG.info('Sending email')
        # EMAIL(BODY(POSTS),CFG['email'])
        #
        # LOG.info('Publishing event')
        # ALERT(CFG['alert'],success=True)

        runtime = (datetime.datetime.now()-start).seconds
        LOG.info('Job complete after {} seconds!'.format(runtime))

        return {
            'status': 'success',
            'summary': '{} posts pulled in {} seconds.'.format(len(POSTS),runtime),
            'data': POSTS,
            'fails': fails
        }

    except Exception as e:
        err = str(e)
        LOG.critical('Fatal error: {}'.format(err))
        # ALERT(CFG['alert'],success=False,err=err)
        return {
            'status': 'failure',
            'error': err
        }

# print(HANDLER(None,None)) # testing
# PROD changes: uncomment AWS service code, return JSON response
