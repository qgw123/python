__author__ = 'qgw'

'''
class queue.Queue(maxsize=0) #先入先出
class queue.LifoQueue(maxsize=0) #last in fisrt out(后进先出)
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级队列

作用：
    解耦，使程序之间实现松耦合
    提高处理效率
'''
import queue,threading

q = queue.LifoQueue()
q1 = queue.PriorityQueue()

#queue.LifoQueue
q.put('d1') #存数据
q.put('d2')
q.put('d3')
q.qsize()   #多少个数据
print(q.qsize())

#PriorityQueue
q1.put((5,'qq'))
q1.put((2,'q2'))
q1.put((4,'q3'))

# q.get() #读数据
print(q.get())
print(q.get())
print(q.get())

# q.get(block=False)
print(q1.get())
print(q1.get())
print(q1.get())