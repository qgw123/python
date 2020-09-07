__author__ = 'qgw'
import select
import socket
import queue
import sys

server = socket.socket()
server.bind(('localhost', 8585))
server.listen(5)

server.setblocking(False)       #设置不阻塞
msg_dic = {}
inputs = [server,]
outputs = []

while True:
    readable, writeable, exceptional = select.select(inputs, outputs , inputs)
    print(readable, writeable, exceptional)
    for i in readable:
        if i is server:
            conn,addr = server.accept()
            print('来了个新连接：', addr)
            # print('recv: ',conn.recv(1024))
            inputs.append(conn) #是因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，
            #所以要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn。
            msg_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据

        else:   #conn2
            data = i.recv(1024)
            print("收到数据：", data.decode())
            # i.send(data)
            # print('send done ......')
            msg_dic[i].put(data)

            outputs.append(i)  # 放入返回的连接队列里

    for w in writeable:  # 要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)  # 返回给客户端源数据

        outputs.remove(w)  # 确保下次循环的时候writeable,不返回这个已经处理完的连接了

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)

        del msg_dic[e]