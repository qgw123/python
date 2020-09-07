__author__ = 'qgw'
'''
https://www.cnblogs.com/alex3714/articles/5830365.html
创建一个socketserver 至少分以下几步:
    首先，必须通过将BaseRequestHandlerclass子类化并重写其handler（）方法来创建请求处理程序类；
此方法将处理传入的请求.
    其次，必须实例化一个服务器类，将服务器地址和请求处理程序类传递给它。
    然后调用服务器对象的handle_request（）或serve_forever（）方法来处理一个或多个请求。
    最后，调用server_close（）关闭套接字。
'''

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    '''

    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # if not self.data:
                #     print(self.client_address,"客户端断开")
                #     break

                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print('ERR: ',e)
                break


if __name__ == "__main__":
    HOST, PORT = "localhost", 9998

    # Create the server, binding to localhost on port 9999

    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)#多并发，线程
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)  #多进程

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()