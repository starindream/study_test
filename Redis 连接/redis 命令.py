import redis

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'db': 0,
    'decode_responses': True,
}

# 创建连接池
redis_pool = redis.ConnectionPool(**__config)
# 创建连接的客户端
redis_client = redis.Redis(connection_pool=redis_pool)

redis_client.execute_command('SELECT', 1)

# 字符串：如果返回的是字节，则可以通过 client.get(key).decode('utf-8')
# print(redis_client.set('book1', 'book1'))
# print(redis_client.mset({'key1': 'value1', 'key2': 'value2'}))
# print(redis_client.mget('key1', 'key2'))
# for i in redis_client.mget('key1', 'key2'):
#     print(i)

# 列表
# print(redis_client.delete('name'))
# print(redis_client.rpush('name', 'jack'))
# print(redis_client.lpush('name', 'los'))
# print(redis_client.lrange('name', 0, - 1))

# 集合
# print(redis_client.sadd('space', '你好', 8))
# print(redis_client.smembers('space'))  # 返回的是一个集合
# for i in redis_client.smembers('space'):
#     print(i)

# 有序集合
# print(redis_client.zadd('sort', {'你好': 9, '测试': 8}))
# print(redis_client.zincrby('sort', 10, '你好'))
# print(redis_client.zrange('sort', 0, -1, withscores=True))
# print(redis_client.zrevrange('sort', 0, -1, withscores=True))

# 哈希表
# print(redis_client.hset('test', 'one', 'one'))
# print(redis_client.hset('test', mapping={'yyy': 'yyy', '222': '222'}))
# print(redis_client.hmget('test', ['one', 'yyy', '222']))

# 消息队列
print(redis_client.delete('mes'))
print(redis_client.delete('mes2'))
print(redis_client.xadd('mes', {'name': 'jack'}))
print(redis_client.xadd('mes', {'name': 'loi'}))
print(redis_client.xadd('mes', {'message': '你好'}))
print(redis_client.xadd('mes2', {'age': 12}))
print(redis_client.xread({'mes': 0, 'mes2': 0}))

# 创建消费组
print(redis_client.xgroup_create('mes', 'first', 0))
print(redis_client.xreadgroup('first', 'c1', {'mes': '>'}))
