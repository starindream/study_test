import random
from multiprocessing import Process, Queue, Condition, current_process, Manager

import time
from multiprocessing.pool import Pool


class Bread(object):
    """ 馒头类 """
    def __init__(self, name):
        # 馒头的名称
        self.name = name

    def __str__(self):
        return self.name


class ProducerProcess(Process):
    """ 生产者进程 """

    def __init__(self, basket, counter, lock, *args, **kwargs):
        """
        :param basket: 容器，用于存放馒头
        :param counter: int 馒头的编号
        :param lock: 进程锁
        """
        self.basket = basket
        self.counter = counter
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            with self.lock:
                # 判断容器是否已经满了
                if self.basket.full():
                    print('#####馒头生产满了####')
                    # 暂停自己
                    self.lock.wait()
                    # 唤醒他人
                    self.lock.notify_all()
                else:
                    # 生产馒头
                    name = '{0}-{1}-{2}'.format(self.name, self.pid, self.counter)
                    bread = Bread(name)

                    # 馒头计数+1
                    self.counter += 1

                    # 添加到容器
                    self.basket.put(bread)

                    time.sleep(random.randint(1, 5))
                    print('>> 生产馒头：{0}，总共{1}个'.format(name, self.basket.qsize()))


def run_producer(lock, counter, basket):
    while True:
        with lock:
            # 判断容器是否已经满了
            if basket.full():
                print('#####馒头生产满了####')
                # 暂停自己
                lock.wait()
                # 唤醒他人
                lock.notify_all()
            else:
                now_process = current_process()
                # 生产馒头
                name = '{0}-{1}-{2}'.format(
                    now_process.name, now_process.pid, counter)
                bread = Bread(name)

                # 馒头计数+1
                counter += 1

                # 添加到容器
                basket.put(bread)

                time.sleep(random.randint(1, 5))
                print('>> 生产馒头：{0}，总共{1}个'.format(name,
                                                  basket.qsize()))


class ConsumerProcess(Process):
    """ 消费者进程 """

    def __init__(self, basket, lock, *args, **kwargs):
        """
        :param basket: 容器，用于存放馒头
        :param lock: 进程锁
        """
        self.basket = basket
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            with self.lock:
                # 判断是否有馒头可以被消费
                if self.basket.empty():
                    print('@@@@馒头已经消费完了@@@@')
                    # 暂停自己
                    self.lock.wait()
                    # 唤醒他人
                    self.lock.notify_all()
                else:
                    # 消费生产者生产的馒头
                    bread = self.basket.get()

                    time.sleep(random.randint(1, 5))
                    print('<< 消费馒头：{0}，总共{1}个'.format(bread, self.basket.qsize()))


if __name__ == '__main__':
    manager = Manager()
    # 锁
    lock = manager.Condition()
    counter = 0   # 馒头的编号
    # 一个用于存放馒头的容器，容量为10
    basket = manager.Queue(maxsize=5)

    # 启动生产者
    pool_producer = Pool(5)
    for i in range(10):
        rest = pool_producer.apply_async(run_producer, args=(lock, counter, basket))
        print(rest)
    pool_producer.close()

    # 启动消费者
    consumer = ConsumerProcess(basket, lock)
    consumer.start()
    pool_producer.join()
    # producer.join()
    consumer.join()