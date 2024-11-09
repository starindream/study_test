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

print(redis_client.zadd('zset', {'key1': 1, 'key2': 2}))
print(redis_client.zrange('zset', 0, -1, withscores=True))
print(redis_client.zrank('zset', 'key2'))
