from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Worl!"

if __name__ == '__main__':
    app.run(host='192.168.43.195', debug="True")
