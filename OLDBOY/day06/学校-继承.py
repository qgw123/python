__author__ = 'qgw'

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print('为学员%s办理注册' % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣新员工%s" % staff_obj.name)
        self.teachers.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
----Info of Teacher %s ----
Name: %s
Age: %s
Sex: %s
Salary: %s
Course: %s
''' % (self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('%s is teaching course [%s]' % (self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,sex,age)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
----Inof of Student %s ----
Name: %s
Age： %s
Sex: %s
Stu_id: %s
Grade: %s
'''
% (self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_file(self,amount):
        print('%s has paid $%s' % (self.name,amount))

S = School('QGW','sz')

t1 = Teacher('qwe','22','M',12000,'Chinese')
t2 = Teacher('asd','30','W',12000,'English')

s1 = Student('qaz','10','M',10,'三年二班')
s2 = Student('wsx','11','W',11,'三年一班')

t1.tell()
t2.tell()
s1.tell()
s2.tell()

S.hire(t1)
S.hire(t2)
S.enroll(s1)
S.enroll(s2)
S.teachers[0].teach()

for i in S.students:
    i.pay_file(5000)

for i in S.teachers:
    i.teach()