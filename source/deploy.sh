profile_name = $1
bucket_name = $2
stack_name = $3

export AWS_PROFILE=$profile_name

chalice package --merge-template resources.json out

aws cloudformation package  --template-file out/sam.json --s3-bucket $bucket_name --output-template-file out/template.yml
aws cloudformation deploy --template-file out/template.yml --stack-name $stack_name --capabilities CAPABILITY_IAM