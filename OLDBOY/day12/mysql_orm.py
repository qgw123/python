__author__ = 'qgw'

'''
https://www.cnblogs.com/alex3714/articles/5978329.html
'''
'''
优点：
    1、隐藏了数据访问细节，“封闭”的通用数据库交互，ORM的核心。
    他使得我们的通用数据库交互变得简单易行，并且完全不用考虑该死的SQL语句。快速开发，由此而来。
    2、ORM使我们构造固化数据结构变得简单易行。
    
缺点：
    无可避免的，自动化意味着映射和关联管理，代价是牺牲性能（早期，这是所有不喜欢ORM人的共同点）。
    现在的各种ORM框架都在尝试使用各种方法来减轻这块（LazyLoad，Cache），效果还是很显著的

'''

'''
在Python中，最有名的ORM框架是SQLAlchemy。

安装sqlalchemy:
        pip3 install SQLAlchemy 
'''

'''
Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如：
    MySQL-Python
        mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
        
    pymysql
        mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
   
    MySQL-Connector
        mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
   
    cx_Oracle
        oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
    '''