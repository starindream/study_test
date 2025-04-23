import json
import kafka


# kafka 在使用前，需要先启动 zookeeper 服务，然后启动 kafka 服务。
# 主要是通过类，来创建统一的kafka生产者，这样可以在发送kafka消息时，针对同一个服务器broker，只需要定义消息和主题即可。


class Producer:
    def __init__(self, broker="localhost:9092", topic="add_topic", max_request_size=104857600, batch_size=0, **kwargs):
        self.broker = broker
        self.topic = topic
        self.max_request_size = max_request_size
        # self.producer_json = kafka.KafkaProducer(bootstrap_servers=self.broker, max_request_size=self.max_request_size,
        #                                          batch_size=batch_size,
        #                                          key_serializer=lambda k: json.dumps(
        #                                              k).encode(self._coding),
        #                                          # 设置键的形式使用匿名函数进行转换
        #                                          value_serializer=lambda v: json.dumps(
        #                                              v).encode(self._coding),
        #                                          # 当需要使用 json 传输地时候必须加上这两个参数
        #                                          **kwargs)

        self.producer = kafka.KafkaProducer(bootstrap_servers=self.broker, max_request_size=self.max_request_size,
                                            batch_size=batch_size, api_version=(3, 9, 0), **kwargs)

    def send(self, message, partition=None
             ):
        future = self.producer.send(self.topic, message, partition=partition)
        record_metadata = future.get(timeout=30)
        print('record_metadata:', record_metadata)
        if future.failed():
            raise Exception(f'send message failed{future.exception}')

    def close(self):
        # self.producer_json.close()
        self.producer.close()


if __name__ == '__main__':
    kafka_obj = Producer(topic='test')
    print('kafka=>', kafka_obj)
    print(kafka_obj.broker)
    for i in range(10):
        kafka_obj.send(f"new message{i}".encode())

    # kafka_obj.send("new message1234".encode())
