from chalice import Chalice
import boto3

app = Chalice(app_name='backend')


@app.route('/uploadresult',methods=['POST'])
def index():
    return {'hello': 'world'}
