#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# durable=True => Make queue durable (if rabbitMQ down, the queue still exists)
# If we not set, if rabbitMQ down, the queue will be deleted.
channel.queue_declare(queue='task_queue', durable=True)

# check if there's argument in the command, if not, use default value
# Ex:
# python3 send.py Hello..........
# => message = "Hello.........." 
# python3 send.py
# => message = "Hello World!"
message = ' '.join(sys.argv[1:]) or "Hello World!"

# properties=pika.BasicProperties(
#    delivery_mode=2,  # make message persistent
# ))
# => 
# Make message persistent (if rabbitMQ down, the message still exists)
# If we not set, if rabbitMQ down, the message will be deleted.
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))

print(" [x] Sent %r" % message)
connection.close()
