class Cat:
    def __init__(self, name):
        self.name = name

    def method(self):
        return self.name

    # __getitem__ 让对象可以通过 [] 语法来调用，并且所有 [] 中包裹的参数，都会报整合为一个元组传递到 __getitem__ 的第一个参数中。
    # 获取到参数后，可以通过 self 实例来返回需要的数据
    def __getitem__(self, item):
        print(item)


c = Cat('你好')
c[{'a': 1}, {'b': 2}, '1']
