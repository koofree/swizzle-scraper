import json
import requests


class Connector:
    def __init__(self, config):
        facebook_config = config['facebook']

        payload = {'grant_type': 'client_credentials',
                   'client_id': facebook_config['app_id'],
                   'client_secret': facebook_config['app_secret']}
        file = requests.post('https://graph.facebook.com/oauth/access_token?', params=payload)
        json_text = json.loads(file.text)
        access_token = json_text['access_token']

        self.connector = {
            "access_token": access_token
        }

    def api(self):
        return self.connector


if __name__ == '__main__':
    import os

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(ROOT_DIR, '../../config.json'), 'r') as config_file:
        config_json = json.load(config_file)

    conn = Connector(config_json['connectors'])
