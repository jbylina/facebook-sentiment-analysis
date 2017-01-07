import time
from fb_processor.fb_resource import FacebookResource
from socketIO_client import SocketIO


class FacebookSentimentAnalyser:
    def __init__(self, facebook_resource: FacebookResource, page: str, post_limit: int = 100):
        self.fb = facebook_resource
        self.page = page
        self.post_limit = post_limit
        self.socket_io = SocketIO('localhost', 5000)

    def run(self):
        fanpage = self.fb.extract_fanpage_name_from_url(self.page)

        reports = []
        i = 0
        for post in self.fb.get_all_posts(fanpage):

            post_report = self.process_post(post)
            self.publish_status({'status': 'POST_PROCESSED',
                                 'post': post,
                                 'report': post_report})
            reports.append(post_report)

            i += 1
            if i > self.post_limit:
                break

        final_report = self.merge_and_evalute_score(reports)
        self.publish_status({'status': 'PAGE_PROCESSED',
                             'report': final_report})
        return final_report

    def merge_and_evalute_score(self, reports):
        return {}

    def process_post(self, post: dict):
        comments_sentim = list(map(lambda com: self.get_text_sentiment(com['message']),
                                   self.fb.get_all_comments(post['id'])))

        if len(comments_sentim) == 0:
            return {}
        else:
            return {
                "score": sum(comments_sentim) / len(comments_sentim)
            }

    def preprocess_text(self, text: str):
        return None

    def get_text_sentiment(self, text: str):
        from textblob import TextBlob
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def publish_status(self, data):
        self.socket_io.emit('processing_status', {
            'page': self.page,
            'data': data
        })
