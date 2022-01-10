from socket import *
import select
import sys

serverPort = 12040
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)
list_of_clients = []

def clientthread(conn, addr):
    conn.send("Welcome to the Chat room!")

    while True:
            try:
                message = conn.recv(2048)
                if message:
                    print ("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)

                else:
                    remove(conn)
            except:
                continue
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    print ("the server is ready")
    connectionSocket, addr = serverSocket.accept()

    list_of_clients.append(conn)
    print (addr[0] + " connected")
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()