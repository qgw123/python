#斐波那契数列：除第一个和第二个数之外，前两个数字相加得到最后一个数字的数列

def fib_fun(num):
    fib = [0,1]

    # num = int(input('数列长度：'))
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

# num = fib_fun()
# X = [i * 3 for i in num ]
# print(X)
# qlist = [8,10,12]
# for w in qlist:
#     result = fib_fun(w)
#     print(result)

# l = int(input('数列长度： '))
print(fib_fun(10))