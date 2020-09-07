__author__ = 'qgw'
import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)
    print("task done", n,threading.current_thread())

start_time = time.time()
t_objs = [] #存线程实例

for i in range(5):
    t = threading.Thread(target=run, args=('t-%s'% i ,))
    # t2 = threading.Thread(target=run, args=('t2',))

    t.start()
    # t2.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs:   #循环线程实例列表，等待所有线程执行完毕
#     t.join()

# print(t_objs)
print("---all threads has finished...---",threading.current_thread(),
      threading.active_count())
print("cost:",time.time() - start_time)