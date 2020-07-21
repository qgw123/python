__author__ = 'qgw'

class pig:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print('%s: hehehehe' % self.name )


p1 = pig('q')
p2 = pig('a')

p1.bulk()
p2.bulk()