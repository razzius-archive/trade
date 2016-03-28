import itertools
import json
import logging
import os

import requests
import websocket


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    token = os.environ['SLACK_API_TOKEN']
    slack_response = requests.get('https://slack.com/api/rtm.start', params={'token': token}).json()

    websocket_url = slack_response['url']

    ws = websocket.WebSocket()
    ws.connect(websocket_url)

    for index in itertools.count():
        message = json.loads(ws.recv())

        logging.info(message)

        if 'channel' in message:
            response_json = {
                'id': index,
                'channel': message['channel'],
                'type': 'message',
                'text': json.dumps(message)
            }

            ws.send(json.dumps(response_json))

# todo
# INFO:root:
{
    'user': 'U0SERP6UU',
    'item': {
        'ts': '1459112109.000012',
        'type': 'message',
        'channel': 'C0VHSCGTY'
    },
    'reaction': 'thinking_face',
    'item_user': 'U0VHL5YQL',
    'event_ts': '1459112191.707354',
    'type': 'reaction_added'
}
