import redis

__config = {
    "host": 'localhost',
    "port": 6379,
    'password': 'a123456789',
    "decode_responses": True,
}

# 直接连接
redis_client = redis.Redis(**__config)

# 连接池
redis_pool = redis.ConnectionPool(**__config)  # 建立连接池
redis = redis.Redis(connection_pool=redis_pool)  # 从连接池获取连接

redis.set('book', '西游记2')
print(redis.get('book'))

# 选择逻辑库
# redis.execute_command('SELECT', 1)
# print(redis.get('book'))
# redis.execute_command('SELECT', 0)
# print(redis.get('book'))

redis.execute_command('SET', 'video', '西游1记')

print(redis.execute_command('GET', 'video'))
