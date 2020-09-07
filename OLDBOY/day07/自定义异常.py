__author__ = 'qgw'


class QGWException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
        # return "buyiyang"


try:
    raise QGWException('我的异常')

except QGWException as  e:
        print(e)