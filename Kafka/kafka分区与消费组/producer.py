# producer_demo.py
from kafka import KafkaProducer, KafkaAdminClient
import time

# 默认只有一个分区，所以只会有一个消费者消费。

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: v.encode('utf-8')
)

admin = KafkaAdminClient(bootstrap_servers='localhost:9092')

for i in range(10):
    msg = f"message-{i}"
    producer.send('demo_topic', value=msg)
    print(f"Produced: {msg}")
    # time.sleep(1)  # 加个延迟方便观察

topic_name = 'demo_topic'
topic_metadata = admin.describe_topics([topic_name])
print('metadata for topic:', topic_metadata)
for topic in topic_metadata:
    print('ttt', topic)
    print(f"Number of partitions: {len(topic.partitions)}")
    print(f"Topic: {topic.topic}")

producer.flush()
producer.close()
