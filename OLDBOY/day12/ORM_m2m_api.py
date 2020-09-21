__author__ = 'qgw'
from day12  import ORM_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=ORM_m2m.engine)
session = Session_class()

# b1 = ORM_m2m.Book(name="Python",pub_date='2017-10-11')
# b2 = ORM_m2m.Book(name="Linux", pub_date='2018-07-12')
# b3 = ORM_m2m.Book(name="Redis", pub_date='2020-08-13')
# b4 = ORM_m2m.Book(name="Mysql", pub_date='2020-09-20')
#
# a1 = ORM_m2m.Author(name='qgw')
# a2 = ORM_m2m.Author(name='asd')
# a3 = ORM_m2m.Author(name='zxc')
#
# b1.authors = [a1,a3]
# b3.authors = [a1,a2,a3]
#
# session.add_all([b1,b2,b3,b4,a1,a2,a3])

author_obj = session.query(ORM_m2m.Author).filter(ORM_m2m.Author.name=='qgw').first()
print(author_obj.books[1].pub_date)

book_obj = session.query(ORM_m2m.Book).filter(ORM_m2m.Book.id==1).first()
print(book_obj.authors)
print(book_obj)

session.commit()