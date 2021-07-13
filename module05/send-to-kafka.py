from json import dumps
from time import sleep
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

for _ in range(1_000):
    quantity = random.randint(100, 400)
    price = random.randint(90, 110)
    order = {'symbol': 'orcl', 'price': price, 'quantity': quantity}
    producer.send('orders', value=order)
    sleep(3)
