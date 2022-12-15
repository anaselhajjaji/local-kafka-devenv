# producer.py
from datetime import datetime
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
producer.send('posts', {'author': 'anas', 'content': 'Hello Kafka!', 'created_at': datetime.now().isoformat()})
