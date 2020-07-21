#获取列表的下标和值
alist = ['10','20','30']

for i in enumerate(alist):
    print(i)

for it in enumerate(alist):
    print('%s: %s' % (it[0],it[1]))

for io,num in enumerate(alist):
    print('%s:%s' % (io,num))