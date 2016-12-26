from fb_processor.sentiment_analyser import *
import itertools


class TestSentimentAnalyser:
    tested_obj = SentimentAnalyser()

    def test_should_get_ten_posts(self):
        obj = self.tested_obj.get_all_posts('WirtualnaPolska')
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

        val = self.tested_obj.process_comment(text)
        print(val)
        assert val < 0

    def test_should_get_positive_text_polarity(self):
        text = 'I really like this :)'

        val = self.tested_obj.process_comment(text)
        print(val)
        assert val > 0
