import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def run(params):
    # print('params', params)
    time.sleep(2)
    # print('run')
    return params


def main():
    pool = ThreadPoolExecutor(max_workers=10)
    future = pool.submit(run, [1, 2])
    # print('result', future.result())
    futures = [pool.submit(run, i) for i in range(10)]
    result = as_completed(futures)
    for i in result:
        print(i)
        print('结果:', i.result())


if __name__ == '__main__':
    main()
    print('主线程结束')
