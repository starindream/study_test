import asyncio


async def compute(x, y):
    print('计算x +y => {0}+{1}'.format(x, y))
    await asyncio.sleep(3)
    return x + y


async def get_sum(x, y):
    rest = await compute(x, y)
    print('{0} + {1} = {2}'.format(x, y, rest))

# 拿到事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(get_sum(1, 2))
loop.close()
