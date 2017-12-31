from flask import Flask, request, render_template
# import bluetooth
import btcheck as bt

# def btconnect():
# 	print "Searching for devices..."

# 	nearby_devices = bluetooth.discover_devices()

# 	num = 0
# 	print "Select your device by entering its coresponding number..."
# 	for i in nearby_devices:
# 		num+=1
# 		print num , ": " , bluetooth.lookup_name( i )

# 	# bluetooth module must be paired

# 	selection = input("> ") - 1
# 	print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
# 	bd_addr = nearby_devices[selection]

# 	port = 1
# 	print "hi1"
# 	sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# 	sock.connect((bd_addr, port))

# def runner(inp):
# 	if(check=="disconnect"):
#     	#Close socket connection to device
# 		sock.close()
        
# 	if(check=="on"):
#     	#Send 'H' which the Arduino
#     	#detects as turning the light on
# 		data = "1"
# 		sock.send(data)

# 	if(check=="off"):
#     	#Send 'L' to turn off the light
#     	#attached to the Arduino
# 		data = "0"
# 		sock.send(data)


app = Flask(__name__)

sock = 0

@app.route('/')
def hello():
	return render_template('index.html')
	#return "Hello World!"

@app.route('/', methods=['POST'])
def my_form_post():
	global sock
	text = request.form['text']
	bt.application(text, sock)
	return text

if __name__ == '__main__':
	sock = bt.starting()
	app.run(host='192.168.43.195', debug="True", port=1111)
    # either leave host empty to use localhost or
    # use the IPV4 address of your laptop
