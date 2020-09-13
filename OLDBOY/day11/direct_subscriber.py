__author__ = 'qgw'

import  pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host= 'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare('',exclusive=True)
queue_name = result.method.queue

severites = sys.argv[1:]
if not severites:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severites:
    channel.queue_bind (exchange='direct_logs',
                        queue=queue_name,
                        routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, preperties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue_name,
                      callback,
                      True)

channel.start_consuming()
