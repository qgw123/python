__author__ = 'qgw'

import redis
import time

pool = redis.ConnectionPool(host='192.168.80.128',
                            port=6379,
                            password='qwe123')

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('name6', 'qgw')
pipe.set('role6', 'tc')

pipe.execute()
