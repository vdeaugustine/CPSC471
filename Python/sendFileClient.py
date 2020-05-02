import socket
import os
import sys


def sendFileClient(serverAddress, serverPort, fileName):

    # Open the file
    fileObject = open(fileName, "r")

    # Create TCP socket
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    connectionSocket.connect((serverAddress, serverPort))

    # Number of bytes sent
    numBytesSent = 0


    # The file data
    fileData = None

    while True:

        amount = 65536
        # Read 65536 bytes of data
        fileData = fileObject.read(amount)

        if fileData:

            # Get the size of the data read and convert it to string
            dataSizeString = str(len(fileData))

            # Prepend 0's to the size string
            # until the size is 10 bytes
            while len(dataSizeString) < 10:
                dataSizeString = dataSizeString + "0"

            # Prepend the size of the data to the file data
            fileData = dataSizeString + fileData

            # Number of bytes sent
            numBytesSent = 0

            # Send the data
            while len(fileData) > numBytesSent:
                numBytesSent += connectionSocket.send(fileData[numBytesSent:])

            # The file has been read. We are done
            else:
                break

    print("Sent ", numBytesSent, " bytes.")

    # Close the socket and the file
    connectionSocket.close()
    fileObject.close()
