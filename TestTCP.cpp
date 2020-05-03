/*------------------------------------------
     CPSC 471 - Computer Communications
     By: John O. Gomez
     Submitted 05/02/2020

     The following code runs a TCP Server
     Client that utilizes the WS2tcpip.h
     Library in order to process a given
     Server IP + Port.
------------------------------------------*/

#include <iostream>
#include <string>
#include <WS2tcpip.h>
#pragma comment(lib, "WS2_32.lib")

using namespace std;

// The following code tests for a sample TCP Firefly

void TestTCP()
{
     string ipAddress = "127.0.0.1";         // IP Address o the server
     int port = 54000;                       // Listening port # on the server

     // Initialize WinSock
     WSAData data;
     WORD ver = MAKEWORD(2, 2);
     int wsResult = WSAStartup(ver, &data);
     if (wsResult != 0)
     {
          cerr << "Can't start winsock, Err #" << wsResult << endl;
          return;
     }

     // Create socket
     SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
     if (sock == INVALID_SOCKET)
     {
          cerr << "Can't create socket, Err #" << WSAGetLastError() << endl;
          WSACleanup();
          return;
     }

     // Fill in a hint structure
     sockaddr_in hint;
     hint.sin_family = A_INET;
     hint.sin_port = htons(port);
     inet_pton(AF_INET, ipAddress.c_str(), &hint.sin_addr);

     // Connect to server
     int connResult = connect(sock, (sockaddr*)&hint, sizeof(hint));
     if(connResult == SOCKET_ERROR)
     {
          cerr << "Can't connect to server, Err #" << WSAGetLastError() << endl;
          closesocket(sock);
          WSACleanup();
          return;
     }

     // Do-while loop to send and receive data
     char buf[4096];
     string userInput;

     do
     {
          // Prompt the user for some text
          cout << "> ";
          getline(cin, userInput);

          if (userInput.size() > 0)     // Make sure the user has typed in something
          {
               // Send the text
               int sendResult = send(sock, userInput.c_str(), userInput.size() + 1, 0);
               if (sendResult != SOCKET_ERROR)
               {
                    // Wait for response
                    ZeroMemory(buf, 4096);
                    int bytesReceived = recv(sock, buf, 4096, 0);
                    if (bytesReceived > 0)
                    {
                         // Echo response to console
                         cout << "SERVER> " << string(buf, 0, bytesReceived) << endl;
                    }
               }
          }
     } while (userInput.size() > 0);

     // Gracefully close down everything
     closesocket(sock);
     WSACleanup();
}
