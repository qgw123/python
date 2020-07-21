''''''
'''
面向对象：--> 类 --> class
面向过程：--> 过程 --> def
函数式编程：--> 函数 --> def
'''

# 函数
def func1():
    """testing1"""
    print('in the func1')
    return 0

# 过程
def func2():
    '''testing2'''
    print('in the func2')

x = func1()     #x的值是函数的返回值
y = func2()

print('from func1 return is %s' % x)
print('from func2 return is %s' % y)
'''
为什么要有返回值
想要知道这个函数的执行结果。后续程序需要对这个返回值进行操作
'''