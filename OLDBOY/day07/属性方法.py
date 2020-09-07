__author__ = 'qgw'

'''
属性方法
    把一个方法变成一个静态属性
'''

class Dog(object):
    '''这是一个变换的变量'''
    def __init__(self,name):
        self.name = name
        self.food = None

    @property
    def eat(self):
        print('%s is eatting %s' % (self.name, self.food))

    @eat.setter         #建立
    def eat(self,food):
        print("set to food:", food)
        self.food = food

    @eat.deleter        #删除
    def eat(self):
        del self.food
        print("删完了")

    def talk(self):
        print('%s is talking ' % self.name)

d = Dog('alex')
# d.eat()     #报错
d.eat
d.eat = 'baozi'
del d.eat     #删除后后续不可以调用
# d.eat
print(Dog.__doc__)      #__doc__ 读取描述信息