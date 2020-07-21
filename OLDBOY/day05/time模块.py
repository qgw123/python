__author__ = 'qgw'

import time
print(time.time())          #获取时间戳
print(time.timezone)        #时间戳
print(time.localtime())     #isdst表示时区  tm_wday是从0开始  结果为本地时区（UTC+8：中国时区）
print(time.sleep(0.1))
print(time.gmtime())        #结果为UTC时区

x = time.localtime(1234567941)
# print(help(x))
print(x.tm_hour)
print("This is %s's day: %s" % (x.tm_year, x.tm_yday))

# time.mktime()   #将元组转换成时间戳
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strptime('2020-07-14 14:51:17','%Y-%m-%d %H:%M:%S'))
'''
strftime('格式'，元组(struct_time)) ---> '格式化的字符串'
    time.strftime('%Y-%m-%d %H:%M:%S')
strptime('格式化的字符窜'，'格式')    ---> struct_time(元组)
    time.strptime('2020-07-14 14:51:17','%Y-%m-%d %H:%M:%S')
'''
print(time.asctime())   #Tue Jul 14 15:13:41 2020
print(time.ctime())     #Tue Jul 14 15:14:14 2020

import datetime
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  #三天后的时间
print(datetime.datetime.now() + datetime.timedelta(hours=3))    #三小时的时间