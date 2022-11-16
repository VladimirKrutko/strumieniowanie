import pika
from time import sleep
from datetime import datetime

# parameters = pika.URLParameters('amqp://user:pass@localhost:5672')
# connection = pika.BlockingConnection(parameters)
# channel = connection.channel()


# channel.queue_declare(queue='hello')


if __name__ == '__main__':
    parameters = pika.URLParameters('amqp://user:pass@localhost:5672')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()


    channel.queue_declare(queue='test')

    while True:
        try:
            message = datetime.now()
            print(f'Send: {message}')
            channel.basic_publish(exchange='',
                      routing_key='test',
                      body=f'{message}')
            sleep(1)
        except KeyboardInterrupt:
            break
    
    channel.close()

