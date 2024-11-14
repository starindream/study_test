import os
import time
from multiprocessing import Process, Queue


def put_in_process(q):
    info = f'{os.getpid()},put:{time.asctime()}'
    q.put(info)
    print("\033[31m" + 'put', info)


# 可能会出现打印出来的put的顺序和get的顺序不一致的问题
# 问题点可能在于，每个进程执行的速度不同，可能会收到CPU的负载，I/O操作的延迟等多种因素。
# 可能A、B进程都在毫秒级的先后添加数据，可能B进程稍快一些先行加入了队列，随后A进程也加入了队列。
# 但是在print的过程中，A进程先行结束，这样便导致先打印的A在打印的B,但实际上队列中是B在A前
def get_in_process(q):
    info = q.get()
    print("\033[32" + 'mget', info)


if __name__ == '__main__':
    ls_one = []
    ls_two = []
    q = Queue()
    for i in range(10):
        p = Process(target=put_in_process, args=(q,))
        p.start()
        ls_one.append(p)

    for i in range(10):
        p = Process(target=get_in_process, args=(q,))
        p.start()
        ls_two.append(p)

    # 将所有子进程都进行join，主要目的是join住运行时间最长的子进程，使得主进程可以等待所有子进程结束
    for process in ls_one:
        process.join()

    for process in ls_two:
        process.join()
