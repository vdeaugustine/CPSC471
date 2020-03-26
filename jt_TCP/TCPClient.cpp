#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#define _WINSOCK_DEPRECATED_NO_WARNINGS	// Needed to ignore warnings about outdated Winsock functions

#include<iostream>
#include<string>
#include<stdio.h>
#include<Windows.h>
#include<stdlib.h> // Needed for exit() and atoi()
#pragma comment(lib, "Ws2_32.lib")	// Needed to link build environment to Winsock Library
// The following two header files are required in order
// to work with Winsock functions and definitions.
#include<WinSock2.h>
#include<WS2tcpip.h>
#include <fcntl.h>        /* For O_RDONLY */

#define MAX_BUFFER_SIZE 250
using namespace std;

int main(int argc, char** argv)
{
	// Assuming that no arguments are declared, set these
	// variables to their default values.
	int sockConnect = -1;
	int portNum = -1;
	int bytesSent = 0;
	char userMessage[MAX_BUFFER_SIZE];

	sockaddr_in serverAddress;
	socklen_t serverLen = sizeof(serverAddress);

	// Check if the number of arguments are valid.
	if (argc < 3)
	{
		fprintf(stderr, "Requires the following: %s <SERVER IP> <SERVER PORT #>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	// Get the port number.
	portNum = atoi(argv[2]);

	// Check if the port number is within the valid range.
	if (portNum < 0 || portNum > 65535)
	{
		cerr << "Invalid port number.\n";
		exit(EXIT_FAILURE);
	}

	// Try to create a new socket if possible.
	if (sockConnect = (socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		cerr << "Cannot create new socket.\n";
		exit(EXIT_FAILURE);
	}

	// Configure the family and port number of the server.
	serverAddress.sin_family = AF_INET;
	serverAddress.sin_port = htons(portNum);

	// Now try to establish the connection if possible.
	if (connect(sockConnect, (sockaddr*)&serverAddress, sizeof(sockaddr)) < 0)
	{
		cerr << "Unable to establish a connection.\n";
		exit(EXIT_FAILURE);
	}

	// Tell the user to enter the message.
	cout << "Enter the message: ";
	fgets(userMessage, MAX_BUFFER_SIZE - 1, stdin);

	// Send the bytes of data from the user input over to the server.


	// Close the socket afterwards.
	closesocket(sockConnect);

	Sleep(2000);
	return 0;
}