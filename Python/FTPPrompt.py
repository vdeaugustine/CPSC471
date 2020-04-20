userInput = input("ftp>")

if userInput.startswith('ls'):
    print("Now printing out the directory")

elif userInput.lower().startswith('get '):
    pass
    # Check if the file exists in the server

    # If the file does not exist in the server:
        # print("Cannot retrieve the file from the server."
        # break
    # else if the file does exist in the server:
        # download the file from the server
        # print("File successfully downloaded."

elif userInput.lower().startswith('put '):
    pass
    # Check if the file exists in the server

    # If the file already exists in the server:
        # print("Another file already exists in the server."
        # break

    # else if the file does not already exists in the server:
        # Upload the file to the server
        # print("File successfully uploaded")

elif userInput.lower().startswith('quit'):
    print("Disconnecting from server.")
    # break out of while loop

else:
    print("Invalid command.")

