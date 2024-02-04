import socket
import datetime

time = datetime.datetime.now()
x=0
x = x+1

s = socket.socket()
port = 56789
s.connect(('127.0.0.1', port))
response = s.recv(1024)

if response == b'yes':
    print("Okay! Executing..")
    file = open(f"Responsefromclient{x}.txt", "r+")
    file.write("Connected to server. S.E.N.S.E.I ")
    

s.close()