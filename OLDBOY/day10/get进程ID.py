__author__ = 'qgw'

import multiprocessing
import os
# from multiprocessing import Process


def info(title):
    print(title)
    print('module name: ',__name__)
    print('parent process: ',os.getppid())
    print('process id:', os.getpid())
    print('\n\n')

def f(name):
    info('\033[31;1mfunctione f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = multiprocessing.Process(target=f,args=('qgw',))
    p.start()
    p.join()