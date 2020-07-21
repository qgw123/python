__author__ = 'qgw'
#装饰器
import time

def timer(func):    #timer= timer(test1)    func=test1

    def code(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)         #run test1()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return code

@timer      #相当于test1 = timer(test1)
def test1():
    time.sleep(2)
    print('in  the test1')

@timer
def test2(name):
    time.sleep(4)
    print('in the test2',name)

#test1()  ---> test1(code)
test1()
test2('qgw')
