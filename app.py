from flask import Flask
import socket
import datetime

app = Flask(__name__)
count = 0

@app.route('/')
def hello():
    global count
    count = count + 1
    return '''<h4>Hello, world!</h4><p>I\'ve been hit {0} times.</p><p>Date: {1}</p>
    <p>Served from: {2} </p>'''. format(str(count),datetime.datetime.now(),socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)