'''main program'''
import socket
import sys
import pickle
PORT = 4637
SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.bind(("0.0.0.0", PORT))
print "waiting on port:", PORT
clients = {}

# {ip: (port, name, sprite, team)}

def lobby_phase():
    global clients
    try:
        while 1:
            data, addr = SOCK.recvfrom(1024)
            data = pickle.loads(data)
            print ("        %s, %s") % (data, addr[0])


            if data[0] == "j": # ("j")
                
                #name, sprite, team
                clients[addr[0]] = [addr[1], addr[0], "default", "default", False]
                SOCK.sendto(pickle.dumps(clients), addr)
                
            elif data[0] == "u": # ("u", name, sprite, team, ready)
                clients[addr[0]] = [addr[1], data[1], data[2], data[3], clients[addr[0]][4]]

            elif data[0] == "q":# ("q")
                del clients[addr[0]]
                

            if data[0] == "c" or data[0]=="u":
                for client in clients:
                    SOCK.sendto(pickle.dumps((data, addr)), (client, clients[client][0]))
            else:            
                for client in clients:
                    if not client == addr[0]:
                        SOCK.sendto(pickle.dumps((data, addr)), (client, clients[client][0]))

            if data[0] == "*": # ("*")
                clients[addr[0]][4] = not clients[addr[0]][4]
                for client in clients:
                    if not client == addr[0]:
                        SOCK.sendto(pickle.dumps(("*", addr)), (client, clients[client][0]))
                
            ready=False
            if len(clients)!=0:
                ready=True
                for client in clients:
                    print "%s:%s" % (client, clients[client][4])
                    if not clients[client][4]:
                        ready=False
            if ready:
                for client in clients:
                    SOCK.sendto(pickle.dumps(("^", "SERVER")), (client, clients[client][0]))
                return
    except Exception,e: 
        print str(e)
        
def game_phase():
    try:
        team_points = [0, 0]
        point_limit=25
        while 1:
            if len(clients)==0:
                return True
            data, addr = SOCK.recvfrom(1024)
            data = pickle.loads(data)
            print ("        %s, %s") % (data, addr[0])

            if data[0] == "q":
                del clients[addr[0]]

            for client in clients:
                #if not client == addr[0]:
                SOCK.sendto(pickle.dumps((addr[0], data)),
                                (client, clients[client][0]))
    except Exception,e: 
        print str(e)

def main():
    '''the main loop'''  
    restart=True
    while restart:
        
        print '\nstarting lobby phase'
        lobby_phase()
        print '\nstarting game phase'
        restart=game_phase()

if __name__ == "__main__":
    main()
