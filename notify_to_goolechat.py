from __future__ import print_function
from datetime import datetime
import requests
import json
import re
import pytz


def lambda_handler():
    print("hoge")
    json_open = open('insidentResponse.json', 'r')
    event = json.load(json_open)
    #Subject = event['requestPayload']['Records'][0]['Sns']['Subject']
    Subject = 'hoge'
    message = event['requestPayload']['Records'][0]['Sns']['Message']

    if Subject == 'System Trouble Notification':
        found = re.search('{0=(.+?)}', message).group(1)
        print(found)

        time = iso_to_jstdt(found)

        fixed_time = time.strftime('%Y-%m-%d %H:%M')

        fixed_message = re.sub('{0=(.+?)}',fixed_time, message)

        notify_line(fixed_message)
    else:
        print('end')

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


def notify_line(message):
    line_notify_token = 'QTi1vgfOLEKOyfd9vmmilHk6fCiZSmPHDB2dEp5GtZT'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {message}'}
    requests.post(line_notify_api, headers = headers, data = data)

lambda_handler()