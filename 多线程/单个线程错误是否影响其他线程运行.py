from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def run(i):
    if i % 2 == 0:
        raise NotImplementedError
    print(i)
    return i


def main():
    # with ThreadPoolExecutor(max_workers=20) as executor:
    #     ls = range(0, 10)
    #     futures = as_completed([executor.submit(run, i) for i in ls])
    #     for future in futures:
    #         print(future.result())
    executor = ThreadPoolExecutor(max_workers=20)
    ls = range(0, 10)
    futures = as_completed([executor.submit(run, i) for i in ls])
    for future in futures:
        print(future.result())


if __name__ == "__main__":
    main()
    print([i for i in range(0, 10)])
