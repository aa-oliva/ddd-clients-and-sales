import pika
import promotions
import json

# connected to broadcaster on localhost (can change to ips from another machine)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='order')


def callback(ch, method, properties, body):

	print("Method: {}".format(method))
	print("Properties: {}".format(properties))

    data = json.loads(body)
    print("ID: {}".format(data['order-id']))
    print("Customer: {}".format(data['customer']))
    
    promotions.give_promotions(data)

channel.basic_consume(callback, queue='order', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()