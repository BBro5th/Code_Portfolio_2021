import socket
import threading

name = input("Choose your name")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 54545))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "NICK" :
                client.send(name.encode())
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(name, input(''))
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
