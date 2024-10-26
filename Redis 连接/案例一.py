# 从TxT文档中解析学生的信息，把考试成绩超过85分的同学信息，缓存到Redis的哈希表中
import redis

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 2
}

redis_pool = redis.ConnectionPool(**__config)
redis_client = redis.Redis(connection_pool=redis_pool)
pipline = redis_client.pipeline()

with open('text', 'r', encoding='utf-8') as f:
    result = f.readlines()
    print(result)
    student_info = []
    for value in result:
        new_value = value.replace('\n', '')
        info_arr = new_value.split(',')
        print(info_arr)
        item = {
            'number': info_arr[0],
            'name': info_arr[1],
            'class': info_arr[2],
            'score': info_arr[3]
        }
        student_info.append(item)

    for item in student_info:
        if int(item.get('score', 0)) >= 85:
            pipline.multi()
            pipline.hset('student', item['name'], item['score'])
            pipline.execute()
