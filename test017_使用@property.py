class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self, vale):

        if not isinstance(vale, int):
            raise ValueError("score must be an integer!")
        if vale < 0 or vale > 100:
            raise ValueError("'score must between 0 ~ 100!")
        self.__score = vale


s = Student()
s.set_score(60)
print(s.get_score())


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Teacher(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
t = Teacher()
t.score = 70  # OK，实际转化为s.set_score(60)
print(t.score)  # OK，实际转化为s.get_score()


class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth


# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
s2 = Student2()
s2.birth = 1992
print("年龄：%s" % s2.age)


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, vale):
        self.__width = vale

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')