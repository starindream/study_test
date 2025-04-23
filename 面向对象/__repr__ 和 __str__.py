"""
    总结：__str__ 和 __repr__ 都是描述对象的字符串，不过应用场景不同
"""

class Cat:

    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        dic = {
            'text': '文字'
        }
        return dic[item]

    def __repr__(self):
        """
         repr 为对象提供官方字符串，反映出当前对象的状态和重要的属性
         repr 通常通过 repr 函数来调用对象的 __repr__，当对象没有定义 __str__ 时，使用print也会调用 __repr__
        """
        return f'名字：{self.name}'

    def __str__(self):
        """
         str 为对象提供 非正式 字符串，主要用一种易于理解的方式呈现对象的内容
         __str__ 通过 str 函数 和 print 函数调用时，会触发对象的 __str__ 函数
        """
        return f"str名字:{self.name}=》str"


c = Cat('星')

print(c)
print(repr(c))
