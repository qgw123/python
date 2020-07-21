src_name = '/bin/cp'
drt_name = '/tmp/cp'

srcf = open(src_name, 'rb')
detf = open(drt_name, 'wb')

while True:
    data = srcf.read(4096)
    # if data == b'':   #如果文件已读完，再读取将会得到空窜，退出循环
    # if len(data) == 0:
    if not data :  #空窜为false。取反为true
        break
    else:
        detf.write(data)

srcf.close()
detf.close()



