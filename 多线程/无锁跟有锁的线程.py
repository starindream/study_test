import threading
import time

lock = threading.RLock()
count = 0


class MyThread(threading.Thread):
    def __init__(self, target, number):
        super().__init__()
        self.number = number
        self.target = target

    def run(self):
        self.target(self.name, self.number)


def have_lock(name, number):
    global count
    num = 0
    while num < number:
        num += 1
        lock.acquire()
        count += 1
        time.sleep(1)
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {name}")
        lock.release()


def no_lock(name, number):
    global count
    num = 0
    while num < number:
        num += 1
        # lock.acquire()
        count += 1
        time.sleep(1)
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {name}")
        # lock.release()


if __name__ == '__main__':
    thread_one = MyThread(have_lock, 4)
    thread_two = MyThread(no_lock, 5)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
