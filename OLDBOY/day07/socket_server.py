__author__ = 'qgw'

#服务端
import socket
server = socket.socket()
server.bind(('127.0.0.1', 6969))   #绑定要监听端口
server.listen() #监听

print('begin')
while True:
    conn,addr = server.accept() #等待
    #conn就是客户端连过来而在服务器为其生成的一个连接实例
    # print(conn,addr)
    print('beginning')

    while True:
        data = conn.recv(10240)     #默认是阻塞的
        print("recv:", data.decode())
        if not data:
            print('client has lost...')
            break
        conn.send(data.upper())

server.close()