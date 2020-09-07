__author__ = 'qgw'
'''
反射
    hasattr(obj,name_str) 判断一个对象obj里是否有对应的name_str字符串的方法
    getattr(obj,name_str) 根据字符串去获取obj对象里的对应方法的内存地址
    setattr(obj,'y',z) is equivalent(相当于) to "x.y = v"
    delattr
'''

class Cat(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s is eatting %s' % (self.name,food))

def bulk(self):
    print("%s id yelling......" % self.name)

c = Cat('alex')
choice = input('>>: ').strip()

# print(hasattr(c,choice))
# getattr(c,choice)()

if hasattr(c,choice):
    func = getattr(c,choice)
    func('food')
    # attr = getattr(c,choice)
    # setattr(c,choice,'qgw')
else:
    setattr(c,choice,bulk)
    c.talk(c)
    # setattr(c,choice,22)
    # print(getattr(c,choice))
    # setattr(c,choice,None)
    # print(getattr(c,choice))

# print(c.name)