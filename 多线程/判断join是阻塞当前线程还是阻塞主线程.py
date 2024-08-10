import time
import threading
from concurrent.futures import ThreadPoolExecutor


# 结论：会阻塞当前线程，及当前线程的父级线程，因为阻塞了当前线程，当前线程不结束，则会阻塞父级线程，一直向上传递。

# 使用原生的thread模块
def children_main(n):
    time.sleep(3)
    print('children', n)


# 使用原生的thread模块
def parent_main(n):
    time.sleep(2)
    print('parent', n)
    thread_list = []
    for i in range(20):
        thread = threading.Thread(target=children_main, args=(i,))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()
        thread.join()

# 使用原生的thread模块
def use_thread():
    time_start = time.time()
    for count in range(1):
        ls = range(10)
        thread_list = []
        for i in ls:
            thread = threading.Thread(target=parent_main, args=(i,))
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()
    print('用时', time.time() - time_start)


def children_executor(n):
    time.sleep(2)
    print('children_executor', n)


def parent_excutor(n):
    time.sleep(2)
    with ThreadPoolExecutor(max_workers=10) as executor:
        ls = range(50)
        executor.map(children_executor, ls)
    print('parent_excutor', n)


def main_use_executor():
    time_start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        ls = range(50)
        executor.map(parent_excutor, ls)
    print('结束时间', time.time() - time_start)


if __name__ == '__main__':
    # use_thread()
    main_use_executor()
    print('主线程结束')
