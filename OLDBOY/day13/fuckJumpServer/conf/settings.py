__author__ = 'qgw'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#连接数据库
ConnParams = 'mysql+pymysql://root:123456@192.168.80.128/jumpdb?charset=utf8mb4'

