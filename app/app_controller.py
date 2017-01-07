from flask import jsonify, request
from flask_socketio import emit

from app import app, socketio, celery
from app.resources import get_fb
from fb_processor.fb_sentiment_analyser import FacebookSentimentAnalyser


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/api/reports/<fanpage_name>')
def get_report(fanpage_name):

    # TODO: check database

    return '', 404


@celery.task
def process_page(page_url):
    tmp = FacebookSentimentAnalyser(get_fb(), page_url)
    tmp.run()


@app.route('/api/analyze', methods=['POST'])
def analyze_post():
    page_url = request.json['pageUrl']

    # Run on Celery worker now
    task = process_page.delay(page_url)

    return jsonify({
        "taskId": task.task_id,
        'pageUrl': page_url,
        'results': {
            'positive': {'text': "positive comments", 'count': 12},
            'neutral': {'text': "neutral comments", 'count': 4},
            'negative': {'text': "negative comments", 'count': 20}
            }
        }), 202


@socketio.on('processing_status')
def route_message(message):
    emit(message['page'], message['data'], broadcast=True)


@app.errorhandler(404)
def angular_redirect(error):
    if request.path.startswith(('/api', '/images', '/styles', '/node_modules')):
        return error
    else:
        return root()
