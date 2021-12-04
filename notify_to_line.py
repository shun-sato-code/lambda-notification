from __future__ import print_function
from datetime import datetime
import requests
import json
print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    # print("From SNS: " + message)
    # return message
    line_notify_token = 'QTi1vgfOLEKOyfd9vmmilHk6fCiZSmPHDB2dEp5GtZT'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {message}'}
    requests.post(line_notify_api, headers = headers, data = data)