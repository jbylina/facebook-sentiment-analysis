from flask import jsonify
from flask_socketio import send
from urllib.parse import urlparse, parse_qs
from app import app, socketio, fb


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/hello')
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


@socketio.on('message')
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
