# consumer.py
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'posts',
    bootstrap_servers=['kafka:9093'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
# note that this for loop will block forever to wait for the next message
for message in consumer:
    print(message.value)