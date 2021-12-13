from kafka import KafkaProducer
import json
from data import get_user
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer = json_serializer
    )

if __name__ == '__main__':

    i = 0
    while i < 10:
        user = get_user()
        producer.send('pykafka', user)
        print(user)
        i += 1
        time.sleep(3)