from urllib.parse import urlparse, parse_qs
from configparser import ConfigParser
from facebook import GraphAPI


class SentimentAnalyser:

    def __init__(self, cfg_dict=None):
        if cfg_dict is None:
            cfg_dict = ConfigParser()
            cfg_dict.read('config.ini')
            cfg_dict = cfg_dict['default']

        self.facebook = GraphAPI()
        self.facebook.access_token = self.facebook.get_app_access_token(cfg_dict['FB_APP_ID'], cfg_dict['FB_APP_SECRET'])

    def process_comment(self, text):
        from textblob import TextBlob
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def get_all_posts(self, page_name):
        return self.__get_all_connections(page_name, 'posts')

    def get_all_comments(self, post_id):
        return self.__get_all_connections(post_id, 'comments')

    def __get_all_connections(self, id, connection, **args):
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
