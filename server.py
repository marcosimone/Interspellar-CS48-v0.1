import socket, sys
import pygame

port = 4637
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", port))
print "waiting on port:", port
while 1:
	data, addr = sock.recvfrom(1024)
	print data

	if data=="<Event(12-Quit {})>":
		sock.close()
		sys.exit()