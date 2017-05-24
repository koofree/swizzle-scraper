import json

END_POINT = "https://api.twitter.com/1.1/"
END_SEARCH_TWEET = END_POINT + "search/tweets.json"
END_USER_TIMELINE = END_POINT + "statuses/user_timeline.json"


class Scraper:
    def __init__(self, connector):
        self.connector = connector
        self.count = 0
        pass

    def scrape(self, video_id, limit=10):
        res, data = self.connector.request(END_SEARCH_TWEET + ("?q=%s&count=%s&result_type=mixed" % (video_id, limit)))
        for item in json.loads(data)['statuses']:
            yield item
