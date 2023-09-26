# 

### Before we begin, we need to install pika and rabbitMQ by docker (simpler than normal rabbitMQ installation)

## Install pika
`pip install pika --upgrade`

## Install rabbitMQ by Docker
https://www.rabbitmq.com/download.html

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
ctrl PQ
```

rabbitMQ default behavior is acting by `round robin`, which is by orderly

Ex:

open 2 terminal and run "python3 receive.py", 
and another terminal and run "python3 send.py" for 10 time.

you will see 5 ouput from terminal receiver 1, 
and 5 ouput from terminal receiver 2.

## hello-world
this is simplest example to describe how round robin work

## workers
this is example where 1 receiver is processing and busy, 
then when we continue to send message, the receiver 2 will handle it but not receiver 1

such as send a message with time.sleep for 10 second to receiver 1, 
and while receiver 1 are sleeping, whenver we send a message, receiver 2 will receive

## exchange types
there are 4 types of exchange in rabbitMQ:

fanout, topic, direct, headers

### fanout:
all receiver will subcribe to the sender, and whenever sender send a message, 
all receiver will receive

### topic:
receiver will receive message from the sender based on the `routing_key`

Ex: 
```
python3 receive.py "#"
python3 receive.py "test1.#"
python3 receive.py "test1.*"
python3 receive.py "test1.*" "*.com"
```
```
python3 send.py "test1.com" "just some random message"
```

all receiver above are receive message successfully from sender `"test1.com"`

### direct
receiver will receive message from the sender based on the `routing_key`

this work differently than normal rabbitMQ, 
because normal rabbitMQ run `round robin` algorithms 
but this `direct` exchange send to all receiver with the exactly `routing_key` 
at the same time

Ex: 
```
python3 receive.py test1
python3 receive.py test1 test2
```
```
python3 send.py test1 "just some random message"
python3 send.py test2 "just some random message"
```

### headers
this exchange type is not so familiar and even tutorial doesn't cover this part 
even though other part they doing great.
So i will skip this exchange type for now.

But you can always do it if you want, try this link:

https://www.tumblr.com/deontologician/19741542377/using-pika-to-create-headers-exchanges-with