# Server Code
from socket import *
import sendFileServer as SFS
import receiveAllData as rAD
import sys


if __name__ == "__main__":

    numOfArguments = len(sys.argv)
    if numOfArguments == 2:
        serverPort = sys.argv[1]
        if serverPort.isdigit():
            print("Server port is in right format")
            serverPort = int(serverPort)
        else:
            print("Server port needs to be a digit")
    else:
        print("Incorrect invocation. Server should be invoked as: "
              "server.py <server port>")
        quit()

    serverSocket = socket(AF_INET, SOCK_STREAM)

    print("Server port is :", serverPort)
    # Bind the socket to the port
    serverSocket.bind(('', serverPort))

    # Start listening for incoming connections
    serverSocket.listen(1)

    print("The server is ready to receive...")

    while True:

        connectionSocket, addr = serverSocket.accept()

        print("Accepted and created connectionSocket. address is: ", addr)
        # Temporary buffer
        tmpBuff = ""
        data = ""

        while len(data) != 40:
            # Receive whatever the newly connected client has to send
            tmpBuff = connectionSocket.recv(40)

            # The other side unexpectedly closed its socket
            if not tmpBuff:
                break

            # Save the data
            data += tmpBuff

    connectionSocket.close()

    print(data)



    quit()



# -------- PROVIDED CODE ------------------
# The port on which to listen
# serverPort = 12000

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))

# Start listening for incoming connections
serverSocket.listen(1)

print("The server is ready to receive...")

# Forever accept incoming connections
while 1:
    # Accept a connection; get client's socket
    connectionSocket, addr = serverSocket.accept()

    # Temporary buffer
    tmpBuff = ""

    while len(data) != 40:
        # Receive whatever the newly connected client has to send
        tmpBuff = connectionSocket.recv(40)

        # The other side unexpectedly closed its socket
        if not tmpBuff:
            break

        # Save the data
        data += tmpBuff

    print(data)

    # Close the socket
    connectionSocket.close()

