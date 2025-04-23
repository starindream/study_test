from kafka import KafkaConsumer, KafkaProducer
from kafka.structs import TopicPartition
import json
import time

# 消费组需要消费消息，必须要绑定消费主题、或消费分区、或订阅主题，否则消费组无法正常进行消费。
# 消费组创建后，如果没有指定从最早的消息开始消费，则默认是消费未来的消息
# offset 消费组消费的起始位置，默认是最新的消息
# KafkaConsumer 返回的 consumer 实例中，在通过 message 获取 self.consumer 中的消息时，会阻塞线程，直到有消息可消费。
# 消费组默认自动消费，消费完成后 offset 会进行偏移，也可以手动进行消费，自动调用 commit 来提交消费，让 offset 进行偏移。
"""
1、kafka中的主题保存的消息自动将消息分发到不同的分区中，这样做是为了可以让消费组中的多个消费者可以并发读取，且一个分区只能被一个消费者消费。
    不会出现多个消费者消费同一个分区的情况。
2、 消费组中不会有多个消费者消费同一个消息。同一个消费组中的消费者可以消费同一个主题的不同分区，但不能消费同一个主题的同一个分区。
3、 自理解：kafka将消息分发到不同分区中，且不同分区中的消息都不重复，且是有序的，而且kafka的消费组不会有多个消费者消费同一条消息。
"""

# --------------- 消费者 和 kafka 的分区问题 ---------------
"""
1、理解消费组和消费者的概念，消费组时针对消息的主体，表示该消息必须在该消费组内被消费，至于被谁消费，则不需要管，可以理解为多客户端写入kafka的日志消息
    只需要确保日志消息被写入数据库即可，无需管理是哪个客户端写入的。
2、如果在 producer 生产消息时，没有指定消息分区，也没有指定key，kafka会使用轮训策略将消息平均分配到多个分区中。
    如果制定了key，kafka 则会使用 key 的哈希值来决定分区，确保相同的 key 的消息进到相同分区。
3、如果消费组没有指定分区并订阅了主题，kafka 会将这个主题下的所有分区自动均匀分配到这个消费组中的消费者
    如果一个消费者，则消费所有分区。
    如果多个消费者，则每个消费者消费其中一部分分区，不会重复消费。
    所以，即使消息被写入了多个分区，只要你订阅了整个主题，Kafka 会帮你分配对应的分区，你就不会漏掉任何消息。
4、同一时间一个分区只能被一个消费者消费，但在不同时间，该分区可能被另一个消费者消费，但只能有一个消费者。
5、subscribe 可以让消费者自动订阅主题，相当于订阅新主题。
6、poll 方法可以手动获取指定的消息批次，也可以指定阻塞时间，如果在指定的阻塞时间内都没有消息，会返回一个空的结果，使用poll方法可以自定义消息获取的频率。
    手动处理批次消息，进行手动提交。
"""


class KConsumer:
    _encode = 'utf-8'

    def __init__(self, topics="start_server", bootstrap_server=None, group_id="start_task", partitions=None,
                 **kwargs):
        if bootstrap_server is None:
            bootstrap_server = ['localhost:9092']
        # 此处没有绑定消费主题，后续也没有subscribe来订阅主题，也没有使用partitions来指定分区，导致该消费组消费不到消息。
        self.consumer = KafkaConsumer(topics, group_id=group_id,
                                      bootstrap_servers=bootstrap_server, api_version=(3, 9, 0), **kwargs)
        exist = self.exist_topics(topics)
        if not exist:
            self.create_topics(topics)
        if partitions is not None:
            self.consumer = KafkaConsumer(bootstrap_server=bootstrap_server, api_version=(3, 9, 0), group_id=group_id,
                                          **kwargs)
            self.topic_set = TopicPartition(topics, int(partitions))
            self.consumer.assign([self.topic_set])

    def exist_topics(self, topics):
        topics_set = set(self.consumer.topics())
        if topics not in topics_set:
            return False
        return True

    def create_topics(self, topics):
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            api_version=(3, 9, 0),
            key_serializer=lambda k: json.dumps(k).encode('utf-8'),
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        producer.send(topics, key='start', value={'msg': 'aaa'})
        producer.close()

    def recv_seek(self, offset):
        self.consumer.seek(self.topic_set, offset)
        for message in self.consumer:
            print('message:', message)
            yield {'topic': message.topic, 'partition': message.partition, 'offset': message.offset, 'key': message.key,
                   'value': message.value.decode(self._encode)}

    def poll(self, ):
        # # 必须要设置第一个参数timeout_ms，表示需要多长时间获取参数。不传递的话就是 0 ，会直接返回 {}
        # res = self.consumer.poll(10000)
        # print('consumer poll', res)
        # return res

        while True:
            # max_records 是指单次最多拉取20条，不是最少20条。
            res = self.consumer.poll(10000, max_records=20)
            for key, records in res.items():
                print('key:', key)
                print('records:', records)
                for message in records:
                    print('message:', message)
            if res:
                self.consumer.commit()
            print('consumer poll', res)

    def recv(self):
        print('consumer实例：', self.consumer)
        # self.consumer 会阻塞线程，直到有消息可消费
        for message in self.consumer:
            print('message:', message)
            yield {'topic': message.topic, 'partition': message.partition, 'offset': message.offset, 'key': message.key,
                   'value': message.value.decode(self._encode)}


if __name__ == '__main__':
    # kc = KConsumer(topics='test', group_id='test', bootstrap_server=['localhost:9092'])
    # print('kc:', kc)
    # for i in kc.recv():
    #     print('i=>', i)
    # time.sleep(30)

    # ----手动提交-----
    kc = KConsumer(topics='test', group_id='test112', bootstrap_server=[
        'localhost:9092'], enable_auto_commit=False, )
    result = kc.poll()
    print('poll=>result:', result)
    print('进程结束')
