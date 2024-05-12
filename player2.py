import socket

socket2 = socket.socket()
socket2.connect(('localhost', 9999))

while 1:
    server_message = socket2.recv(1024).decode()
    print(server_message)

    client_message = input()
    socket2.send(bytes(client_message, 'UTF-8'))
    if(client_message.lower() == "exit"):
        break

socket2.close() 