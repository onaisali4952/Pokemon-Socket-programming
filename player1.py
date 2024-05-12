import socket

socket1 = socket.socket()
socket1.connect(('localhost', 9999))

while 1:
    server_message = socket1.recv(1024).decode()
    print(server_message)

    client_message = input()
    socket1.send(bytes(client_message, 'UTF-8'))
    if(client_message.lower() == "exit"):
        break

socket1.close() 