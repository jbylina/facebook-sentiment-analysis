import os

from celery import Celery
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='secret!',
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',

))

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

socketio = SocketIO(app)

from app import db_resource
from app import fb_sentiment_analyser
