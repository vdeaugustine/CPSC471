import socket


def send_data(sock, data):

    data_size = str(len(data))
    while len(data_size) < 10:
        data_size = "0" + data_size

    data = data_size + data
    data_sent = 0

    while data_sent != len(data):
        sendingThis = data[data_sent:]
        data_sent += sock.send(sendingThis)


