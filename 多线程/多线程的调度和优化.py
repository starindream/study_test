import threading
import time
from multiprocessing.dummy import Pool
from concurrent.futures import ThreadPoolExecutor


def run(n):
    """ 线程要做的事 """
    time.sleep(2)
    print(threading.current_thread().name, n)
    return n


def main():
    start = time.time()
    print("Starting", start)
    # 大概需要200秒来执行
    for i in range(100):
        run(i)
    print(time.time() - start)


# 正常使用thread
def main_use_thread():
    thread_list = []
    time_start = time.time()
    # 一次性添加100 ， 可能会导致线程过多，而电脑性能不支持的情况
    for count in range(10):
        for i in range(10):
            thread = threading.Thread(target=run, args=(i,))
            thread_list.append(thread)
            thread.start()
            # thread.join() 注意：join 会阻塞当前线程进度

        for thread in thread_list:
            thread.join()
    print(time.time() - time_start)  # 20.064146995544434


# 使用进程模块中的线程池
def main_use_pool():
    pool = Pool(10)
    thread_list = range(100)  # 多个线程需要处理的数据，即有指定需要多少个线程来进行处理
    print('pool模块执行之前')
    res = pool.map(run, thread_list)  # run：处理数据需要做的事情；thread_list：需要线程处理的数据，需要执行的线程数
    print('pool模块执行之后')
    print('res =>', res)
    pool.close()  # 关闭线程池，防止继续往线程池中添加任务
    pool.join()  # 阻塞主线程，等待子线程完成再运行
    print('结束代码')


def main_use_executor():
    pool = ThreadPoolExecutor(max_workers=10)
    thread_list = range(100)
    result = pool.map(run, thread_list)
    pool.shutdown(wait=True)
    print('结束代码')


if __name__ == '__main__':
    # main()
    # main_use_thread()
    # main_use_pool()
    main_use_executor()
    print('主线程结束')
