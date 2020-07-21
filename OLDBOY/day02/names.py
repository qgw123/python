names = ['zhangyang', 'guyun', 'xiangpeng', 'xuliangchen']
#             0          1          2             3

print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[1:3])   #切片
# print(names[:3])
# print(names[-1])
# print(names[-3:-1])
print(names[-3:])
names.append('leihaidong')
names.insert(1,'lili')

#delete
# names.remove('lili')#delete
# del names[1]
# names.pop(1)

print(names)
print(names.index('xiangpeng'))     #查看下标是什么
print(names[names.index('xiangpeng')])

##统计相同的数
print(names.count('xiangpeng'))
# names.clear()          #清楚所有
# names.sort()           #排序
# names.reverse()        #倒序
# names.extend()         #合并（）里填另一张列表