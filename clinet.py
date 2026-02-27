import socket
import sys
client =socket.socket()

client.connect(("localhost",9999))
i =1 
while i != 0:
    a = client.recv(1024).decode()
    if a == "y":
        x = input("Enter message to send(q for quit) - ")
        if x == "q":
            print("connection closed")
            client.send("q".encode())
            client.close()
            i = 0
        else:
            client.send(x.encode())
    elif a == "n":
        a1 = client.recv(1024).decode()
        print(a1)
sys.exit(0)