name = input('Name: ')
age = int(input('age: '))
job = input('job: ')
salary = input('salary: ')


# prompt = '''
# ---------------info in %s----------
# Name: %s
# Age: %s
# Job: %s
# salary: %s''' % (name,name, age, job, salary)

# info = '''
# -------------info in {_name}--------
# Name: {_name}
# age: {_age}
# Job: {_job}
# salary: {_salary}
# ''' .format(_name=name,
#             _job=job,
#             _age=age,
#             _salary=salary)

info= '''
-------------info in {0}--------
Name: {0}
age: {1}
Job: {2}
salary: {3}
''' .format(name,
            job,
            age,
            salary)

# print(prompt)
print(info)