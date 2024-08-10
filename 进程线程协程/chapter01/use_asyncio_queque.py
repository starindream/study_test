# 1. 定义一个队列
# 2. 让两个协程来进行通信
# 3. 让其中一个协程往队列中写入数据
# 4. 让另一个协程从队列中删除数据

import asyncio
import random


async def add(store, name):
    """
    写入数据到队列
    :param store: 队列的对象
    :return:
    """
    for i in range(5):
        # 往队列中添加数字
        num = '{0} - {1}'.format(name, i)
        await asyncio.sleep(random.randint(1, 5))
        await store.put(i)
        print('{2} add one ... {0}, size: {1}'.format(
            num, store.qsize(), name))


async def reduce(store):
    """
    从队列中删除数据
    :param store:
    :return:
    """
    for i in range(10):
        rest = await store.get()
        print(' reduce one.. {0}, size: {1}'.format(rest, store.qsize()))


if __name__ == '__main__':
    # 准备一个队列
    store = asyncio.Queue(maxsize=5)
    a1 = add(store, 'a1')
    a2 = add(store, 'a2')
    r1 = reduce(store)

    # 添加到事件队列
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(a1, a2, r1))
    loop.close()
