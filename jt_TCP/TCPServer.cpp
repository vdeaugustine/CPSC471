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
#define MAX_BUFFER_SIZE 250
using namespace std;

void recvInfo(const int& sock, char* input)
{
	// Assuming that nothing has been received,
	// set the size of input to negative.
	int inputSize = -1;
}

int main(int argc, char** argv)
{
	// Assuming that no arguments are declared, set these
	// variables to their default values.
	int sockListen = -1;
	int portNum = -1;
	int sockConnect = -1;
	char userMessage[MAX_BUFFER_SIZE];
	char buffRecv[MAX_BUFFER_SIZE];
	int bytesRead = 0;

	sockaddr_in serverAddress, clientAddress;
	socklen_t clientLen = sizeof(clientAddress);

	// Check if the number of arguments are valid.
	if (argc < 2)
	{
		fprintf(stderr, "Requires the following: %s <PORT NUM #>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	// Get the port number.
	portNum = atoi(argv[1]);

	// Check if the port number is within the valid range.
	if (portNum < 0 || portNum > 65535)
	{
		cerr << "Invalid port number.\n";
		exit(EXIT_FAILURE);
	}

	fprintf(stderr, "Connected to Port Number %d\n", portNum);

	// Try to create a new socket if possible.
	if ((sockListen = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		cerr << "Cannot create new socket.\n";
		exit(EXIT_FAILURE);
	}

	// Configure the family and port number of the server.
	serverAddress.sin_family = AF_INET;
	serverAddress.sin_port = htons(portNum);

	// Associate the server address with the socket; otherwise, abort.
	if (bind(sockListen, (sockaddr*)&serverAddress, sizeof(serverAddress)) < 0)
	{
		cerr << "Unable to bind the socket with the server address.\n";
		exit(EXIT_FAILURE);
	}

	// Now have the server listen for the client to accept connection.
	if (listen(sockListen, 100) < 0)
	{
		cerr << "Unable to find client via listen.\n";
		exit(EXIT_FAILURE);
	}

	// Force the server to run indefinitely as long as connection is open.
	while (1)
	{
		// Try to accept the client's connection request if possible.
		if ((sockConnect = accept(sockListen, (sockaddr*)&clientAddress, &clientLen)) < 0)
		{
			cerr << "Unable to accept the client's connection.\n";
			exit(EXIT_FAILURE);
		}

		cout << "Connection success.\n";

		// Always set bytes read to 0 for each new incoming data.
		bytesRead = 0;

		// Read in the size of the user input.
		recvInfo(sockConnect, userMessage);

		cout << bytesRead << " bytes have been received.\n";

		// Close the socket afterwards.
		closesocket(sockConnect);
	}

	Sleep(2000);
	return 0;
}
