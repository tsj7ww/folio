SRC() {
  # zip source py code
  (cd $1 && zip -r $2/src.zip ./*)
  # s3 put
  aws s3api put-object --region us-east-1 \
  --bucket tsj7ww-artifacts-useast1 --key etl/indeed/src.zip \
  --body $2/src.zip --acl bucket-owner-full-control \
  --storage-class REDUCED_REDUNDANCY
}

LAMBDA() {
  aws lambda update-function-code \
  --function-name etl-indeed \
  --s3-bucket tsj7ww-artifacts-useast1 \
  --s3-key etl/indeed/src.zip \
  --publish
}

LAYER() {
  PKG=$1/layers/webscrape
  # install reqs
  pip install -r $PKG/requirements.txt -t $PKG/python/lib/python3.8/site-packages
  # zip layer
  (cd $PKG && zip -r $1/webscrape.zip ./*)
  # s3 put
  aws s3api put-object --region us-east-1 \
  --bucket tsj7ww-artifacts-useast1 --key layers/python/webscrape.zip \
  --body $1/webscrape.zip --acl bucket-owner-full-control \
  --storage-class REDUCED_REDUNDANCY
  # publish layer
  aws lambda publish-layer-version \
  --layer-name python-webscrape \
  --compatible-runtimes "python3.8" \
  --description "Python web scraping packages. Includes: bs4, requests." \
  --content S3Bucket=tsj7ww-artifacts-useast1,S3Key=layers/python/webscrape.zip
  # update lambda
  aws lambda update-function-configuration \
  --function-name etl-indeed \
  --layers "$LAYER:python-webscrape:2"

}

UPDATE() {
  source $PWD/artifacts/build.env
  SRC=$PWD/src
  ART=$PWD/artifacts

  SRC $SRC $ART
  LAMBDA

  # LAYER $ART
}

UPDATE
