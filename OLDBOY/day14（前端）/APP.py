__author__ = 'qgw'

import tornado.ioloop
import tornado.web

class  MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        user = self.get_argument('username')
        # email = self.get_argument('email')
        passwd = self.get_argument('password')

        if user == 'qgw' and passwd == '123456':
            self.write("OK")
        else:
            self.write("很遗憾")

    def post(self, *args, **kwargs):
        user = self.get_argument('username', None)
        # email = self.get_argument('email', None)
        passwd = self.get_argument('password', None)
        print(user,passwd)
        self.write('POST')

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()