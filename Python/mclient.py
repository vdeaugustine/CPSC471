# Client code
from socket import *
import cmds
import ephemeral
import sys
import sendFileClient as SFC
import sendData as sd




if __name__ == "__main__":

    numOfArguments = len(sys.argv)
    if numOfArguments == 3:
        serverName = sys.argv[1]
        serverPort = sys.argv[2]
        # Check that server port is a digit
        if serverPort.isdigit():
            print("Server port is in right format")
            serverPort = int(serverPort)
        else:
            print("Server port needs to be a digit")
        # print(serverName, serverPort)

    # try:
    # Create a socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    print("trying to connect to server")
    clientSocket.connect((serverName, serverPort))
    quit()

    if userInput.startswith('ls'):
        print("Now printing out the directory")
        # Tell the server we want to perform ls
        sd.send_data(clientSocket, 'ls')



    # except socket.error as errorFromSocket:
    #     print("Error occurred with FTP: ", errorFromSocket)



        quit()
    else:
        print("Incorrect invocation. Client should be invoked as: client.py <server machine> <server port>")
        quit()

    userInput = input("ftp> ")






    # # Print arguments
    # for a in sys.argv:
    #     print(a)




# -------- CODE PROVIDED BY INSTRUCTIONS --------------------
#
# # Name and port number of the server to which want to connect
# # serverName = "ecs.fullerton.edu"
# serverPort = 12000
#
# # Create a socket
# clientSocket = socket(AF_INET, SOCK_STREAM)
#
# # Connect to the server
# clientSocket.connect((serverName, serverPort))
#
# # A string we want to send to the server
#
# data = "Hello world! This is a very long string."
#
# bytesSent = 0
#
# while bytesSent != len(data):
#     # Send that string
#     bytesSent += clientSocket.send(data[bytesSent:])
#
# # Close the socket
# clientSocket.close()

# ---------- END OF CODE PROVIDED BY INSTRUCTIONS --------------

