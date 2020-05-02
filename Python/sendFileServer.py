import socket

# This function can receive a file and print its contents


def sendFileServer(listenPort):

    # Create welcome socket
    welcomeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    welcomeSocket.bind('', listenPort)

    # Start listening on the socket
    welcomeSocket.listen(1)

    def receiveAll(sock, numberOfBytes):
        # The buffer
        receiveBuffer = ""


        # Temporary buffer
        tempBuffer = ""

        # Keep receiving till all of it is received
        while len(receiveBuffer) < numberOfBytes:

            # Attempt to receive bytes
            tempBuffer = sock.recv(numberOfBytes)

            if not tempBuffer:
                break

            # Add the received bytes to the buffer
            receiveBuffer += tempBuffer

        return receiveBuffer


    while True:
        print("Waiting for connections...")

        # Accept connections
        clientSocket, address = welcomeSocket.accept()

        print("Accepted connection from client: ", address, "\n")

        # The buffer to all data received from the client
        fileData = ""

        # The temporary buffer to store the receive data
        receiveBuffer = ""

        # The size of the incoming file
        fileSize = 0

        # The buffer containing the file size
        fileSizeBuffer = ""

        # Receive the first 10 bytes indicating the size of the file
        fileSizeBuffer = receiveAll(clientSocket, 10)

        # Get the file size
        fileSize = int(fileSizeBuffer)

        print("The file data is: ")
        print(fileData)

    clientSocket.close()