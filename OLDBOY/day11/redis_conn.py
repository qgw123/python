__author__ = 'qgw'
import redis

# r = redis.Redis(host='192.168.80.128', port=6379, password='qwe123')
# r.set('doo', 'bar')
#
# print(r.get('doo'))

###连接池
pool = redis.ConnectionPool(host='192.168.80.128',
                            port=6379,
                            password='qwe123')

r = redis.Redis(connection_pool=pool)
r.set('foo','qgw')
print(r.get('foo'))

