__author__ = 'qgw'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:123456@192.168.80.128/db2?charset=utf8mb4',
                       encoding='utf-8')
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shopping_address_id = Column(Integer,ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys=[billing_address_id])
    shopping_address = relationship('Address', foreign_keys=[shopping_address_id])


class Address(Base):
    __tablename__    = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return  self.street

Base.metadata.create_all(engine)

