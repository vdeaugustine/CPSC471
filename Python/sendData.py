import socket


def send_data(sock, data):

    print("Data: ", data, "Type of data: ", type(data))

    data_size = str(len(data))
    # set header to 10 bytes
    while len(data_size) < 10:
        data_size = "0" + data_size

    data = data_size + data
    data_sent = 0

    # ensure all data is sent
    while data_sent != len(data):
        sendingThis = data[data_sent:]
        print("Type of sendingThis: ", type(sendingThis))
        data_sent += sock.send(sendingThis)
    # size_of_data = str(len(data_passed))
    #
    # # Header set to 10 bytes
    # while len(size_of_data) < 10:
    #     size_of_data = "0" + size_of_data
    #
    # data_passed = size_of_data + data_passed
    # sentData = 0
    #
    # # Make sure all data is sent
    # while sentData != len(data_passed):
    #     sentData += sockPassed.send(data_passed[sentData:])

