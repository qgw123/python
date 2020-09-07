__author__ = 'qgw'

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(server, mask):
    conn,addr = server.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False) #非阻塞模式
    sel.register(conn, selectors.EVENT_READ, read)  #新连接注册read回调函数

def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

server = socket.socket()
server.bind(('localhost', 8989))
server.listen(100)
server.setblocking(False)
sel.register(server, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)