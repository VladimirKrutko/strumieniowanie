import pika

parameters = pika.URLParameters('amqp://user:pass@localhost:5672')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test')


def callback(ch, method, properties, body):
    print ("Get : %r" % (body,))

channel.basic_consume('test',callback)

channel.start_consuming()
    