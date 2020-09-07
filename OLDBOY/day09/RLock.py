__author__ = 'qgw'
import threading


def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('-----between run1 and run2-----')
    res2 =run2()
    lock.release()
    print(res,res2)

num = 0
num2 = 0
lock = threading.RLock()

for i in range(2):
    t = threading.Thread(target=run3)#args=(('t-%s'% i,)))
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num,num2)
