__author__ = 'qgw'
import socket
import os
import time

server = socket.socket()
server.bind(('localhost',8989))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:" , addr)

    while True:
        print("开始等待指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：",data)
        res = os.popen(data.decode()).read()    #接受字符串，执行结果也是字符串
        print('before send', len(res))
        if len(res) == 0:
            res = "cmd has no output......"


        conn.send(str(len(res.encode())).encode('utf-8'))
        #time.sleep(0.5)
        client_ack = conn.recv(1024)  #wait client to confire
        print('ack from client',client_ack)
        conn.send(res.encode('utf-8'))

server.close()