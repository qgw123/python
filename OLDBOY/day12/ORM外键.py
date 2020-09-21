__author__ = 'qgw'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:123456@192.168.80.128/db2?charset=utf8mb4',
                       encoding='utf-8')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    time = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.name)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32))
    stu_id = Column(Integer, ForeignKey('student.id'))

    student = relationship('Student', backref='my_study_record')

    def __repr__(self):
        return '<%s day: %s status: %s >' % (self.student.name , self.day, self.status)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

# s1 = Student(name='qqqq', time='2015-10-01')
# s2 = Student(name='wwww', time='2016-10-01')
# s3 = Student(name='eeee', time='2016-11-13')

# stu1 = StudyRecord(day=1,status='YES',stu_id=1)
# stu2 = StudyRecord(day=2,status='NO',stu_id=1)
# stu3 = StudyRecord(day=3,status='YES',stu_id=1)
# stu4 = StudyRecord(day=1,status='YES',stu_id=2)

# session.add_all([s1,s2,s3])
# session.add_all([stu1,stu2,stu3,stu4])

stu_obj = session.query(Student).filter(Student.name=='qqqq').first()
print(stu_obj.my_study_record)
session.commit()



