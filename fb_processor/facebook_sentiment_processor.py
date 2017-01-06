from fb_processor.facebook_resource import *


class FacebookSentimentProcessor:

    def __init__(self, facebook_resource: FacebookResource):
        self.fb = facebook_resource

    def process_fanpage(self, fanpage: str, post_limit: int = 100, event_callback=lambda a, b: None):
        fanpage = self.fb.extract_fanpage_name_from_url(fanpage)

        reports = []
        i = 0
        for post in self.fb.get_all_posts(fanpage):

            post_report = self.process_post(post)
            event_callback('POST_PROCESSED', {'post': post,
                                              'report': post_report})
            reports.append(post_report)

            i += 1
            if i > post_limit:
                break

        final_report = self.merge_and_evalute_score(reports)
        event_callback('PAGE_PROCESSED', {'report': final_report})
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
