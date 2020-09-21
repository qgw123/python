__author__ = 'qgw'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func     #分组

engine = create_engine('mysql+pymysql://root:123456@192.168.80.128/db1',
                       encoding='utf-8',)#echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return  '<%s name: %s>' % (self.id, self.name)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
sess = Session_class()

# fake_user = User(name='Rain', password='12345')
# sess.add(fake_user) #添加数据

#查询
# data = sess.query(User).filter_by().all()   #all 查询所有
data  = sess.query(User).filter_by(name='TTG').first()
#sess.query(User).filter().all #filter() ()里填写需要配置的字段
#多条件查询
#objs = sess.query(User).filter(User.id>0).filter(User.id<7).all()
print(data)

#修改         #查找到后修改
# data.name = 'TTG'
# data.password = '123456'
# sess.commit()

#统计
# t = sess.query(User).filter(User.name.like("%G")).count()
# print(t)

#分组
# print(sess.query(func.count(User.name),User.name).group_by(User.name).all() )
