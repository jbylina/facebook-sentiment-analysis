from flask import Flask
from flask_socketio import SocketIO
from configparser import ConfigParser
from facebook import GraphAPI

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

cfg = ConfigParser()
cfg.read('app/config.ini')
cfg = cfg['default']

# Facebook app details
FB_APP_ID = cfg['FB_APP_ID']
FB_APP_NAME = cfg['FB_APP_NAME']
FB_APP_SECRET = cfg['FB_APP_SECRET']

fb = GraphAPI()
fb.access_token = fb.get_app_access_token(FB_APP_ID, FB_APP_SECRET)

from app import fb_sentiment_analyser
