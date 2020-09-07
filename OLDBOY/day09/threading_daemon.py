__author__ = 'qgw'
import threading, time

def run(n):
    print('task: ',n)
    time.sleep(2)
    print('task done', n)

start_time = time.time()
t_job = []

for i in range(6):
    t = threading.Thread(target=run, args=('t-%s' % i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()
    t_job.append(t)

# time.sleep(2)
print('---all threads has finished...---',threading.current_thread()#线程类型
    ,threading.active_count() #线程个数
      )
# print('cost: ', time.time() - start_time)