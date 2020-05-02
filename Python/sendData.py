import socket

def send_data (sockPassed, data_passed):

    size_of_data = str(len(data_passed))

    # Header set to 10 bytes
    while len(size_of_data) < 10:
        size_of_data = "0" + size_of_data

    data_passed = size_of_data + data_passed
    sentData = 0

    # Make sure all data is sent
    while sentData != len(data_passed):
        sentData += sockPassed.send(data_passed[sentData:])

