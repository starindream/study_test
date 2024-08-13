import os
import random
import time
from multiprocessing import Process, Lock


def run(n, lock):
    print(lock,n)
    if not n >= 5:
        print('lock',n)
        lock.acquire()
    print(f'正在运行，id:{os.getpid()}', n)
    time.sleep(random.random())
    print(f'执行完毕，id:{os.getpid()}', n)
    if not n >= 5:
        lock.release()


def create_process():
    # 必须要将锁在父进程中定义并传入子进程中，因为每一个进程都是独立的内存空间，所以在最外层定义的全局变量锁不是同一个对象。
    lock = Lock()
    ls = []
    for i in range(10):
        p = Process(target=run, args=(i, lock))
        p.start()
        ls.append(p)
    # 注意：其实主要join住的是最长的子进程，如果第一个子进程的执行时间最长，则其实后续的都还没有运行至join这一步。
    for process in ls:
        print('join')
        process.join()


if __name__ == '__main__':
    create_process()
