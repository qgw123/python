__author__ = 'qgw'

from day12 import ORM多外建
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=ORM多外建.engine)
session = Session_class()

# addr1 = ORM多外建.Address(street='LongGang',city='ShenZhen', state='GD')
# addr2 = ORM多外建.Address(street='BaiYun',city='GuangZhou', state='GD')
# addr3 = ORM多外建.Address(street='DanShui',city="HuiZhou", state='GD')
# addr4 = ORM多外建.Address(street='XingNing',city='MeiZhou', state="GD")
#
# session.add_all([addr1, addr2, addr3, addr4])
#
# c1 = ORM多外建.Customer(name='qgw', billing_address=addr1, shopping_address=addr2)
# c2 = ORM多外建.Customer(name='asd', billing_address=addr3, shopping_address=addr3)
# c3 = ORM多外建.Customer(name='liangzan', billing_address=addr1, shopping_address=addr4)
#
# session.add_all([c1, c2, c3])

obj = session.query(ORM多外建.Customer).filter(ORM多外建.Customer.name=='qgw').first()
print(obj.name, obj.billing_address, obj.shopping_address)

session.commit()