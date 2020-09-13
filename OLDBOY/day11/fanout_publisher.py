__author__ = 'qgw'

'''Publish\Subscribe(消息发布\订阅)　'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ''.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs',
                        routing_key='',
                        body=message)

print('[X] Sent %r ' % message)
connection.close()