# *************************************************************
# This program illustrates how to generate an emphemeral port
# *************************************************************
import socket


def do_ephemeral():

    # Create a socket
    welcomeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to port 0
    welcomeSocket.bind(('',0))

    print("I chose ephemeral port: ", welcomeSocket.getsockname()[1])

    return welcomeSocket




