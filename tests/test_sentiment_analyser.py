from fb_processor.facebook_sentiment_processor import *


class TestFacebookSentimentProcessor:
    tested_obj = FacebookSentimentProcessor(FacebookResource())

    def test_should_get_negative_text_polarity(self):
        text = 'Bad idea! I hate you'

        val = self.tested_obj.get_text_sentiment(text)
        print(val)
        assert val < 0

    def test_should_get_positive_text_polarity(self):
        text = 'I really like this :)'

        val = self.tested_obj.get_text_sentiment(text)
        print(val)
        assert val > 0

    def test_should_process_fanpage(self):
        mean = self.tested_obj.process_fanpage('facebook.com/CNN/', post_limit=10)
        print(mean)
        assert mean > 0
