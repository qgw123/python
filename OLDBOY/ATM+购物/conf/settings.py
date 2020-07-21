__author__ = 'qgw'
import  os
import sys
import  logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

database = {'engine': 'file_storage',
            'name': 'accounts',
            'path': '%s/db' % BASE_DIR}
#
# LOG_lever = logging.log()
print(BASE_DIR)