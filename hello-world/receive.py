#!/usr/bin/env python
import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Khi auto_ack được đặt thành True, 
    # consumer sẽ tự động gửi phản hồi cho RabbitMQ ngay sau khi nhận được message, 
    # mà không cần phải gọi phương thức basic_ack() để gửi phản hồi. 
    # Điều này có nghĩa là
    # RabbitMQ sẽ xóa message khỏi queue ngay lập tức sau khi gửi message đến consumer,
    # mà không cần phải chờ đợi phản hồi từ consumer trước.

    # Tuy nhiên, việc sử dụng auto_ack=True cũng có thể dẫn đến một số vấn đề, 
    # như là mất mát message hoặc xử lý trùng lặp message,
    # nếu consumer không xử lý message thành công hoặc xảy ra lỗi.

    # Do đó, việc sử dụng auto_ack=True nên được cân nhắc cẩn thận
    # và chỉ được sử dụng trong các trường hợp đơn giản,
    # nơi không cần quản lý phản hồi của message.
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
