import time
import asyncio


async def one():
    print('one start')
    await asyncio.sleep(2)
    print('one end')
    return 'hello one'


async def two():
    print('two start')
    await asyncio.sleep(3)
    print('two end')


def callback(task):
    print('task1执行完毕',task.result())

async def main():
    task = []
    # 注意：此处只是让事件调度立即执行one协程，但此时事件循环正在执行当前函数，需要等当前函数执行完毕，才能轮到one协程执行。
    task1 = asyncio.create_task(one())  # 创建task任务，跟踪协程的状态，并且快速调用one对应的协程函数。
    task1.add_done_callback(callback)
    task2 = asyncio.create_task(two())
    task.append(task1)
    task.append(task2)
    print('task1', task1)

    # 上方没有使用await，都是同步执行
    # 阻塞函数执行
    # await task1
    # await task2

    await asyncio.gather(*task)  # 等待所有协程执行完毕，才会继续往下执行。


if __name__ == '__main__':
    asyncio.run(main())
    print('主线程')    
