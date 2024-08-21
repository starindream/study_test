import time
import threading

# 父线程结束，守护线程是否会强制结束
# 结论：父线程结束，子线程不会结束，同样守护线程也不会跟随父线程终止而强制终止，只有当进程结束后，才会终止守护线程。

def test():
    print(f'test {threading.current_thread().daemon}')

def func():
    t = threading.Thread(target=test)
    t.start()
    while True:
        time.sleep(1)
        print(f'线程状态 {threading.current_thread().daemon}')

def children_thread():
    t = threading.Thread(target=func)
    t.daemon = True
    t.start()
    
    # t.join()

if __name__ == '__main__':
    t = threading.Thread(target=children_thread)
    t.start()
    # t.join()
    print('children线程结束')
    time.sleep(30)