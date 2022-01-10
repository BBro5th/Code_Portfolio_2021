from socket import *
import time
import calendar
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 modifiedMessage = message.decode().upper()
 print("you guessed...")
 print(modifiedMessage)
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)
 print("epoch time is")
 eptime = str(calendar.timegm(time.gmtime()))
 modtime = eptime.encode()
 #modtime, clientAddress = serverSocket.recvfrom(2048)
 sendtime = modtime.decode().upper()
 print(sendtime)

 serverSocket.sendto(sendtime.encode(), clientAddress)