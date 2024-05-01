import socket

socket2 = socket.socket()
socket2.connect(('localhost', 9999))

while 1:
    response = socket2.recv(1024).decode()
    print(response)

    message = input("Enter message: ")
    socket2.send(bytes(message, 'UTF-8'))
    if(message.lower() == "exit"):
        break

socket2.close()