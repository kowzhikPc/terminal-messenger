import socket
import sys
server = socket.socket()

server.bind(("localhost",9999))

server.listen()

conn,addr = server.accept()
print(f"connected to{addr}")
i = 0

while i == 0:
    r = input(" Receive mode(y/n) - ")
    if r == "y":
        i+=1
    else: 
        conn.send("n".encode())
        a = input("Type something that you want to send to client(q for quit)-")
        if a == "q":
            conn.send("q".encode())
            conn.close()
            print("connection closed!")
            i +=1
        else:
            conn.send(a.encode())
while True:
    conn.send("y".encode())
    a1 = conn.recv(1024).decode()
    if a1 == "q":
        conn.close()
        print("connection closed!")
        sys.exit(0)
    else:
        print(a1)