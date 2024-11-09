import redis

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'db': 0,
    'decode_responses': True,
}

redis_pool = redis.ConnectionPool(**__config)

redis_client = redis.Redis(connection_pool=redis_pool)

print(redis_client.set('key1', 'value1'))
print(redis_client.get('key1'))
print(redis_client.setnx('key1', 'value1_u'))
print(redis_client.get('key1'))
print(redis_client.getrange('key1', 1, 3))
print(redis_client.mset({'key2': 'value2', 'key3': 'value3'}))
print(redis_client.mget('key1', 'key2', 'key3'))
