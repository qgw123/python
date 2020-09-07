__author__ = 'qgw'
import threading
import queue
import time

q = queue.Queue()
def Producer(name):
    count = 1
    while True:
        q.put("食品%s" , count)
        print('生产了食品%s ' % count)
        count += 1
        time.sleep(0.5)

def Consumer(name):
    # while q.qsize() > 0:
    while True:
        print("%s 取到了[%s]，并且吃了" % (name, q.get()))
        time.sleep(1)

t = threading.Thread(target=Producer,args=('qwe',))
c = threading.Thread(target=Consumer,args=('aaa',))
c1 = threading.Thread(target=Consumer,args=('bbb',))

t.start()
c.start()
c1.start()
