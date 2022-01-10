from socket import *
import time
import calendar
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#messege part
message = "whats the time"
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
#time part
#modtime =str( calendar.timegm(time.gmtime()))

#clientSocket.sendto(modtime.encode(),(serverName, serverPort))
sendtime, serverAddress = clientSocket.recvfrom(2048)
print("It be ...")
print(sendtime.decode())
clientSocket.close()