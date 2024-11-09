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

print(redis_client.hset('hash', 'key2', 'va2lue11'))
print(redis_client.hget('hash', 'key2'))
print(redis_client.hgetall('hash'))
print(redis_client.hset('hash', mapping={'key3': 'value3', 'key4': 'value4'}))
print(redis_client.hmget('hash', ['key3', 'key4', 'key5']))
