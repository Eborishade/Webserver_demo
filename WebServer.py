#import socket module
from socket import *
import sys # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)


#Prepare a sever socket
host = "127.0.0.1"
port = 5001
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

#Client GET Request:

#"GET / HTTP/1.1\r\n"  ---requests root file
#"Host: 127.0.0.1\r\n"
#"User-Agent: PythonClient/1.0\r\n" ---different if browser
#"Accept: text/html\r\n"
#"\r\n"

#BROWSER ACCESS: http://127.0.0.1:5001/HelloWorld.html or http://127.0.0.1:5001/ANI_HelloWorld.html

    try:
        message = connectionSocket.recv(1024).decode() # receive HTTP request
        filename = message.split()[1]
        f = open(filename[1:]) # open the requested file

        outputdata = f.read() # read the content of the file
        print(outputdata) # print to terminal for confirmation

        #Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        #Send response message for file not found
        header = "HTTP/1.1 404 Not Found\n\r\n"
        connectionSocket.send(header.encode())

        #Close client socket
        connectionSocket.close()

connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
