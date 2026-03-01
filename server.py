import socket
import sys
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

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
    elif r == "n":
            while True:
                conn.send("n".encode())
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"Type something that you want to send to client(q for quit)-",end="")
                a = input(Fore.BLUE+Style.BRIGHT)
                if a == "q":
                    conn.send("q".encode())
                    conn.close()
                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"connection closed!")
                    sys.exit(0)
                else:
                    conn.send(a.encode())
while True:
    conn.send("y".encode())
    a1 = conn.recv(1024).decode()
    if a1 == "q":
        conn.close()
        print(Fore.LIGHTRED_EX+Style.BRIGHT+"connection closed!")
        sys.exit(0)
    else:
        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+a1)