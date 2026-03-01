import socket
import sys
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
client =socket.socket()

client.connect(("localhost",9999))
i =1 
while i != 0:
    a = client.recv(1024).decode()
    if a == "y":
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"Type something that you want to send to client(q for quit)-",end="")
        x = input(Fore.BLUE+Style.BRIGHT)
        if x == "q":
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"connection closed")
            client.send("q".encode())
            client.close()
            i = 0
        else:
            client.send(x.encode())
    elif a == "n":
        a1 = client.recv(1024).decode()
        if a1 != "q":
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+a1)
        else:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"connection closed!")
            client.close()
            sys.exit(0)
sys.exit(0)