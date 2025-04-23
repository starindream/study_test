from datetime import datetime

"""
    总结：
    1、生成器函数首次调用会返回一个生成器
    2、通过 next 调用这个生成器，会执行函数到 yield ，如果没有返回值或循环调用，则在下一次执行 next 会直接报错。
"""


def gener():
    while True:
        print('while loop start')
        yield datetime.now().replace(hour=12, minute=12)
        return 2


def new_gen():
    yield 1


gen = gener()

# print(gen)
# result = next(gen)
# print(result)
# result = next(gen)
# print(result)
# result = next(gen)
# print(result)


g = new_gen()

for i in g:
    print(i)
