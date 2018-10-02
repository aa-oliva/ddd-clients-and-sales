import pika


def send_promotions(promotions):
    # connected to broadcaster on localhost (can change to ips from another machine)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # queue which will receive messages , if theres not a queue rabbit will drop messages
    channel.queue_declare(queue='hello')
    # messages cant just be sent, they need to go through an exchange,
    # this exchange lets us specify which queue receives
    # in the routing_key parameter
    channel.basic_publish(exchange='', routing_key='order', body=promotions)
    print(" [x] Sent ", promotions)
    # necessesary
    connection.close()
