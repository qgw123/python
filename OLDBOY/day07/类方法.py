__author__ = 'qgw'

'''
类方法
    只能访问类变量，不能访问实例变量
'''

class Dog(object):
    n = 333
    name = '类变量'

    def __init__(self,name):
        self.name = name

    @classmethod        #类方法
    def eat(self):
        print('%s is eatting %s' % (self.n, 'dd'))
        print('%s is eatting %s' % (self.name, 'dd'))

    def talk(self):
        print('%s is talking ' % self.name)

d = Dog('alex')
d.eat()
