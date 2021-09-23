#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('192.168.0.121', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message, clientAddress = connectionSocket.recvfrom(2048)
        message = message.decode()
        
        filename = message.split()[1]
        
        if(filename != "/HelloWorld.html"):
            filename = filename + ".html"
        
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found'.encode())
  
    connectionSocket.close()
        
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data