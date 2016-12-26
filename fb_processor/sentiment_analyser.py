import re
import itertools as it
from urllib.parse import urlparse, parse_qs
from configparser import ConfigParser
from facebook import GraphAPI


class SentimentAnalyser:
    FB_URL_PATTERN = re.compile(
        '(?:(?:http|https):\/\/)?(?:www.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)\/')

    def __init__(self, cfg_dict=None):
        if cfg_dict is None:
            cfg_dict = ConfigParser()
            cfg_dict.read('config.ini')
            cfg_dict = cfg_dict['default']

        self.facebook = GraphAPI()
        self.facebook.access_token = self.facebook.get_app_access_token(cfg_dict['FB_APP_ID'],
                                                                        cfg_dict['FB_APP_SECRET'])

    def process_fanpage(self, fanpage: str, post_limit: int = 100):
        fanpage = self.get_fanpage_name(fanpage)

        i = 0
        for post in self.get_all_posts(fanpage):
            tmp = self.process_post(post)
            if tmp is not None:
                return tmp
            i += 1
            if i > post_limit:
                break

    def process_post(self, post: dict):
        comments_sentim = list(map(lambda com: self.get_text_sentiment(com['message']),
                                   self.get_all_comments(post['id'])))
        if len(comments_sentim) == 0:
            return None
        else:
            return sum(comments_sentim)/len(comments_sentim)

    def get_fanpage_name(self, fanpage: str):
        if self.FB_URL_PATTERN.match(fanpage, 0):
            sub_url = self.FB_URL_PATTERN.sub('', fanpage)
            if sub_url.endswith('/'):
                return sub_url.replace('/', '')
            else:
                return sub_url.rsplit('/', 1)[0].replace('/', '')
        return fanpage.replace('/', '')

    def get_text_sentiment(self, text: str):
        from textblob import TextBlob
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def get_all_posts(self, page_name: str):
        return self.__get_all_connections(page_name, 'posts')

    def get_all_comments(self, post_id: str):
        return self.__get_all_connections(post_id, 'comments')

    def __get_all_connections(self, id: str, connection: str, **args):
        assert id is not None
        assert connection is not None

        while True:
            page = self.facebook.get_connections(id, connection, **args)
            for item in page['data']:
                yield item
            next_page = page.get('paging', {}).get('next')
            if not next_page:
                return
            args = parse_qs(urlparse(next_page).query)
            del args['access_token']
