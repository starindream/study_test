# 线程的作用：常运用大量的I/O 操作
# 创建多个线程在同时打印a、b

import threading
import time


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
    print(f'线程开始{thread_name}')
    num = 0
    while num < number:
        time.sleep(1)
        num += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {thread_name} 输出 {letter}")


if __name__ == '__main__':
    thread_one = MyThread(4, 'a')
    thread_two = MyThread(3, 'b')
    thread_one.daemon = True
    thread_one.start()
    thread_two.daemon = True
    thread_two.start()
    print('join')
    # thread_one.join()
    # thread_two.join()
    print('join 之后')
