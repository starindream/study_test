import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 0
}

# 创建连接池
redis_pool = redis.ConnectionPool(**config)
# 创建redis实例，每个redis 实例内部都会维护一个自己的连接池，在execute_command 方法中会创建连接，并保留此次创建的连接
redis_client = redis.Redis(connection_pool=redis_pool)

# 定义一个管道，将所有的命令都存放在管道中
pip = redis_client.pipeline()
pip.watch('book1')
pip.multi()
pip.set('book1', 'book1')
pip.set('book2', 'book2')
pip.get('book1')
pip.get('book2')
result = pip.execute()
print(result)
