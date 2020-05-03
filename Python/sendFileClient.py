import socket
import os
import sys


def sendFileClient(serverAddress, serverPort, fileName):

    fileObject = open(fileName, "r")

    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connectionSocket.connect((serverAddress, serverPort))

    numBytesSent = 0

    fileData = None

    while True:

        amount = 65536
        fileData = fileObject.read(amount)

        if fileData:

            dataSizeString = str(len(fileData))

            while len(dataSizeString) < 10:
                dataSizeString = dataSizeString + "0"

            fileData = dataSizeString + fileData

            numBytesSent = 0

            while len(fileData) > numBytesSent:
                numBytesSent += connectionSocket.send(fileData[numBytesSent:])

            else:
                break

    print("Sent ", numBytesSent, " bytes.")

    # Close the socket and the file
    connectionSocket.close()
    fileObject.close()
