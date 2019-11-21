from datetime import datetime
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect(('127.0.0.2', 5005))

while True:
    to_send = input(f'{datetime.now()} - Send: ').encode() # omzetten naar bytes
    if to_send == b'stop':
        s.close()
        break
    s.send(to_send)
    data = s.recv(2048)
    print(f"{datetime.now()} - recvd: {data}")

#s.close()
