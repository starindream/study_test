from concurrent.futures import ThreadPoolExecutor
from contextvars import ContextVar
import time

val = ContextVar('val', default=0)


def first_fn():
    print('first_fn', val.get())


def first_task():
    print(f'first修改前{val.get()}')
    val.set('first')
    time.sleep(2)
    print(f'first修改后{val.get()}')
    first_fn()


def second_task():
    print(f'second修改前{val.get()}')
    val.set('second')
    time.sleep(1)
    print(f'second修改后{val.get()}')


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(first_task)
        future2 = executor.submit(second_task)
        # l = [future1, future2]
        # for i in l:
        #     print(i.result())
        print('main', val.get())


if __name__ == "__main__":
    main()
    print('主线程', val.get())
