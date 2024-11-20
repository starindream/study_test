import random
import time

import redis
# from concurrent.futures import ThreadPoolExecutor
import asyncio

__config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'a123456789',
    'decode_responses': True,
    'db': 3
}

# 创建redis连接池
redis_pool = redis.ConnectionPool(**__config)

success_id = []
error_id = []


async def run(id):
    print('id', id)
    while True:
        # 注意不宜使用 time.sleep 会导致整个线程停止，协程的事件循环调度也会停止
        # time.sleep(random.randint(1, 3))
        await asyncio.sleep(random.randint(1, 3))
        try:
            redis_client = redis.Redis(connection_pool=redis_pool)
            pipline = redis_client.pipeline()
            pipline.watch('kill_total')
            pipline.multi()
            pipline.decrby('kill_total', 1)
            result = pipline.execute()

            if result is not None:
                print(f'抢购成功:{id}', result)
                global success_id
                success_id.append(id)
                break
        except Exception as e:
            global error_id
            print(f'抢购失败{id}', e)
            error_id.append(id)


async def main():
    # 创建线程池。错误：使用线程时，当发生任务阻塞，线程会将任务挂起，等待任务结束，当100用户抢购时，无法实现100位用户的并发问题,当线程数量为20时，
    # with ThreadPoolExecutor(max_workers=100) as executor:
    #     thread_list = list(range(100))
    #     executor.map(run, thread_list)

    # 使用协程来实现，想要真正实现完全的并发，还是得使用多线程或者多进程，因为这样才是所有人都是公平竞争的，协程是单线程的，当一个任务在处理，其他任务不会开启
    # 使用协程，当任务发生阻塞时，任务会交出执行权，让事件调度执行其他任务，这样便可以实现100位用户同时并发，看谁的网络好便可以有限完成任务
    task = []
    for i in range(100):
        print(i, 'i')
        target = asyncio.create_task(run(i))
        task.append(target)
    print('task', task)
    await asyncio.gather(*task)
    print('await之后', task)


if __name__ == "__main__":
    # print(main())
    asyncio.run(main())
