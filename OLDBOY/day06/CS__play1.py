__author__ = 'qgw'

'''
析构函数
私有方法、私有属性
'''
class Role(object):

    def __init__ (self, name, role, waepon,life_value=100, money=15000):
        self.name = name
        self.role = role
        self.waepon = waepon
        self.__life_value = life_value      #私有属性 在前面添加“__”
        self.money = money

    def __del__(self):      #析构函数
        pass #print("%s彻底死了!!!!!!" % self.name)

    def show_status(self):
        print('name: %s; waepon: %s; life_val:%s ' % (self.name, self.waepon,self.__life_value))

    def __shot(self):       #私有方法  在前面加‘__’
        print("shooting...")

    def got_shot(self):
        r1.__shot()
        self.__life_value -= 50
        print("%s: ah...,I got shot..." % self.name)

    def buy_gun(self, gun_name):
        print('%s: just bought %s '% (self.name, gun_name))

r1 = Role('qwe', 'police', 'm416')
r1.buy_gun('AK47')
r1.got_shot()
r1.show_status()


# r2 = Role('asd', 'docker', 'B12')
# r2.buy_gun('B5')


