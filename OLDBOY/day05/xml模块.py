__author__ = 'qgw'
# https://www.cnblogs.com/alex3714/articles/5161349.html
'''
xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，
但json使用起来更简单，不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，
至今很多传统公司如金融行业的很多系统的接口还主要是xml。
'''
import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)