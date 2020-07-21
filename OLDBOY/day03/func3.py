'''
参数组
'''
'''
def test(*args):
    print(args)

test(1,2,3,4,5)
test(*[1,2,3,4,5])       #*args=*[1,2,3,4,5]  args=tuple([1,2,3,4,5]) 元组
'''

 #*args:接受N个位置参数，转换成元组形式
def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,7,8,9)

#**kwargs：接受N个关键字参数，转换成字典的方式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])

test2(name='qgw', age=23)
test2(**{'name':'qgw','age':23})

def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('alex',age=18,sex='m')
"""
def test4(name, age=18, **kwargs):
    print(name)
    print(age)
    print(kwargs)

test4('qwe',sex='m',hobby='baoma')
"""

def test4(name, age=18, *args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test4('qgw',23,56 ,sex='boy')