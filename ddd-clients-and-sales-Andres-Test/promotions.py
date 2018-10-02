import math
import send
import json


# order should come in format [[nameoffood, priceoffood]]
def give_promotions(order):

    order = order.sort()
    promotions = []

    for food in order:
        if float(food[1]) <= 10.0:
            promotions.append([food[0], math.sqrt(float(food[1])) / 2])

    promotions = json.dumps(promotions)
    send.send_promotions(promotions)
