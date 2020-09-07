__author__ = 'qgw'
# import urllib
from urllib import request

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open('url.html', 'wb')
    f.write(data)
    f.close()
    print('%d bytes received from %s.'% (len(data),url))

f('https://www.cnblogs.com/alex3714/articles/5248247.html')