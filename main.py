import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv('graph_token')
TEAM_ID = os.getenv('team_id')
CHANNEL_ID = os.getenv('channel_id')
CHAT_ID = os.getenv('chat_id')

URL_CHANNEL = (f'https://graph.microsoft.com/beta/'
               f'teams/{TEAM_ID}/channels/{CHANNEL_ID}/messages')

URL_CHAT = (f'https://graph.microsoft.com/beta/'
            f'chats/{CHAT_ID}/messages')

headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

while True:
    try:
        # Вставить необходимую ссылку
        response = requests.get(URL_CHANNEL, headers=headers).json()
        # Использовать переменную из ссылки выше
        URL_CHANNEL = response.get('@odata.nextLink')
        value_list = response.get('value')
        with open('<required name>.json', 'a', encoding='utf-8') as outfile:
            for value in value_list:
                json.dump(value, outfile, ensure_ascii=False, indent=2)
    except Exception as error:
        raise Exception(error)
