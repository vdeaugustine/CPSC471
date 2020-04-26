from socket import *
import os path
from os import path
from ftplib import FTP

serverPort = 12000

while True:

    userInput = raw_input("ftp>")


    if userInput.startswith('ls'):
        print("Now printing out the directory")
        print("Here are the files: \nfile1\nfile2\nfile3")
        

    elif userInput.lower().startswith('get '):
        print("User Entered 'get' command")

        pass
        userFileChoice = input()
        # Check if the file exists in the server
        if(userFileChoice == "file1.txt"):
            print ("Does the file exist:" + str(path.exists(userFileChoice)))
        elif(userFileChoice == "file2.txt"):
            print ("Does the file exist:" + str(path.exists(userFileChoice)))        
        elif(userFileChoice == "file3.txt"):
            print ("Does the file exist:" + str(path.exists(userFileChoice)))  
        # If the file does not exist in the server:
            # print("Cannot retrieve the file from the server."
            # break        
        else:
            print("Cannot retrieve the file from the server.")
       
        # else if the file does exist in the server:
            # download the file from the server
            # print("File successfully downloaded.")
            chosenFile = userFileChoice
            localfile = open(chosenFile, 'wb')
            ftp.retrbinary('RETR ' + chosenFile, localfile.write, 1024)

            ftp.quit()
            localfile.close()
    elif userInput.lower().startswith('put '):
        print("User Entered 'put' command")

        pass
        # Check if the file exists in the server

        # If the file already exists in the server:
            # print("Another file already exists in the server."
            # break

        # else if the file does not already exists in the server:
            # Upload the file to the server
            # print("File successfully uploaded")

    elif userInput.lower().startswith('quit'):
        print("User Entered 'quit' command")
        print("Disconnecting from server.")
        # break out of while loop
        break

    else:
        print("Invalid command.")


