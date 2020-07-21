def fib(max):  # 10
    n, a, b = 0, 0, 1
    while n < max:  # n<10
        # print(b)
        yield b     # yield  生成器标识
        a, b = b, a + b
        #相当于t = (a, a+b)
        # a = t[0]
        # b = t[1]
        n = n + 1
    return '---done---'
#
#
f = fib(10)
print(f)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# print("---------dddd")
# print(f.__next__())
# print("======")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

print("====start loop======")
# for i in f:
#    print(i)