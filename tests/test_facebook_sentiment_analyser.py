from configparser import ConfigParser
from fb_processor.fb_sentiment_analyser import *
import pytest


class TestFacebookSentimentProcessor:

    def __init__(self):
        cfg_dict = ConfigParser()
        cfg_dict.read('config.ini')
        cfg_dict = cfg_dict['default']
        self.fb_resource = FacebookResource(cfg_dict['FB_APP_ID'], cfg_dict['FB_APP_SECRET'])
        self.tested_obj = FacebookSentimentAnalyser(self.fb_resource, 'facebook.com/CNN/', post_limit=2)

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

    @pytest.mark.skip(reason="Still in development")
    def test_should_process_fanpage(self):
        mean = self.tested_obj.run()
        print(mean)
        assert mean > 0
