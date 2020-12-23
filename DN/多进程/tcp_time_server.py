__author__ = '秋轩'

import socket
import time

class TcpTimeServer():
    def __init__(self ,host='',port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self,cli_socket):
        while True:
            data = cli_socket.recv(1024)
            if data.strip() == b'quit':
                break
            data = data.decode()
            data = '[%s] %s' % (time.strftime('%H:%M:%S'), data)
            cli_socket.send(data.encode())

        cli_socket.close()

    def run(self):
        while True:
            try:
                cli_socket, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            self.chat(cli_socket)
        self.serv.close()

if __name__ == '__main__':
    tcpserv = TcpTimeServer()
    tcpserv.run()