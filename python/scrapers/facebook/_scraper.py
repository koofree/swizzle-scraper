import requests

PAGE_END_POINT = "https://graph.facebook.com/v2.5/%s/posts?access_token=%s&fields=" \
                 "id,from,message,link,name,message_tags,type,status_type,shares,created_time"
GROUP_END_POINT = "https://graph.facebook.com/v2.9/%s/feed?access_token=%s&fields=" \
                  "id,from,message,link,name,message_tags,type,status_type,shares,created_time"
COMMENT_END_POINT = "https://graph.facebook.com/v2.5/%s/comments?summary=true&" \
                    "access_token=%s&fields=name,message_tags,message,from,created_time,id"


class AbstractScraper:
    def __init__(self, connector, id_type):
        if id_type == 'page':
            self.end_point = PAGE_END_POINT
        else:
            self.end_point = GROUP_END_POINT
        self.connector = connector

        pass

    def scrape(self, page_id, limit=10):
        count = 0
        url = self.end_point % (page_id, self.connector['access_token'])
        while True:
            page_res = requests.get(url)
            page_data = page_res.json()

            for page_item in page_data['data']:
                post_id = page_item['id']

                url = COMMENT_END_POINT % (post_id, self.connector['access_token'])

                while True:
                    comment_res = requests.get(url)
                    comment_data = comment_res.json()

                    for item in comment_data['data']:
                        count += 1
                        yield item
                        if count >= limit:
                            break

                    if 'paging' in comment_data and 'next' in comment_data['paging'] and not count >= limit:
                        url = comment_data['paging']['next']
                    else:
                        break
                        # end of comment scrape

            if 'paging' in page_data and 'next' in page_data['paging'] and not count >= limit:
                url = page_data['paging']['next']
            else:
                break
