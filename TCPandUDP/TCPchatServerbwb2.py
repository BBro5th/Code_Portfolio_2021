import socket
import threading

host = '127.0.0.1'
port = 54545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients =[]
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left!' ".format(nickname).encode())
            break

def receive():
    while True:
        client, address = server.accept()
        print ("connected with {}".format(str(address)))
        client.send('NICK'.encode())
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)
        print("Name is {}".format(name))
        broadcast("{} joined ".format(name).encode())
        client.send('connected to the server!'.encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()