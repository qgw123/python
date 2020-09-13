__author__ = 'qgw'

'''
有选择的接收消息(exchange type=direct)　

RabbitMQ还支持根据关键字发送，即：队列绑定关键字，
发送者将数据根据关键字发送到消息exchange，exchange根据 关键字 判定应该将数据发送至指定队列。'
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [X] Sent %r:%r" % (severity, message))
connection.close()