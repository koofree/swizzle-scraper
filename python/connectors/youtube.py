from googleapiclient.discovery import build


class Connector:
    def __init__(self, config):
        youtube_config = config['youtube']
        self.connector = build(youtube_config['service_name'],
                               youtube_config['api_version'],
                               developerKey=youtube_config['key'])

    def api(self):
        return self.connector
