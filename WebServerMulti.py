#import socket module
from socket import *
import sys
import threading # In order to terminate the program


#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 5001
serverSocket.bind((host, port))
serverSocket.listen(5) #handle max 5 clients (5 threads?)

def handle_client(connectionSocket, thread_name):
    print("Thread %s Received request from %s" % (thread_name, connectionSocket))

    try:
        #Recieve Request
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        #Open and read requested file
        f = open(filename[1:]) 
        outputdata = f.read() 
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


while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("Accepted connection from %s" % str(addr))
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, threading.current_thread().__getattribute__))
    client_thread.start()

#Client GET Request:

#"GET / HTTP/1.1\r\n"  ---requests root file 
#"Host: 127.0.0.1\r\n"
#"User-Agent: PythonClient/1.0\r\n" ---different if browser 
#"Accept: text/html\r\n"
#"\r\n"

#BROWSER ACCESS: http://127.0.0.1:5001/HelloWorld.html or http://127.0.0.1:5001/ANI_HelloWorld.html  

serverSocket.close()
sys.exit() #unreachable