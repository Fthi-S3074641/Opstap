from flask import render_template, request, jsonify, redirect, Response, Flask
import json
from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
from datetime import datetime
import time
import redis


app = Flask(__name__)
app.secret_key = 'asdf'
red = redis.StrictRedis()


def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        print (message)
        yield 'data: %s\n\n' % message['data']
# gunicorn  --worker-class=gevent -t 99999 spp:spp

cluster= Cluster()
session = cluster.connect('opstap')



@app.route('/')
def index():
    # session.row_factory = tuple_factory    
    # rows = session.execute("SELECT * FROM feedback WHERE feedb='stream id' LIMIT 2");
    # for row in rows:
        # tweet1 = row.feedb
    return render_template('commenter.html')

@app.route('/post', methods=['POST'])
def post():
    message =  request.form['message']
    print(message)
    red.publish('chat', message.encode('utf-8').strip())#u'[%s] %s: %s' % (now.isoformat(), user, )
    return Response(status=204)


@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.json#(silent=True)#['Let us know the things you liked about De Opstap?']
    print(username)
    param_feedb = username['Let us know the things you liked about De Opstap']
    param_datetimenow = int(time.time()*1000);
    query = "INSERT INTO feedback (feedb, created_date) VALUES (?, ?)"
    prepared = session.prepare(query)
    session.execute(prepared, (param_feedb,param_datetimenow))
    # session.row_factory = tuple_factory    
    # rows = session.execute("SELECT * FROM feedback WHERE feedb='stream id' LIMIT 10");    
    # for row in rows:
    red.publish('chat', username['Let us know the things you liked about De Opstap'])#.encode('utf-8').strip())
    return jsonify(bol = username['Let us know the things you liked about De Opstap'], username = username['Let us know the things you liked about De Opstap'])
    # return render_template('commenter.html', comment = username)
    # return redirect(url_for('index'))


@app.route('/stream')
def stream():
    return Response(event_stream(),
                          mimetype="text/event-stream")


if __name__ == '__main__':
    app.debug = True
    app.host= '0.0.0.0'
    app.run()