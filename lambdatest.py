from __future__ import print_function
from datetime import datetime
import requests
import json
import re
from datetime import datetime
import pytz
print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['requestPayload']['Records'][0]['Sns']['Message']
    
    print("From SNS: " + message)
    # return message

    try:
        found = re.search('{0=(.+?)}', message).group(1)
        print(found)
    except AttributeError:
        pass
    
    time = iso_to_jstdt(found)
    
    
    time2 = time.strftime('%Y-%m-%d %H:%M')
    print(time2)

    
    #test1
    webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAWNswxSo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=nYhJX8NOBLRV7BTVgUNcOjTjzZowhnbUFtnM3GBMZc0%3D'
    #test2
    #webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAZt8akWI/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=mc5-AM1v3GgiYTZWTA9EvvmUrjfU68UyFdBZBOYIL8g%3D'

    response = requests.post(
      webhook_url,
      json={"text": str(time2)}
    )
    


def iso_to_jstdt(iso_str):
    dt = None
    try:
        dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        dt = pytz.utc.localize(dt).astimezone(pytz.timezone("Asia/Tokyo"))
    except ValueError:
        try:
            dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            dt = dt.astimezone(pytz.timezone("Asia/Tokyo"))
        except ValueError:
            pass
    return dt