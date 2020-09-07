__author__ = 'qgw'


import threading,time
import random

event = threading.Event()

def lighter():
    count = 0
    event.set()  # 先设置绿灯
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set()  # 打开绿灯

        time.sleep(1)
        count +=1

def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if event.isSet():  # 绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." % n)

if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=lighter)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()
