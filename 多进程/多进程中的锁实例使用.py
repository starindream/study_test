import os
import json
import time
import random
from multiprocessing import Process, Lock


# import mymodule


def search():
    # print('__file__',__file__)
    # print('os.path.abspath',os.path.abspath(__file__))
    # print('父级目录',os.path.dirname(os.path.abspath(__file__)))
    script_dirname = os.path.dirname(os.path.abspath(__file__))
    script_abspath = os.path.join(script_dirname, 'db.json')
    print('script_abspath', script_abspath)
    with open(script_abspath, 'r') as f:
        time.sleep(random.random())
        result = json.load(f)
        print('result', result)


def get(n, lock):
    print('lock', lock)
    script_dirname = os.path.dirname(os.path.abspath(__file__))
    script_abspath = os.path.join(script_dirname, 'db.json')
    # 模拟网络请求
    time.sleep(random.random())
    # 锁住进程，防止发生冲突
    lock.acquire()
    with open(script_abspath, 'r+') as f:
        dic = json.load(f)
        print(f'dic{n}',dic)

        if dic['count'] > 0:
            dic['count'] -= 1
            # 将文件指针设置在文件的最前方
            f.seek(0)
            # 从文件指针出将后续的内容进行截断
            f.truncate()
            json.dump(dic, f)
            print(f'抢票成功{n}')
        else:
            print(f'抢票失败{n}')

    # 完成票数修改，释放进程
    lock.release()


def use_process():
    lock = Lock()
    print('process_lock', lock)
    ls = []
    # 10次循环
    for i in range(10):
        p = Process(target=get, args=(i, lock))
        p.start()
        ls.append(p) # 必须要让父进程阻塞，防止父进程结束，清空了内存中的lock实例

    for process in ls:
        process.join()


if __name__ == '__main__':
    # search()
    use_process()
