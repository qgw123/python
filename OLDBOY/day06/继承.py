__author__ = 'qgw'

# class People      #经典类
class People(object):   #新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eatting......' % self.name)

    def talk(self):
        print('%s is talking......' % self.name)

    def sleep(self):
        print('%s is sleeping......' % self.name)



class Man(People):    #执行顺序
    def __init__(self,name, age, money):
        # People.__init__(self, name, age )     #调用父类
        super(Man,self).__init__(name, age)     #调用父类   新式类写法
        self.money = money
        print('%s 一出生就有: %s ￥'  % (self.name, self.money))

    def piao(self):
        print('%s is paio......30s......done' % self.name)

    def sleep(self):
        People.sleep(self)
        print('man is sleep' )

class Woman(People):
    def shopping(self):
        print('%s is shopping......' % self.name)

m1 = Man('qwe', 22, 10000)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman('girl', 30)
w1.sleep()
w1.shopping()
