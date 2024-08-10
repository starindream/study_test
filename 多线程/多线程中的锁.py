# 线程的作用：常运用大量的I/O 操作
# 创建多个线程在同时打印a、b

import threading
import time

count = 0
# lock = threading.Lock()
lock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self, number, letter):
        super().__init__()
        self.number = number
        self.letter = letter

    def run(self):
        task(self.name, self.number, self.letter)

    def __del__(self):
        print("【线程销毁释放内存】", self.name)


def task(thread_name, number, letter):
    global count
    print(f'线程开始{thread_name}')
    num = 0
    while num < number:
        lock.acquire()
        lock.acquire()
        print(f'开始锁,线程名称{thread_name}')
        count += 1
        time.sleep(1)
        num += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        lock.release()
        lock.release()
        print(f'结束锁,线程名称{thread_name}')
        print(f"[{current_time}] {thread_name} 输出 {letter}")


if __name__ == '__main__':
    thread_one = MyThread(4, 'a')
    thread_two = MyThread(3, 'b')
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
