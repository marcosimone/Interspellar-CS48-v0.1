import socket, sys
import pygame
import pickle

port = 4637
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.43.194", port))
print "waiting on port:", port
clients=[]
while 1:
	data, addr = sock.recvfrom(1024)
	if addr not in clients:
		clients.append(addr)
		print clients
		
	print ("        %s, %s") % (pickle.loads(data), addr[0])
	for client in clients:
		if client!=addr:
			sock.sendto(pickle.dumps((addr[0], pickle.loads(data))),client)
	
	if data=="<Event(12-Quit {})>":
		sock.close()
		sys.exit()