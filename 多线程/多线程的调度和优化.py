import multiprocessing.dummy
import threading
import time
from multiprocessing.dummy import Pool
from concurrent.futures import ThreadPoolExecutor


def run(n):
    """ 线程要做的事 """
    time.sleep(2)
    print(f'线程状态：{threading.current_thread().daemon}')
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
    pool = multiprocessing.dummy.Pool(10)
    thread_list = range(100)  # 多个线程需要处理的数据，即有指定需要多少个线程来进行处理
    print('pool模块执行之前')
    res = pool.map(run, thread_list)  # run：处理数据需要做的事情；thread_list：需要线程处理的数据，需要执行的线程数
    print('pool模块执行之后')
    print('res =>', res)
    # pool.close()  # 关闭线程池，防止继续往线程池中添加任务
    # pool.join()  # 阻塞主线程，等待子线程完成再运行
    print('结束代码')


def main_use_executor():
    pool = ThreadPoolExecutor(max_workers=10)
    thread_list = range(100)
    result = pool.map(run, thread_list)
    # pool.shutdown(wait=True)
    print('result=>', result)
    print('结束代码')


# 使用 ThreadExecutor 的 with 方式来创建线程
def main_use_executor_with():
    with ThreadPoolExecutor(max_workers=10) as executor:
        thread_list = range(100)
        result = executor.map(run, thread_list)
        print(result)
    # 线程结束后，获取result
    # for one in result:
    #     print('one', one)


# for 循环阻塞主线程，且executor返回的迭代器中的顺序跟传入的urls的顺序一致，不会受线程的结束时间而影响，导致的重新排序。
def test():
    # 参数times用来模拟网络请求时间
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times

    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4]
    result = executor.map(get_html, urls)
    print(result)
    for data in result:
        print("in main:get page {}s success".format(data))


if __name__ == '__main__':
    # main()
    # main_use_thread()
    # main_use_pool()
    # main_use_executor()
    # test()
    main_use_executor_with()
    print('主线程结束')
