class Father:
    num = 0

    def __init__(self):
        print(self.text, self)


class Children(Father):
    text = '你好'


c = Children()
Father.num = 2
print(c.num)
c.num = 5
Children.num = 8
print(Children.num)
print(c.num)
print(Father.num)

# 总结：对于父类中的类变量，子类本身及其实例都能获取，但是修改的话，都是在实例或本身中进行修改，而不是修改父类的变量。
# 当 子类的实例修改了，但子类的并不会修改还是沿用父类的类变量
