from flask import jsonify, request
from flask_socketio import send
from urllib.parse import urlparse, parse_qs
from app import app, socketio, fb


@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def angularRedirect(error):
    if request.path.startswith(('/api', '/images', '/styles')):
        return error
    else:
        return main()

@app.route('/api/hello')
def hello():
    obj = get_all_connections('WirtualnaPolska', 'posts')

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


def get_all_connections(id, connection, **args):
    while True:
        page = fb.get_connections(id, connection, **args)
        for item in page['data']:
            yield item
        next = page.get('paging', {}).get('next')
        if not next:
            return
        args = parse_qs(urlparse(next).query)
        del args['access_token']
