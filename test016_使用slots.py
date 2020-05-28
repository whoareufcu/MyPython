class Student(object):
    pass


# 给实例绑定一个属性
s = Student()
s.name = "Michael"
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


# 给实例绑定的方法对另一个实例是不起作用的
# 为了给所有的实例都绑定方法，可以给class类绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)

print(s.score)


# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Teacher(object):
    __slots__ = ("name", "age")


t = Teacher()
t.name = "Joe"
t.score = 11
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

