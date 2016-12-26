from celery import Celery
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

socketio = SocketIO(app)

from app import fb_sentiment_analyser
