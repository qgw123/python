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

    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)

    def __str__(self):
        return  "<obj:%s>" % self.name

d = Dog('alex')
print(Dog.__doc__)      #__doc__ 读取描述信息
d(12346,name='qgw')
Dog('zhang')()
print(Dog.__dict__)       #打印类里的所有属性，不包括实例熟悉
print(d.__dict__)          #打印所有实力属性，不包括类属性
print(d)