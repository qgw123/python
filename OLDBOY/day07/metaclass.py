__author__ = 'qgw'

class  MyType(type):
    def __init__(self, *args, **kwargs):
        print('Mytype __init__',args, kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ", obj, *args, **kwargs)
        print(self)
        self.__init__(obj, *args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')

# class Foo(object,metaclass=MyType):
class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo --init--")

    def __new__(cls, *args, **kwargs):
        print('Foo --new--')
        return object.__new__(cls)


#第一阶段：解释器从上到下执行代码创建Foo类
#第二阶段：通过Foo类创建f对象
f = Foo('qgw')
print(f.name)
print("fname",f.name)

# 类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__