import re
from urllib.parse import urlparse, parse_qs
from configparser import ConfigParser
from facebook import GraphAPI


class FacebookResource:

    FB_URL_PATTERN = re.compile('(?:(?:http|https)://)?(?:www.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)/')

    def __init__(self, cfg_dict=None):
        if cfg_dict is None:
            cfg_dict = ConfigParser()
            cfg_dict.read('config.ini')
            cfg_dict = cfg_dict['default']

        self.facebook = GraphAPI()
        self.facebook.access_token = self.facebook.get_app_access_token(cfg_dict['FB_APP_ID'],
                                                                        cfg_dict['FB_APP_SECRET'])

    def extract_fanpage_name_from_url(self, url: str):
        if self.FB_URL_PATTERN.match(url, 0):
            sub_url = self.FB_URL_PATTERN.sub('', url)
            return sub_url.rsplit('/', 1)[0].replace('/', '')
        return url

    def get_all_posts(self, page_name: str):
        return self.__get_all_connections(page_name, 'posts')

    def get_all_comments(self, page_id: str, post_id: str):
        return self.__get_all_connections(page_id + '_' + post_id, 'comments')

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
