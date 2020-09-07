__author__ = 'qgw'
import threading
import time

class Mythread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(Mythread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print('task',self.n)
        time.sleep(2)
        print('task done',self.n)

t1 = Mythread('t1',2)
t2 = Mythread('t2',4)

t1.start()
# t1.join()   #=join()=wait()
t2.start()

t1.join()
t2.join()

print("main thread....")