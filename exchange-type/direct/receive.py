#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    # raise warning if the command to run this don't have param
    # Ex: python3 receive.py => raise warning
    # Ex: python3 receive.py test1 => accepted
    sys.stderr.write("Please add queue name after this command to make it work, "
                     "Ex: %s test1" % sys.argv[0])
    sys.exit(1)

# support multiple params
# Ex: python3 receive.py test1 test2
for binding_key in binding_keys:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
