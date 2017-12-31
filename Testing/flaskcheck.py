from flask import Flask, request, render_template
from flaskrunner import *
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    #return "Hello World!"

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	check(text)
	return text

if __name__ == '__main__':
    app.run(host='192.168.43.195', debug="True")
    # either leave host empty to use localhost or
    # use the IPV4 address of your laptop
