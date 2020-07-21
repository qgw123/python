__author__ = 'qgw'

# import  os
# os.path.abspath(__file__)
# print(os.path.dirname(os.path.abspath(__file__)))

class Class:
    def __init__(self, contran, shengfen, shi, zheng, cun):
        self.contran = contran
        self.shengfen = shengfen
        self.shi = shi
        self.zheng = zheng
        self.cun = cun

    def paly(self):
        print( '%s: zhenghaowandedifang' % self.shengfen)




r1 = Class('CN', 'GD', 'SZ', 'LG', 'HG')

r1.paly()
print(r1.contran)


