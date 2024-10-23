# 结论：类变量，可以被所有实例变量和类本身使用，且修改是全局的，当修改了类变量后，下一次新定义的实例，会引用最新修改后的类变量。
# 修改类变量时：通过类来修改，是修改类变量本身，如果通过实例来修改，则是在实例中创建了一个同类变量相同的变量。
# 查找时，会是先查找实例中是否有该变量，没有该变量，会查找类变量中是否有，但赋值时，是在实例中新建相同名称的变量

class Base:
    num = 5

    @classmethod
    def update_num(cls):
        cls.num += 1
        return cls.num

    @classmethod
    def get_class_num(cls):
        return cls.num

    def get_num(self):
        return self.num

    def set_num(self):
        self.num += 1
        return self.num


if __name__ == '__main__':
    b = Base()
    print(b.update_num())
    print(b.set_num())
    print(b.set_num())
    print(b.get_num())
    print('get_class_num', b.get_class_num())
    print(Base.num)
    c = Base()
    print(c.num)
    print(Base.num)
