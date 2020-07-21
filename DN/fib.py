fib = [0,1]

num = int(input('数列长度：'))
for i in range(num - 2 ):
    fib.append(fib[-1] + fib[-2])   #每次将列表中最后两项之加追加到列表中

print(fib)

# 数列输入：11
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
