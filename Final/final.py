from flask import Flask, request, render_template

import btcheck as bt

app = Flask(__name__)

sock = 0

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	global sock
	text = request.form['text']
	bt.application(text, sock)
	return text

if __name__ == '__main__':
	sock = bt.starting()
	app.run(host='192.168.43.195', port=1111) 
    # either leave host empty to use localhost or
    # use the IPV4 address of your laptop
    # you may use your own port too
