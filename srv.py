from datetime import datetime
import socket

table = bytes.maketrans(b'ao', b'eu')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.2', 5005))
s.listen(1)

conn, addr = s.accept()
print(f'{datetime.now()} - Listening on address: f{addr}')
rcv_bufsize = 10
print(f'{datetime.now()} - Receive buffer size: {rcv_bufsize}')
while True:
    data = conn.recv(rcv_bufsize)
    if data == b'kill':
        print(f'{datetime.now()} - kill received, closing connection')
        break
    elif data.startswith(b'sb'):
        rcv_bufsize = int(data[2:])
        print(f'{datetime.now()} - Setting receive buffer to {rcv_bufsize}')
        continue
    if not data:
        print(f'{datetime.now()} - no data received, closing connection')
        break
    print(f'{datetime.now()} - recvd: {data}')
    print(f'{datetime.now()} - sending: {data.translate(table)}')
    conn.send(data.translate(table))
conn.close()
