import time
from multiprocessing import Process,current_process

# 问题点：守护进程是父进程结束则关闭还是所有进程结束再关闭
# 方案：主进程不关闭，父进程关闭
# 结论：守护进程是跟随父进程关闭而强制终止的

def daemon_process():
    # 守护进程一直运行
    while True:
        time.sleep(1)
        print('守护进程',current_process().daemon)

def use_process():
    children_process = Process(target=daemon_process)
    children_process.daemon = True
    children_process.start()
    # children_process.join()
    # time.sleep(3)
    # children_process.terminate() # 3秒之后结束进程，看守护进程能否仅需运行

if __name__ == '__main__':
    p = Process(target=use_process)
    p.start()
    p.join()
    print('子进程执行完毕')
    time.sleep(30)
    print('主线程结束')

