import socket, sys
import pickle

port = 4637
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", port))
print "waiting on port:", port
clients=[]
while 1:
	data, addr = sock.recvfrom(1024)
	if data=="QUIT":
		sock.close()
		sys.exit()
	if not any(addr[0] in client for client in clients):
		clients.append(addr)
		print clients
		
	print ("        %s, %s") % (pickle.loads(data), addr[0])
	for client in clients:
		if client!=addr:
			sock.sendto(pickle.dumps((addr[0], pickle.loads(data))),client)
	