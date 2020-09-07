__author__ = 'qgw'
#客户端
import socket

client = socket.socket() #声明socket
client.connect(('127.0.0.1',6969))

# client.send('不一样的烟花'.encode('utf-8'))
while True:
    info = input('>>: ').strip()
    if len(info) == 0:
        continue
    client.send(info.encode('utf-8'))
    data = client.recv(102400)
    print('recv:',data.decode())

client.close()