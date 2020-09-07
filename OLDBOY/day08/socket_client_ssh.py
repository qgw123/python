__author__ = 'qgw'

import socket
client = socket.socket()
client.connect(('localhost',8989))

while True:
    cmd = input(">>: ").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print("命令结果大小：", cmd_res_size)
    client.send("准备好接受了， loser可以发了".encode('utf-8'))
    recevied_size = 0
    recevied_data = b''

    while recevied_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        recevied_size += len(data)
        recevied_data += data
        # print(data.decode())
    else:
        print('cmd is has done......' , recevied_size)
        print(recevied_data.decode())

client.close()

