
from socket import *
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

        instr = rAD.receive(connectionSocket)

        tmpBuff = ""
        data = ""

        while len(data) != 40:
            tmpBuff = connectionSocket.recv(40)
            if not tmpBuff:
                break
            data += tmpBuff

    connectionSocket.close()

    print(data)



    quit()

