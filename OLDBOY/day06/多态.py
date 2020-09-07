__author__ = 'qgw'

class Animal(object):
    def __init__(self,name):
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        pass #raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Dog(Animal):
    def talk(self):
        print('汪汪汪')

class Cat(Animal):
    def talk(self):
        print('喵喵喵')

d = Dog('qwe')
c = Cat('asd')
# d.talk()
# c.talk()
Animal.animal_talk(c)
Animal.animal_talk(d)
