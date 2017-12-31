import bluetooth  # from PyBluez

#sock = 0

def starting():
	print "Searching for devices..."

	nearby_devices = bluetooth.discover_devices()

	num = 0
	print "Select your device by entering its coresponding number..."
	for i in nearby_devices:
		num+=1
		print num , ": " , bluetooth.lookup_name( i )

	# bluetooth module must be paired

	selection = input("> ") - 1
	print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
	bd_addr = nearby_devices[selection]

	port = 1
	print "hi1"
	sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	return sock

#Create the GUI
def application(check, s):
	# sock=starting()
	sock = s
#Create a connection to the socket for Bluetooth communication
	print "hi3"
	if(check=="disconnect"):
    	#Close socket connection to device
		sock.close()
        
	if(check=="on"):
    	#Send 'H' which the Arduino
    	#detects as turning the light on
		data = "1"
		sock.send(data)

	if(check=="off"):
    	#Send 'L' to turn off the light
    	#attached to the Arduino
		data = "0"
		sock.send(data)

#Begin the GUI processing
# check="off"
# while(check!="disconnect"):
# 	application(check)
# 	check = raw_input()