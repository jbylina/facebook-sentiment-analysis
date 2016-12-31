import pytest

from fb_processor.facebook_resource import *
import itertools


class TestFacebookProcessor:
    tested_obj = FacebookResource()

    def test_should_get_ten_posts(self):
        obj = self.tested_obj.get_all_posts('CNNInternationalPoland')
        obj = list(itertools.islice(obj, 10))

        assert len(obj) == 10
        assert 'id' in obj[0]
        assert 'message' in obj[0]
        assert 'created_time' in obj[0]

    def test_should_get_ten_comments(self):
        obj = self.tested_obj.get_all_comments('90593452375', '10154956421562376')
        obj = list(itertools.islice(obj, 10))

        assert len(obj) == 10
        assert 'id' in obj[0]
        assert 'message' in obj[0]
        assert 'created_time' in obj[0]

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
        fanpage_name = self.tested_obj.extract_fanpage_name_from_url(text_input)
        assert fanpage_name == expected_fanpage_name
