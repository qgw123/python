__author__ = 'qgw'

class Flight(object):
    def __init__(self,name):
        self.name = name

    def checking_status(self):
        print('checking flight %s status' % self.name)

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print('flight got canceled...')
        elif status == 1:
            print('flight is arrived...')
        elif status == 2:
            print('flight has departured already...')
        else:
            print('cannot confirm the flight status...,please check later')

    @flight_status.setter
    def flight_status(self,status):
        status_dic = {0:'canceled', 1:'arrived', 2:'departured'}
        print("\033[31;1mHas changed the flight status to \033[0m",status_dic.get(status))

    @flight_status.deleter
    def flight_status(self):
        print("status got removed...")


f = Flight('CA980')
f.flight_status
f.flight_status = 1
# del f.flight_status