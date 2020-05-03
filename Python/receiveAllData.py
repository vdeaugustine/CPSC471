import socket


def receive(the_socket):
    print("Calling recv() in server")

    data = ""
    size_of_file = 0
    file_size_buffer = ""
    file_size_buffer = receive_all_data(the_socket, 10)
    print("file_size_buff before int cast: ", file_size_buffer)
    size_of_file = int(file_size_buffer)

    data = receive_all_data(the_socket, size_of_file)

    return data


def receive_all_data(the_socket, number_of_bytes):
    r_buffer = ""
    temporary = ""

    while len(r_buffer) < number_of_bytes:
        temporary = the_socket.recv(number_of_bytes)

        if not temporary:
            break

        r_buffer += temporary

    return r_buffer
