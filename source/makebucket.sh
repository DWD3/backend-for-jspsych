#!/bin/bash

# set the AWS IAM user for deployment

# input="./credential.txt"
# read -r profile_name < $input

profile_name = $1
bucket_name = $2

# make a s3 bucket to hold the code
export AWS_PROFILE=$profile_name
aws s3 mb s3://$bucket_name
