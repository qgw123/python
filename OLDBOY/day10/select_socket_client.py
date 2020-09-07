__author__ = 'qgw'
import sys
import socket
HOST = 'localhost'  # The remote host
PORT = 8989  # The same port as used by the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    client.sendall(msg)
    data = client.recv(1024)
    # print(data)

    print('Received', repr(data.decode()))
client.close()
