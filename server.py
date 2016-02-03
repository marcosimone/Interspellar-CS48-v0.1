#-------------------------------------------------------------#
#              Interspellar Protocol v0.2                     #
#-------------------------------------------------------------#
#     s(tatus):  ("s", (posx, posy), (health, anim, frame))   #
#        -(posx, posy) ~ tuple (double, double)               #
#        -(health, animation, frame) ~ tuple (int, int, int)  #
#                                                             #
#                                                             #
#     b(ullet):  ("b", bulletString)                          #
#        bulletString: ~ string seperated by commas           #
#          -id ~ int                                          #
#          -posx ~ double                                     #
#          -posy ~ double                                     #
#          -angle ~ double                                    #
#          -sender ~ string                                   #
#                                                             #
#     d(eath): ("d", name, killer)                            #
#        -name ~ string                                       #
#        -killer ~ string                                     #
#                                                             #
#     j(oin):  ("j", name, sprite, team)                      #
#        -name ~ string                                       #
#        -sprite ~ int?                                       #
#        -team ~ int?                                         #
#                                                             #
#     q(uit):  ("q", name)                                    #
#        -name ~ string                                       #
#                                                             #
#-------------------------------------------------------------#
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
	
	if data[0].equals("j"):
		clients[addr[0]]=(addr[1],data[1], data[2], data[3])
		
	elif data[0].equals("q"):
		del client[addr[0]]
	
	#for client in clients:
	#	if not client.equals(addr[0]):
	#		sock.sendto(pickle.dumps((addr[0], data)),(client, clients[client][0]))  #might need to make data -> pickle.loads(data)
	