import socket

client =socket.socket()

client.connect(("localhost",9999))

while True:
    a =(client.recv(1024).decode())
    if a != "q":
        print(a)
    else:
        client.close()