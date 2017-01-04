import time
from flask import jsonify, request, url_for
from flask_socketio import send
from app import app, socketio, celery
from app.db_resource import get_db


@app.route('/')
def root():
    db = get_db()
    return app.send_static_file('index.html')

# allows use of deep links, ie '/chart?pageUrl=facebook.com/cocacola'
# will correctly redirect to '/' ng app and the app will correctly navigate internally to requested view
@app.errorhandler(404)
def angular_redirect(error):
    if request.path.startswith(('/api', '/images', '/styles', '/node_modules')):
        return error
    else:
        return root()


@app.route('/api/reports/<fanpage_name>')
def get_report(fanpage_name):
    
    # TODO: check database

    return '', 404


@celery.task
def fanpage_analyzer(fanpage_name):
    """Background task that runs a long function with progress reports."""

    for i in range(1, 10):
        print("Analyzer loop for " + fanpage_name + " : " + str(i))
        time.sleep(5)


#@app.route('/api/analyze', methods=['POST'])
def analyze_post():
    data = request.json
    url = data['url']

    task = fanpage_analyzer.delay(url)
    return jsonify({
        "task": task.id
    }), 202

    obj = get_all_connections('WirtualnaPolska', 'posts')

    ret = {

    }
    # for index, item in enumerate(obj):
    #     print(item)
    #
    #     post_id = item.get('id')
    #     comments = fb.get_connections(post_id, 'comments')
    #     item['comments'] = comments
    #     ret.append(item)
    #     if index == 99:
    #         break

    return jsonify(ret)


@app.route('/api/hello')
def hello():
    ret = []
    # for index, item in enumerate(obj):
    #     print(item)
    #
    #     post_id = item.get('id')
    #     comments = fb.get_connections(post_id, 'comments')
    #     item['comments'] = comments
    #     ret.append(item)
    #     if index == 99:
    #         break

    return jsonify(ret)


@app.route('/api/analyze')
def analyze():
    pageUrl = request.args['pageUrl']
    return jsonify({
        'pageUrl': pageUrl,
        'results': {
            'positive': {'text': "positive comments", 'count': 12},
            'neutral': {'text': "neutral comments", 'count': 4},
            'negative': {'text': "negative comments", 'count': 20}
            }
        })

@socketio.on('/api/message')
def handle_message(message):
    print('received message: ' + str(message))
    send(message)
