
from socket import * 
# Name and port number of the server to which want to connect
serverName = "ecs.fullerton.edu"
serverPort = 12000

# Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverName, serverPort))

# A string we want to send to the server

data = "Hello world! This is a very long string."

bytesSent = 0

while bytesSent != len(data):
    # Send that string
    bytesSent += clientSocket.send(data[bytesSent:])

# Close the socket
clientSocket.close()