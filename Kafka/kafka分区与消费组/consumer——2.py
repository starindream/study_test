# consumer_demo.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'demo_topic',
    bootstrap_servers='localhost:9092',
    group_id='group1',  # 同一个消费组
    auto_offset_reset='earliest',  # 从最早开始消费
    enable_auto_commit=True,
    value_deserializer=lambda m: m.decode('utf-8')
)

print("Consumer started...")
for msg in consumer:
    print(f"[Consumer] Topic: {msg.topic}, Partition: {msg.partition}, Offset: {msg.offset}, Value: {msg.value}")
