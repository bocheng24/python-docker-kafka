from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'pykafka',
    bootstrap_servers = ['localhost:9092']
)

for msg in consumer:
    print(msg.value)