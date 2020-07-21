import time

def foo():
    time.sleep(0.1)
    print('in the foo')
    bar()

def bar():
    print('in the bar')
foo()

cale = lambda X:X * 3       #匿名函数赋值一个变量
print(cale(4))