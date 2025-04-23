import asyncio
from contextvars import ContextVar

# val 是一个context全局变量，不同的线程和协程内部的变量不会冲突影响
# 不同的协程之间修改的变量不会影响其他协程的值，线程依然是如此
# flask 中不同route中的request的值不同的道理便是如此。
# 在 aircon-serverce 项目中，便是使用了contextvars来实现在相同的函数中，可以获取到不同路由的request值。文件为输出的变量为 request_provider

val = ContextVar('context', default='0')


# val.set('second')


def first_fn():
    print('first_fn=>', val.get())


async def first():
    print(f'first修改前{val.get()}')
    val.set('first')
    await  asyncio.sleep(2)
    print(f'first修改后{val.get()}')
    first_fn()


async def second():
    print(f'second修改前{val.get()}')
    val.set('second')
    await  asyncio.sleep(1)
    print(f'second修改后{val.get()}')


async def main():
    res = await asyncio.gather(first(), second())
    print(res)
    print('main', val.get())


if __name__ == '__main__':
    asyncio.run(main())
    print('主现场', val.get())
