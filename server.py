import socket, sys
import pickle

port = 4637
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", port))
print "waiting on port:", port
clients={}
while 1:
	data, addr = sock.recvfrom(1024)
	data=pickle.loads(data)
	print ("        %s, %s") % (data, addr[0])
	
	clients[addr[0]]=data
	for client in clients:
		if c=addr:
			sock.sendto(pickle.dumps((addr[0], pickle.loads(data))),client)
	
		