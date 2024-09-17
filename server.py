from flask import render_template,Flask
from flask_socketio import SocketIO, send,emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def main():
    return render_template("index.html")


@socketio.on('message')
def handle_message(message):
    print(f"received {message}")
    emit('response', f'Hello from server! Received your message: {message}')

if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)