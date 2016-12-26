import pytest

from fb_processor.sentiment_analyser import *
import itertools


class TestSentimentAnalyser:
    tested_obj = SentimentAnalyser()

    def test_should_get_ten_posts(self):
        obj = self.tested_obj.get_all_posts('CNNInternationalPoland')
        obj = list(itertools.islice(obj, 10))

        assert len(obj) == 10
        assert 'id' in obj[0]
        assert 'message' in obj[0]
        assert 'created_time' in obj[0]

    def test_should_get_ten_comments(self):
        obj = self.tested_obj.get_all_comments('90593452375_10154956421562376')
        obj = list(itertools.islice(obj, 10))

        assert len(obj) == 10
        assert 'id' in obj[0]
        assert 'message' in obj[0]
        assert 'created_time' in obj[0]

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

    @pytest.mark.parametrize("text_input,expected_fanpage_name", [
        ('https://www.facebook.com/CNNInternationalPoland/?fref=ts', 'CNNInternationalPoland'),
        ('https://www.facebook.com/CNNInternationalPoland/', 'CNNInternationalPoland'),
        ('https://www.facebook.com/CNNInternationalPoland', 'CNNInternationalPoland'),
        ('http://www.facebook.com/CNNInternationalPoland', 'CNNInternationalPoland'),
        ('CNNInternationalPoland', 'CNNInternationalPoland'),
        ('facebook.com/CNNInternationalPoland', 'CNNInternationalPoland'),
        ('facebook.com/CNNInternationalPoland/', 'CNNInternationalPoland')
    ])
    def test_should_return_fanpage_name_from_url(self, text_input, expected_fanpage_name):
        fanpage_name = self.tested_obj.get_fanpage_name(text_input)
        assert fanpage_name == expected_fanpage_name

    def test_should_process_fanpage(self):
        mean = self.tested_obj.process_fanpage('facebook.com/CNN/', post_limit=10)
        print(mean)
        assert mean > 0
