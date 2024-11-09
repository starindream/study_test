import redis

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 3
}

redis_pool = redis.ConnectionPool(**__config)
redis_client = redis.Redis(connection_pool=redis_pool)

print(redis_client.sadd('set', 'A', 'B'))
print(redis_client.sadd('set2', 'A', 'C'))
print(redis_client.smembers('set'))
print(redis_client.sismember('set', 'AC'))
print(redis_client.sdiff(['set', 'set2']))
print(redis_client.sinter(['set', 'set2']))
print(redis_client.sunion(['set', 'set2']))
