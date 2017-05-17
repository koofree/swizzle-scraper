from googleapiclient.errors import HttpError


class Scraper:
    def __init__(self, connector):
        self.connector = connector
        pass

    def scrape(self, video_id, next_page_token=None, limit=10):
        count = 0
        youtube = self.connector

        while True:
            try:
                results = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    maxResults=20,
                    pageToken=next_page_token
                ).execute()
            except HttpError:
                raise

            for item in results["items"]:
                count += 1
                yield item
                if count >= limit:
                    break

            if 'nextPageToken' in results and not count >= limit:
                next_page_token = results['nextPageToken']
            else:
                break
