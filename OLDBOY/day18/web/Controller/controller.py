__author__ = 'qgw'

import time
def haddle_index():
    now_time = str(time.time())
    f = open('web/View/index.html' , 'rb')
    data = f.read()
    f.close()
    data = data.replace(b'@uuuuu', now_time.encode('utf-8'))
    return [data,]
    # return ['<h1> Hello Index! </h1>'.encode('utf-8'), ]

def haddle_data():
    return ['<h1> Hello Data! </h1>'.encode('utf-8'), ]