import socket
import sys
client =socket.socket()

client.connect(("localhost",9999))
i =1 
while i != 0:
    a =(client.recv(1024).decode())
    if a != "q":
        print(a)
    else:
        client.close()
        print("connetion closed!")
        i = 0