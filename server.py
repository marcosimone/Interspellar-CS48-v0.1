
import socket, sys
import pickle
PORT = 4637
SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.bind(("0.0.0.0", PORT))
print "waiting on port:", PORT
# {ip: (port, name, sprite, team)}
clients = {}
team_points = (0, 0)

class GameStart(Exception):
    pass


print '\nstarting lobby phase'

try:
    while 1:
        data, addr = SOCK.recvfrom(1024)
        data = pickle.loads(data)
        print ("        %s, %s") % (data, addr[0])


        if data[0] == "j": # ("j")
            SOCK.sendto(pickle.dumps(clients), addr)
            #name, sprite, team
            clients[addr[0]] = (addr[1], addr[0], "default", "default")
            print clients

        elif data[0] == "u": # ("u", name, sprite, team)
            clients[addr[0]] = (addr[1], data[1], data[2], data[3])

        elif data[0] == "q":# ("q")
            del client[addr[0]]

        elif data[0] == "*": # ("*")
            raise GameStart

        for client in clients:
            if not client == addr[0]:
                SOCK.sendto(pickle.dumps((data, addr[0])), (client, clients[client][0]))

except GameStart:
    pass


print '\nstarting game phase'

sys.exit()

while 1:
    data, addr = SOCK.recvfrom(1024)
    data = pickle.loads(data)
    print ("        %s, %s") % (data, addr[0])


    if data[0].equals("j"):
        #name, sprite, team
        SOCK.sendto(pickle.dumps(clients), addr)
        clients[addr[0]] = (data[1], "default", "default")

    elif data[0].equals("q"):
        del client[addr[0]]


    for client in clients:
        if not client.equals(addr[0]):
            SOCK.sendto(pickle.dumps((addr[0], data)),
                        (client, clients[client][0]))
