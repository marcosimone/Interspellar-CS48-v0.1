import socket, sys
import pygame
import pickle

port = 4637
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.1.10", port))
print "waiting on port:", port
while 1:
	data, addr = sock.recvfrom(1024)
	sock.sendto(pickle.dumps((addr[0], pickle.loads(data))),addr)
	
	if data=="<Event(12-Quit {})>":
		sock.close()
		sys.exit()