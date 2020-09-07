__author__ = 'qgw'
import threading,time

def run(n):
    global num  #在每个线程中都获取这个全局变量
    # print('--get num:', num)
    time.sleep(1)
    lock.acquire()  #修改数据前加锁
    num += 1
    lock.release()  #修改后释放

num = 0
t_obj = []
lock = threading.Lock() #生成全局锁

for i in range(10):
    t = threading.Thread(target=run, args=(('t-%s' % i,)))
    t.start()
    t_obj.append(t)

for t in t_obj: #等待所有线程执行完毕
    t.join()

print('---all threads has finished...---', threading.current_thread(),
      threading.active_count())
print('number: ',num)