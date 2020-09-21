__author__ = 'qgw'

import  pymysql

#创建连接
conn = pymysql.connect(host='192.168.80.128',
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='db1')
#创建游标
cursor = conn.cursor()

effect_row = cursor.execute('select * from student')
#查询数据
print(cursor.fetchone())
print(cursor.fetchone())
print('----------------')
print(cursor.fetchall())

#插入数据
data = [('TS', '3', '2016-12-10'),
        ]
cursor.executemany('insert into student (name,age,time) values (%s,%s,%s)' , data)
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
