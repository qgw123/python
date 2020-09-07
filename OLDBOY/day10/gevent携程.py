__author__ = 'qgw'
'''
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 
它是以C扩展模块形式接入Python的轻量级协程。 
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
'''
import gevent
import time

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch  to foo again')

def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context swith back to bar')

def func():
    print('Running in func')
    gevent.sleep(0)
    print('Running fun again')

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
        gevent.spawn(func)
        ])