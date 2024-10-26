import asyncio


async def one():
    print('one开始')
    await asyncio.sleep(5)
    print('one结束')


async def two():
    print('two开始')
    await asyncio.sleep(3)
    print('two结束')


async def main():
    await one()
    await two()


async def main_task():
    task1 = asyncio.create_task(one())
    task2 = asyncio.create_task(two())
    print('create_task之后')
    # await task1
    # await task2


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(main_task())
