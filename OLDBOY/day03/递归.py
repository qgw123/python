
def calc(n):
    print(n)
    if int(n/2) > 0 :
        return calc(n/2)
    print('-->',n)

calc(10)

'''
递归最大层数为999层
递归必须有一个明确的结束条件
每次进入更深一层递归时，问题规模相比上次递归都应有所减少
递归效率低
'''