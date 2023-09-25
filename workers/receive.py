#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# durable=True => Make queue durable (if rabbitMQ is down, the queue still exists)
# If we not set, if rabbitMQ down, the queue will be deleted.
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    # for every "." in the "python3 send.py Hello.........." command,
    # it will sleep that much seconds
    # 10 "." => 10s sleep
    time.sleep(body.count(b'.'))
    print(" [x] Done")

    # this is the same as auto_ack=True in the below command
    # channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    # not sure about the delivery_tag,
    # i've print(method.delivery_tag) and for every time it receive message,
    # it will +1 to the result
    ch.basic_ack(delivery_tag=method.delivery_tag)


# set how many message each receiver will process
# ex:
# if receiver 1 is processing a message for 10 seconds because of time.sleep command
# then when we send another message,
# receiver 1 will not accept it because it's busy,
# it gonna transfer to receiver which not busy
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
