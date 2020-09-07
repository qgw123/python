__author__ = 'qgw'
import socket
import os
import hashlib

server = socket.socket()
server.bind(('localhost',21))
server.listen()

while True:
    conn,addr = server.accept()
    print('new addr: ',addr)

    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break

        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f =open(filename,'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  #send file size
            conn.recv(1024) #wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print('file md5: ',m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print('send done')

server.close