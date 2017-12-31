import bluetooth  # from PyBluez

def starting():
	print "Searching for devices..."
	print "Ensure that the required bluetooth device is paired"

	nearby_devices = bluetooth.discover_devices()

	num = 0
	print "Select your device by entering its coresponding number..."
	for i in nearby_devices:
		num+=1
		print num , ": " , bluetooth.lookup_name( i )

	# bluetooth module must be paired

	selection = input("> ") - 1
	# print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
	bd_addr = nearby_devices[selection]

	port = 1
	sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	print "Connected"
	return sock

#Create the GUI
def application(check, s):
	# sock=starting()
	sock = s
	if(check=="disconnect"):
    	#Close socket connection to device
		sock.close()
        
	if(check=="on"):
    	#Send 'on' which the Arduino detects as turning the light on
		data = "1"
		sock.send(data)

	if(check=="off"):
    	#Send 'off' to turn off the light attached to the Arduino
		data = "0"
		sock.send(data)