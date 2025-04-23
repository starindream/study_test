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
    print('task1执行完毕', task.result())


async def main():
    # task = []
    # 注意：此处只是让事件调度立即执行one协程，但此时事件循环正在执行当前函数，需要等当前函数执行完毕，才能轮到one协程执行。
    task1 = asyncio.create_task(one())  # 创建task任务，跟踪协程的状态，并且快速调用one对应的协程函数。
    # task1.add_done_callback(callback)
    task2 = asyncio.create_task(two())
    print('CREATE_TASK之后')
    # task.append(task1)
    # task.append(task2)
    # print('task1', task1)
    # await one()

    # 上方没有使用await，都是同步执行
    # 阻塞函数执行，等待所有的异步函数结束后，在结束main函数，让run方法中的事件调度关闭。
    # await task1
    # print('await task1 之后')
    # await task2

    # 方法一，传入task对象
    # await asyncio.gather(*task)  # 等待所有协程执行完毕，才会继续往下执行。

    # 方法二，传入异步函数，内部来创建task对象
    # await asyncio.gather(one(), two())

    ls = [item() for item in [one, two]]
    results = await asyncio.gather(*ls)
    for result in results:
        print('result', result)


if __name__ == '__main__':
    # 为什么需要传入异步函数 main
    # 因为需要通过run来确定什么时候结束时间调度，当main异步函数结束后，便会关闭事件调度
    print('run前')
    asyncio.run(main())
    print('run后')
    print('主线程')
