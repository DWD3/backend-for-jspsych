from chalice import Chalice,Rate
import boto3
import os

app = Chalice(app_name='backend-jspsych')

@app.route('/uploadresult',methods=['POST'])
def upload_result():
    domain_name = os.environ.get('SimpleDBDomainName', 'ExpResultSDB')
    bucket_name = os.environ.get('S3BucketName','')
    return {"S3BucketName":domain_name,"bucket_name":bucket_name}
