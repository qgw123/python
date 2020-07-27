__author__ = 'qgw'

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def drunk(self):
        print('%s is drunking......' % self.name)

    def sleep(self):
        print('%s is sleeping......' % self.name)

class Relation(object):     #执行顺序：从左到右
    # def __init__(self):
    def making_friends(self, ojb):
        print("%s is making friend with %s " % (self.name, ojb.name))
        self.friends.append(ojb)

class  Man(People, Relation):
    # def __init__(self,name, age, money):
    #     # People.__init__(self, name, age )     #调用父类
    #     super(Man,self).__init__(name, age)     #调用父类   新式类写法
    #     self.money = money
    #     print('%s 一出生就有: %s ￥'  % (self.name, self.money))

    def piao(self):
        print('%s is paio......30s......done' % self.name)

    def sleep(self):
        People.sleep(self)
        print('man is sleep' )

class Woman(People):
    def get_birth(self):
        print("%s is get birth ......" % self.name)

m1 = Man('小叶', 20)
w1 = Woman('小苏', 18)
m1.making_friends(w1)

w1.name = "小陈"
print(m1.friends[0].name)