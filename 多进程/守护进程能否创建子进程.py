import threading
from multiprocessing import Process
from threading import Thread


# 结论：守护进程不允许创建子进程

def run():
    print('run')


def create_process():
    p = Process(target=create_process)
    p.start()


def create_daemon():
    p = Process(target=create_process)
    p.daemon = True
    p.start()
    p.join()


def create_thread():
    thread = Thread(target=run)
    print('create_thread', threading.current_thread().daemon)
    thread.start()
    thread.join()


def create_daemon_thread():
    thread = Thread(target=create_thread)
    thread.daemon = True
    thread.start()
    thread.join()
    print('结束代码')


if __name__ == '__main__':
    create_daemon() # 守护进程
    # create_daemon_thread() # 守护线程
