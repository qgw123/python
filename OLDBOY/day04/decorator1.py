import time


# def bar():
#     time.sleep(0.5)
#     print('in the bar')
#
# def test1(func):
#     start_time = time.time()
#     func()      #run bar
#     stop_time = time.time()
#     print('the func run time is %s ' % (stop_time-start_time))
#
# test1(bar)

# 返回值中返回参数名
def bar():
    time.sleep(3)
    print('in the bar')


def test2(func):
    print(func)
    return func


bar = test2(bar)
bar()  # run bar

# print(test2(bar))       #得到的是内存地址
# print(test2(bar()))     #得到函数的返回值
# <function bar at 0x0000000001D12F28>  内存地址
# <function bar at 0x0000000001D12F28>
