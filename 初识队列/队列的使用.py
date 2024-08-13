import time
from multiprocessing import Process, Queue


def set_queue(q):
    q.put('1')
    q.put('2')
    q.put('3')
    print('结束set', q.full())


def get_queue(q):
    print('get_queue')
    print(q.get())
    print('get中间', q.full())
    print(q.get())
    print(q.get())
    # print(q.get()) # 队列中没有值了，已经被取空了，此时会阻塞，等待队列中放入值，在取出运行,可以通过参数来配置，等待多少秒后，还获取不到数据就抛出错误
    # q.get_nowait() # 功能同get相同，只不过在获取不到数据后，立马抛出错误
    print('结束get_queue', q.full())


def use_process(q):
    ls = {'name': 'lose', 'age': 18}
    time.sleep(1)
    q.put(ls)


if __name__ == '__main__':
    q = Queue(3)
    print('运行')
    set_queue(q)
    get_queue(q)
    p = Process(target=use_process, args=(q,))
    p.start()
    value = q.get()
    print('value', value)
    print('主进程运行结束')
