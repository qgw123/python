__author__ = 'qgw'

'''
互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 .
'''


import threading
import time

def run(n):
    semaphore.acquire()
    print("run the thread: %s\n" %n)
    time.sleep(1)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)

    for i in range(10):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print('----all threads done----')