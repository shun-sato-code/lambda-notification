from __future__ import print_function
from datetime import datetime
import requests
import json
print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['requestPayload']['Records'][0]['Sns']['Message']
    # print("From SNS: " + message)
    # return message
    from datetime import datetime
    import requests
    
    webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAZ5zOGd4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=i8Lwoaa_QgEHOBoHVkFyab-zCftPX7VuDvJfYB9SsLQ%3D'
    
    response = requests.post(
      webhook_url,
      json={"text": "lambndaから送信テスト\n"+str(message)}
    )