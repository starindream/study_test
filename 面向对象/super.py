"""
结论：传入super的 cls 和 self，必须是处于继承关系，且cls 必须是 self 的父类或本类，
因为原理是通过 self 的创建类，找到 mro 列表，然后在 mro 类表中找到传入 cls 的类的后一个类，再调用后一个类的方法。
"""


class Cat:
    test = 1

    def __init__(d):
        print('Cat')

    @classmethod
    def get_filter(cls, key):
        print(getattr(cls, key))
        # pass


class BlackCat(Cat):
    def __init__(self):
        print('BlackCat')


class BlackChildCat(BlackCat):
    def __init__(self):
        print('BlackChildCat')
        super(BlackCat, self).__init__()


class Dog:
    def __init__(self):
        print('Dog')


class WhiteDog(Dog):
    def __init__(self):
        print('WhiteDog')


class WhiteDogChild(WhiteDog):
    def __init__(self, cls, slf):
        print('WhiteDogChild')
        super(cls, slf).__init__()


def cat_fn():
    cat = BlackChildCat()


def dog_fn():
    # 结论：传入super的 cls 和 self，必须是处于继承关系，且cls 必须是 self 的父类或本类，
    # 因为原理是通过 self 的创建类，找到 mro 列表，然后在 mro 类表中找到传入 cls 的类的后一个类，再调用后一个类的方法。
    # cat = BlackChildCat()
    # dog = WhiteDogChild(WhiteDogChild, cat)
    cat = Cat()
    dog = WhiteDogChild(BlackChildCat, cat)


if __name__ == "__main__":
    # cat_fn()
    # dog_fn()
    # print(Cat.get_filter('test'))
    d = {
        'test': 1
    }
    print(getattr(Cat, 'test'))
    print(getattr(d, 'test'))
