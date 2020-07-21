'''
#data = open("yesterday",encoding="utf-8").read()
f = open("yesterday2",'a',encoding="utf-8") #文件句柄
#a = append 追加

f.write("\nwhen i was young i listen to the radio\n")
data = f.read()
print('--read',data)

f.close()
'''

# f = open("yesterday2",'r+',encoding="utf-8") #文件句柄 读写
# f = open("yesterday2",'w+',encoding="utf-8") #文件句柄 写读
# f = open("yesterday2",'a+',encoding="utf-8") #文件句柄 追加读写
'''
f = open("yesterday2", 'wb')  # 文件句柄  二进制文件    一般用于网络传输
f.write("hello binary\n".encode())
f.close()
'''
f = open('yesterday', 'r' ,encoding='utf-8')
print(f.encoding)       #打印字符的编码

'''
print(f.encoding)       #打印字符的编码
print(f.tell())         #查看指针的位置
f.seek()                #指针回到什么位置
#print(f.flush())       #将文件写入硬盘    刷新
print(dir(f.buffer) )
'''

'''
#high bige  处理第10行
count = 0
for line in f:
    if count == 9:
        print('----我是分割线----------')
        count += 1
        continue
    print(line.strip())
    count +=1
   '''

"""
#low loop
for index,line in enumerate(f.readlines()):
    if index == 9:
        print('----我是分割线----------')
        continue
    print(line.strip())
#for i in range(5):
"""