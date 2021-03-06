# To deploy lambda on AWS
rm slackclara.zip
zip slackclara.zip -r lambda_slackclara.py nocheckin.py elasticsearch/ elasticsearch5/ certifi/ chardet/ requests/ idna/ requests_aws4auth/ urllib3/ awsconfig.py simple_sentiment.py subjclueslen1-HLTEMNLP05.tff

aws --profile ailine s3 cp slackclara.zip s3://sandyai2/

#aws --profile ailine lambda create-function --function-name slackclara --runtime python3.6 --role "arn:aws:iam::740157263594:role/sandyairun" --handler lambda_slackclara.lambda_handler --timeout 59 --code "S3Bucket=sandyai2,S3Key=slackclara.zip"

aws --profile ailine lambda update-function-code --function-name slackclara --s3-bucket sandyai2 --s3-key slackclara.zip


