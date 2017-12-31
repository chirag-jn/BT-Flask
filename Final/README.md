# BT+Flask

Project completed.

We can use this module to connect to an Arduino and send instructions to it by connecting Arduino to any system (which has the capability to run Flask (and necessarily Python)) using Bluetooth.

Steps to run the file:
1. Open final.py, and in the last line, change host="127.0.0.1" to host="addr" where addr is the IPV4 address of your laptop.
2. Pair the Bluetooth module with your laptop. Usually the pairing code is 1234
3. Run final.py using python2
4. Choose the bluetooth module of Arduino (usually labelled as HC-05)
5. Now, go to the website you entered for hosting from any device connected to the network.
6. The usual syntax is 192.168.x.x:5000 (where 192.168.x.x is your IPV4 address on the network, 5000 is the default port)
