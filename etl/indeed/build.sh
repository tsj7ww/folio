DYNAMO() {
    aws dynamodb create-table --table-name etl-indeed \
    --attribute-definitions AttributeName=jobOppId,AttributeType=S \
    --key-schema AttributeName=jobOppId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
    # --sse-specification Enabled=true SSEType=AES256
    # aws dynamodb delete-table --table-name indeed

    # attach policy???
}

SNS() {
  # create topic
  aws sns create-topic --name etl-indeed
  # subscribe stakeholders (a.k.a. me)
  aws sns subscribe --topic-arn "$SNS:etl-indeed" --protocol email --notification-endpoint $SENDER

  # allow invoke from lambda -> only need for cross account
  # aws sns add-permission --topic-arn $SNS
}

IAM() {
  ### lambda
  # role + trust policy
  aws iam create-role \
  --role-name lambda-etl-indeed \
  --assume-role-policy-document file://$PWD/artifacts/iam-lambda-trust.json \
  --description "IAM role for Indeed ETL Lambda function."

  # policy - exec, dynamodb crud, sns publish, ses send
  aws iam put-role-policy \
  --role-name lambda-etl-indeed \
  --policy-name lambda-etl-indeed \
  --policy-document file://$PWD/artifacts/iam-lambda-policy.json

  ### events
  # role + trust
  aws iam create-role \
  --role-name events-etl-indeed \
  --assume-role-policy-document file://$PWD/artifacts/iam-events-trust.json \
  --description "IAM role for ETL Indeed cron event."

  # policy - event target role
  aws iam attach-role-policy \
  --role-name events-etl-indeed \
  --policy-arn "arn:aws:iam::aws:policy/service-role/AWSBatchServiceEventTargetRole"
}

LAMBDA() {
  # publish layer
  # aws lambda publish-layer-version \
  # --layer-name python-webscrape \
  # --compatible-runtimes "python3.8" \
  # --description "Python web scraping packages. Includes: bs4, requests." \
  # --content S3Bucket=tsj7ww-artifacts-useast1,S3Key=layers/python/webscrape.zip
  # update lambda
  aws lambda create-function \
  --function-name etl-indeed \
  --runtime "python3.8" \
  --role "$IAM/lambda-etl-indeed" \
  --handler main.HANDLER \
  --code S3Bucket=tsj7ww-artifacts-useast1,S3Key=etl/indeed/src.zip \
  --description "Function for intaking queries and responding with postings from Indeed.com" \
  --publish --timeout 120 \
  --layers "$LAYER:python-webscrape:1"
  #--environment $PWD/src/env/prod

  # allow invoke from events
  aws lambda add-permission \
  --function-name etl-indeed \
  --statement-id sns \
  --action lambda:InvokeFunction \
  --principal sns.amazonaws.com \
  --source-arn "$EVENTS/etl-indeed"

}

EVENTS() {
  # setup event
  aws events put-rule \
  --name etl-indeed \
  --schedule-expression "cron(59 8 ? * SUN *)" \
  --state ENABLED --description "ETL Indeed.com cron" \
  --role-arn "$IAM/events-etl-indeed"
  # set target
  aws events put-targets --rule etl-indeed --targets "Id"="1","Arn"="$FUNCTION:etl-indeed"
  # --role-arn $IAM/event-etl-indeed
}

COMPILE() { # TODO: build src env files from build env??
  SRC=$PWD/src
  ART=$PWD/artifacts
  # zip source py code
  (cd $SRC && zip -r $ART/src.zip ./*)
  # s3 put
  aws s3api put-object --region us-east-1 --bucket tsj7ww-artifacts-useast1 --key etl/indeed/src.zip --body $ART/src.zip --acl bucket-owner-full-control --storage-class REDUCED_REDUNDANCY
  # install reqs
  PKG=$ART/layers/webscrape
  pip install -r $LAYER/requirements.txt -t $PKG/python/lib/python3.8/site-packages
  # zip layer
  (cd $PKG && zip -r $ART/webscrape.zip ./*)
  # s3 put
  aws s3api put-object --region us-east-1 --bucket tsj7ww-artifacts-useast1 --key layers/python/webscrape.zip --body $ART/webscrape.zip --acl bucket-owner-full-control --storage-class REDUCED_REDUNDANCY
}

BUILD() {
  source $PWD/artifacts/build.env
  # dev
  if $1;
    then
      DYNAMO;
      SNS; # SES -> no setup
  fi;
  # prod
  if $2;
    then
      COMPILE;
      IAM;
      LAMBDA;
      EVENTS;
  fi;
}

BUILD true true
