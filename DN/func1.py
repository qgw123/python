def func1(*q):  #*号表示后面的名字是个元组
    print(q)

def func2(**w):     ##**号表示后面的名字是个字典
    print(w)

if __name__ == '__main__':
    func1()
    func1('qq')
    func1('qq','ww', 'ee')
    func2()
    func2(name='bob',age=20)