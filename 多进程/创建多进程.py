import os
import time
from multiprocessing import Process

n = 1
ls = []

print('执行代码')


class MyProcess(Process):
    # def __init__(self, name):
    #     super().__init__()
    #     self.name = name

    def run(self):
        
        print(f'我是{self.name}子进程为{os.getpid()};父进程为{os.getppid()}',n)
        # class_my_process()


def class_my_process():
    time.sleep(2)
    print('class_my_process')


def sun_my_process():
    time.sleep(2)


def use_process():
    time.sleep(2)
    print('use_process', n)
    ls.append('1')
    p = Process(target=sun_my_process)
    p.start()
    p.join()
    print('子进程中的ls',ls)
    # os._exit(0)  # 退出子进程


def create_process():
    p = Process(target=use_process)
    p.start()
    p.join()
    # os._exit(0)  # 退出父进程
    print('退出终端')


def test():
    print(a)

if __name__ == '__main__':
    a = 1
    create_process()
    p_one = MyProcess(name='p_one')
    p_two = MyProcess(name='p_two')
    p_three = MyProcess(name='p_three')

    # p_one.start()
    # p_two.start()
    # 这里只是调用了实例的方法，没有创建新的进程，进程的创建需要涉及操作系统的调度、内存分配、进程初始化等操作，因此比直接调用run方法慢，而进程的创建是在start中进行的
    # p_three.run()

    # p_one.join()
    # p_two.join()
    # p_three.join()

    print(p_one.name)
    print(p_two.name)
    print(p_three.name)
    test()
    print(ls)

    print('主进程结束')
