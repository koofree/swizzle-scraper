import oauth2

END_POINT = "https://api.twitter.com/1.1/"
END_SEARCH_TWEET = END_POINT + "search/tweets.json"
END_USER_TIMELINE = END_POINT + "statuses/user_timeline.json"


class Connector:
    def __init__(self, config):
        twitter_config = config['twitter']

        consumer = oauth2.Consumer(key=twitter_config['consumer_key'], secret=twitter_config['consumer_secret'])
        token = oauth2.Token(key=twitter_config['token_key'], secret=twitter_config['token_secret'])
        self.connector = oauth2.Client(consumer, token)

    def api(self):
        return self.connector


if __name__ == '__main__':
    from os import path
    import json

    ROOT_DIR = path.dirname(path.abspath(__file__))

    with open(path.join(ROOT_DIR, '../../config.json'), 'r') as config_file:
        config_json = json.load(config_file)

    api = Connector(config_json['connectors']).api()

    # res, data = api.request(END_SEARCH_TWEET + '?q=축구&result_type=mixed', method="GET")
    # json_result = json.loads(data, encoding='utf-8')
    # for status in json_result['statuses']:
    #     print(status)

    res, data = api.request(END_USER_TIMELINE, method="GET")
    json_result = json.loads(data, encoding='utf-8')
    print(json_result)
    for status in json_result:
        print(status)
