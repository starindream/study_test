import time
import threading
from multiprocessing import Process,current_process

# 问题：进程中产生的线程是根据当前进程关闭而关闭，还是所有的进程关闭而关闭
# 结论：
#   1、一个进程的生命周期依赖于它的所有线程，只有当进程中的所有线程都结束后，进程才会结束，所以，虽然子进程代码执行完毕了，但内部的线程还在运行，进程也就没有结束。
#   2、守护线程会在其他非守护线程结束后，才会结束。
#   3、当一个进程关闭后，他内部的所有线程也会自动关闭。

def thread_run():
    while True:
        time.sleep(1)
        print(f'thread：{threading.current_thread().daemon}')

def create_thread():
    t = threading.Thread(target=thread_run)
    # t.daemon = True
    t.start()
    # t.join()
    print('子进程结束')

if __name__ == '__main__':
    p = Process(target=create_thread)
    p.start()
    time.sleep(3)
    p.terminate() # 关闭子进程
    # p.join()
    print('主进程结束')
