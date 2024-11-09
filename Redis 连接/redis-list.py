import redis

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 0
}

redis_pool = redis.ConnectionPool(**__config)

redis_client = redis.Redis(connection_pool=redis_pool)

print(redis_client.delete('list'))
print(redis_client.lpush('list', 'A', "B"))
print(redis_client.lrange('list', 0, -1))
print(redis_client.linsert('list', 'before', 'A', 'C'))
print(redis_client.lrange('list', 0, -1))
