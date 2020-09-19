from chalice import Chalice
import boto3
import os

app = Chalice(app_name='backend')


@app.route('/uploadresult',methods=['POST'])
def upload_result():
    domain_name = os.environ.get('SimpleDBDomainName', 'ExpResultSDB')
    return {"result":domain_name}
