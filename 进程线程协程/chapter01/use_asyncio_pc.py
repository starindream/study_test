import random
from queue import Queue

import asyncio


class Bread(object):
    """ 馒头类 """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


async def consumer(name, basket, lock):
    """
    消费者
    :param name  协程的名称
    :param basket  篮子，用于存放馒头
    :return:
    """
    while True:
        with await lock:
            # 如果没有馒头了，则自己休息，唤醒生产者进行生产
            if basket.empty():
                print('{0}@@@消费完了@@@'.format(name))
                # 唤醒他人
                lock.notify_all()
                # 休息
                await lock.wait()
            else:
                # 取出馒头
                bread = basket.get()
                print('>>{0} 消费馒头 {1}, size: {2}'.format(
                    name, bread, basket.qsize()
                ))
                await asyncio.sleep(random.randint(1, 5))


async def producer(name, basket, lock):
    """
    生产者
    :param name  协程的名称
    :param basket  篮子，用于存放馒头
    :return:
    """
    print('{0} 开始生产'.format(name))
    while True:
        with await lock:
            # 馒头生产满了，休息生产者，唤醒消费者进行消费
            if basket.full():
                print('{0} 生产满了'.format(name))
                # 唤醒他人
                lock.notify_all()
                # 自己休息
                await lock.wait()
            else:
                # 馒头的名字
                bread_name = '{0}_{1}'.format(name, basket.counter)
                bread = Bread(bread_name)
                # 将馒头放入篮子
                basket.put(bread)
                print('>>{0} 生产馒头 {1}, size: {2}'.format(name, bread_name, basket.qsize()))
                # 计数+ 1
                basket.counter += 1
                await asyncio.sleep(random.randint(1, 2))


class Basket(Queue):
    """ 自定义的仓库 """
    # 馒头生产的计数器
    counter = 0


def main():
    lock = asyncio.Condition()
    # 篮子，用于放馒头，协程通信使用
    basket = Basket(maxsize=5)
    p1 = producer('P1', basket, lock)
    p2 = producer('P2', basket, lock)
    p3 = producer('P3', basket, lock)
    c1 = consumer('C1', basket, lock)
    c2 = consumer('C2', basket, lock)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(p1, p2, p3, c1, c2))
    loop.close()


if __name__ == '__main__':
    main()