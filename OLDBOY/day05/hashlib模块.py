__author__ = 'qgw'

import  hashlib

# ######## md5 ########
m = hashlib.md5()
m.update(b'hello')
print(m.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

import hmac
h = hmac.new(b'qgw')
# h.update(b'hellowo')
print(h.hexdigest())