import random
import time

from concurrent.futures import ThreadPoolExecutor


def run(id):
    num = random.randint(2, 5)
    print(f'当前线程{id},阻塞{num}')
    time.sleep(num)
    print(f'完成线程{id},被阻塞{num}')


with ThreadPoolExecutor(max_workers=1) as executor:
    executor.map(run, range(10))
