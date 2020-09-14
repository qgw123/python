__author__ = 'qgw'
import pika, time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello' ,durable=True) #durable=True 队列持久化

def callback(ch, method, properties, body): #回调函数
    print('--->',ch, method, properties)
    print('[x] Received %r' % body)
    time.sleep(20)
#print("method.delivery_tag", method.delivery_tag)-
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(#消费消息
                        'hello',
                        callback,   #如果收到消息，就调用callback函数处理
                       # queue='hello',
                        True,
                        )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

