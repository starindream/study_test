import os
import time
from multiprocessing import Process


def do_sth(name):
    """
    进程要做的事情
    :param name: str 进程的名称
    """
    print('进程的名称：{0}， pid: {1}'.format(name, os.getpid()))
    time.sleep(150)
    print('进程要做的事情')


class MyProcess(Process):

    def __init__(self, name, *args, **kwargs):
        self.my_name = name
        # print(self.name)
        super().__init__(*args, **kwargs)
        print(self.name)

    def run(self):
        print('MyProcess进程的名称：{0}， pid: {1}'.format(
            self.my_name, os.getpid()))
        time.sleep(150)
        print('MyProcess进程要做的事情')


if __name__ == '__main__':
    # p = Process(target=do_sth, args=('my process', ))
    p = MyProcess('my process class')
    # 启动进程
    p.start()
    # 挂起进程
    p.join()
