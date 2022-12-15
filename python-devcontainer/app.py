# app.py
# fun fact: This snippet was generated entirely by Copilot
from flask import Flask, request
from kafka import KafkaProducer
from datetime import datetime
import json

app = Flask(__name__)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/posts', methods=['POST'])
def create_post():
    post = request.get_json()
    # clickhouse can only parse strings without milliseconds
    post['created_at'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    producer.send('posts', post)
    return 'ok'