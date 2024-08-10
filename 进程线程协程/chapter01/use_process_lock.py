import random
from multiprocessing import Process, Lock, RLock

import time


class WriteProcess(Process):
    """ 写入文件 """

    def __init__(self, file_name, num, lock, *args, **kwargs):
        # 文件的名称
        self.file_name = file_name
        self.num = num
        # 锁对象
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        """ 写入文件的主要业务逻辑 """
        with self.lock:
        # try:
        #     # 添加锁
        #     self.lock.acquire()
        #     print('locked')
        #     self.lock.acquire()
        #     print('relocked')
            for i in range(5):
                content = '现在是： {0} : {1} - {2} \n'.format(
                    self.name,
                    self.pid,
                    self.num
                )
                with open(self.file_name, 'a+', encoding='utf-8') as f:
                    f.write(content)
                    time.sleep(random.randint(1, 5))
                    print(content)
        # finally:
        #     # 释放锁
        #     self.lock.release()
        #     self.lock.release()


if __name__ == '__main__':
    file_name = 'test.txt'
    # 所的对象
    lock = RLock()
    for x in range(5):
        p = WriteProcess(file_name, x, lock)
        p.start()
