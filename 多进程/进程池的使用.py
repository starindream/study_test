import time
from multiprocessing import Pool,current_process


def func(n):
    print(f'进程状tai：{current_process().daemon}')
    print('值：',n)
    print(n * n)


if __name__ == '__main__':
    p = Pool(4)
    ls = range(10)
    # p.map(func, ls)
    for i in ls :
        p.apply_async(func,(2,))
    for n in range(10):
        p.apply_async(func,(n,))
    p.close()
    p.join()
    # print('jincheng')
    # time.sleep(2)
    # for i in range(5) :
    #     p.apply_async(func,(i,))
    # p.close()
    # p.join()
    print('进程结束')
