__author__ = 'qgw'

'''
    obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象,
因为在Python中一切事物都是对象。

    如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，
那么Foo类对象应该也是通过执行某个类的 构造方法 创建。

类 是由 type 类实例化产生
'''
# class Foo(object):
#     def __init__(self,name):
#         self.name = name

def func(self):
    print('hello %s, %s' % (self.name,self.age))

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'func': func,'__init__':__init__})

# f = Foo('qgw')
f = Foo('123', 22)
f.func()
# print(type(f))
print(type(Foo))
