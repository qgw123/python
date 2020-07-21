__author__ = 'qgw'

x = 0
def grandpa():
    #x=1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()

grandpa()