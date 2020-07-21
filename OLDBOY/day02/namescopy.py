import  copy

names = ['zhangyang', 'guyun', 'xiangpeng', ['qgw', 'asd'], 'xuliangchen']

# names2 = names.copy()         ##深度copy
names2 = copy.copy(names)       ##浅copy
print(names)
print(names2)
names[2] = '祥鹏'
names[3][0] = 'QGW'
names2[3][1] = 'ASD'

print(names)
print(names2)