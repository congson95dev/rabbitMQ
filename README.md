# 

## Before we begin, we need to install pika and rabbitMQ by docker (simpler than normal rabbitMQ installation)

## Install pika
`pip install pika --upgrade`

## Install rabbitMQ by Docker
https://www.rabbitmq.com/download.html

## rabbitMQ default behavior is acting by "round robin", which is by orderly
## Ex:
### open 2 terminal and run "python3 receive.py", and another terminal and run "python3 send.py" for 10 time.
### you will see 5 ouput from terminal receiver 1, and 5 ouput from terminal receiver 2.

## hello-world
### this is simplest example to describe how round robin work

## workers
### this is example where 1 receiver is processing and busy, then when we continue to send message, the receiver 2 will handle it but not receiver 1
### such as send a message with time.sleep for 10 second to receiver 1, and while receiver 1 are sleeping, whenver we send a message, receiver 2 will receive

## pub-sub
### this is example where all receiver will subcribe to the sender, and whenever sender send a message, all receiver will receive