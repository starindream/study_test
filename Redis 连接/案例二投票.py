# 用Python程序模拟 300 位观众，为5位嘉宾（马云、丁磊、张朝阳、马化腾、李彦宏）随机投票，最后按照降序排列结果

import time
import random
import redis
from concurrent.futures import ThreadPoolExecutor

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 3,
}

redis_pool = redis.ConnectionPool(**__config)
# redis_client = redis.Redis(connection_pool=redis_pool)
# pipline = redis_client.pipeline()

dict_name = {
    1: '马云',
    2: '丁磊',
    3: '张朝阳',
    4: '马化腾',
    5: '李彦宏'
}


# 模拟300位观投票需要建立 300个客户端和300个线程，如果只用一个客户端会300个线程的命令都是发往一个客户端，导致命令的顺序不可控
# 用一个客户端可能会导致，上一个线程使用了 事务的开始，下一个线程马上又发送监听命令。
# 导致redis报在事务开始时发送监听的错误，redis开启事务但未执行，中间发送监听。
def run(n):
    redis_client = redis.Redis(connection_pool=redis_pool)
    pipline = redis_client.pipeline()
    while True:
        try:
            vote = dict_name.get(random.randint(1, 5))
            pipline.watch(vote)
            pipline.multi()
            pipline.incrby(vote, 1)
            result = pipline.execute()
            print(f'成功{n}:{result}')
            break
        except Exception as e:
            print(f'设置失败{n}')
            print(e)
    return True


def main_thread():
    with ThreadPoolExecutor(max_workers=20) as executor:
        print('ThreadPoolExecutor')
        thread_list = range(300)
        executor = executor.map(run, thread_list)
    print('executor', executor)
    return sort_candidate()


def sort_candidate():
    redis_client = redis.Redis(connection_pool=redis_pool)
    candidate = []
    for item in dict_name.values():
        # candidate_people = {
        #     item: redis_client.get(item)
        # }
        candidate_people = (item, redis_client.get(item))
        candidate.append(candidate_people)
    print(candidate)
    return sorted(candidate, key=lambda one: one[1] if one[1] else 0, reverse=True)


if __name__ == '__main__':
    result = main_thread()
    print('排名结果:', result)
    # sort_candidate()
