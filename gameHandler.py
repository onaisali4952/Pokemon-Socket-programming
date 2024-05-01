import socket

socket1 = socket.socket()
print('Socket Created')
socket1.bind(('localhost', 9999))
socket1.listen(5)
print('Waiting for socket connection (run client file on separate terminal to get started)')

while 1:
    c, addr = socket1.accept()

    while 1:
        
        message = input("Enter message: ")
        c.send(bytes(message, 'UTF-8'))
        if(message.lower() == "exit"):
            break

        response = c.recv(1024).decode()
        print(response)
        
    c.close()
    break