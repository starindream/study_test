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

print(redis_client.delete('stream'))
print(redis_client.xadd('stream', {'message': 'info'}, '*'))
print(redis_client.xrange('stream', '-', '+'))
print(redis_client.xread({'stream': 0}))
