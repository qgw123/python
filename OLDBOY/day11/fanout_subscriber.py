__author__ = 'qgw'

'''
Publish\Subscribe(消息发布\订阅)　

消息被所有的Queue收到，类似广播的效果，这时候就要用到exchange了，

Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息:
    fanout: 所有bind到此exchange的queue都可以接收消息
    direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
    topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'
))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare('', exclusive=True)
#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print('[X] %r ' % body)

channel.basic_consume(queue_name,
                     callback,
                     True)

channel.start_consuming()


