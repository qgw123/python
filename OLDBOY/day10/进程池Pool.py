__author__ = 'qgw'

'''
进程池中有两个方法：
                apply
                apply_async
'''

from multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(2)
    print('in process ',os.getpid() )
    return i + 100

def Bar(arg):
    print('--> exec done:' ,arg ,os.getpid())


if __name__ == '__main__':
    #freeze_support()
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #并行   callback回调
        # pool.apply(func=Foo, args=(i,))   #串行
    print("主进程：", os.getpid())
    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
