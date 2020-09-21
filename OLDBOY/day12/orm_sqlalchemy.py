__author__ = 'qgw'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@192.168.80.128/db1',
                       encoding='utf-8' ,echo=True ) #echo=true:打印消息

Base = declarative_base() #生成ORM基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)       #创建表结构

#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class()       #生成session实例  #curson

user_job = User(name='DYG' , password='12346')  #生成你要创建的数据对象
user_job2 = User(name='XYG', password='987654') #生成你要创建的数据对象

Session.add(user_job)       #把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_job2)      #把要创建的数据对象添加到这个session里， 一会统一创建

Session.commit()        #现此才统一提交，创建数据,  commit后才会将数据写入库中