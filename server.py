import socket

server = socket.socket()

server.bind(("localhost",9999))

server.listen()

conn,addr = server.accept()
print(f"connected to{addr}")

x = ""

while True:
    a = input("Type something that you want to send to client(q for quit)-")
    if a == "q":
        conn.send("q".encode())
        conn.close()
        print("connection closed!")
    else:
        conn.send(a.encode())