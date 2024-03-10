# Importing the socket module to use its functionalities
from socket import *

try:
    # Creating a socket using AF_INET for IPv4 and SOCK_STREAM for TCP
    s = socket(AF_INET, SOCK_STREAM)
    print('Client socket is successfully created')

    # Setting the server's host and port
    host = '127.0.0.1'
    port = 24921

    # Connecting to the server
    s.connect((host, port))
    print(f'Connected to server at {host}:{port}')

    # Main loop for sending/receiving messages
    while True:
        # Taking user input for the message to be sent to the server
        inp = input('Client send: ')

        # Encoding the input message and adding a newline indicator
        s.send(inp.encode() + b'\n')

        # Receiving the response from the server
        receive = b''
        while True:
            part = s.recv(2048)
            if not part:
                break
            receive += part
            if b'\n' in part:
                break

        # Printing the received message from the server
        print(f'Client received: {receive.decode()}')

    # Closing the socket when the loop exits
    s.close()

except Exception as e:
    print(f'Socket error: {e}')
