''''''

def test(x, y ,z):
    print(x)
    print(y)
    print(z)

# test(1, 2)
# test(12, 22)
# test(y=2,x=1)   #与形参顺序无关
# test(1,2)       #与形参一一对应
# # test(x=2, 3)
test(3,z=2,y=6)     #关键参数不能写在位置参数前面

#默认参数
def test(x,y=2):
    print(x)
    print(y)

test(1)
'''
默认参数的特点：调用函数的时候，默认参数非必传
用途：默认安装值
'''