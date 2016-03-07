'''main program'''
import socket
import sys
import pickle
import random
PORT = 4637
SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.bind(("0.0.0.0", PORT))
print "waiting on port:", PORT
clients = {}
players={}
# {ip: (port, name, sprite, team, ready)}

def lobby_phase():
    global clients
    try:
        while 1:
            data, addr = SOCK.recvfrom(1024)
            data = pickle.loads(data)
            print ("        %s, %s") % (data, addr[0])


            if data[0] == "j": # ("j")
                
                #name, sprite, team
                clients[addr[0]] = [addr[1], addr[0], random.choice(["0", "1", "2", "3"]), random.choice(["0", "1"]), False]
                SOCK.sendto(pickle.dumps((clients, addr[0])), addr)
                
            elif data[0] == "u": # ("u", name, sprite, team, ready)
                clients[addr[0]] = [addr[1], data[1], data[2], data[3], clients[addr[0]][4]]

            elif data[0] == "q":# ("q")
                del clients[addr[0]]
                

            if data[0] == "c" or data[0]=="u":
                for client in clients:
                    SOCK.sendto(pickle.dumps((data, addr)), (client, clients[client][0]))
            elif data[0] == "j":
                for client in clients:
                    if not client == addr[0]:
                        SOCK.sendto(pickle.dumps(("j", addr, (clients[addr[0]][2], clients[addr[0]][3]))), (client, clients[client][0]))   
            
            elif data[0] == "*": # ("*")
                clients[addr[0]][4] = not clients[addr[0]][4]
                for client in clients:
                    #if not client == addr[0]:
                    SOCK.sendto(pickle.dumps(("*", addr)), (client, clients[client][0]))
            else:            
                for client in clients:
                    if not client == addr[0]:
                        SOCK.sendto(pickle.dumps((data, addr)), (client, clients[client][0]))

            
            ready=False
            print clients
            if len(clients)!=0:
                ready=True
                for client in clients:
                    #print "%s:%s" % (client, clients[client][4])
                    print client
                    if not clients[client][4]:
                        ready=False
            if ready:
                map=random.choice(["0", "1", "2", "3"])
                for client in clients:
                    SOCK.sendto(pickle.dumps(("^", "SERVER", map)), (client, clients[client][0]))
                return
    except Exception,e: 
        print str(e)
        
# {ip: (port, name, sprite, team, (posx, posy), health, anim, frame)}    
def game_phase():
    score_limit=5
    for client in clients:
        players[client]=[clients[client][0], clients[client][1], clients[client][2], clients[client][3], (0,0), 1000, 0, 0]
    
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
            elif data[0] == "d":
                team_points[int(clients[addr[0]][3])]+=1
                print team_points
                for client in players:
                        SOCK.sendto(pickle.dumps(("p", "SERVER", team_points)), (client, clients[client][0]))
                if team_points[0]==score_limit:
                    for client in clients:
                        SOCK.sendto(pickle.dumps(("0", "SERVER")), (client, clients[client][0]))
                    return True
                elif team_points[1]==score_limit:
                    for client in clients:
                        SOCK.sendto(pickle.dumps(("1", "SERVER")), (client, clients[client][0]))
                    return True
            for client in clients:
                if not client == addr[0]:
                    SOCK.sendto(pickle.dumps((data, addr[0])),
                                (client, clients[client][0]))
    except Exception,e: 
        print str(e)

def main():
    '''the main loop'''  
    restart=True
    global clients 
    global players
    while restart:
        restart=False
        clients = {}
        players={}
        print '\nstarting lobby phase'
        lobby_phase()
        print '\nstarting game phase'
        restart=game_phase()

if __name__ == "__main__":
    main()
