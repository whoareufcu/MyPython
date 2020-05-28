from enum import Enum, unique

# 为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 枚举它的所有成员：

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique
class WeekDays(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# @unique装饰器可以帮助我们检查保证没有重复值。
# 访问这些枚举类型可以有若干种方法：
day1 = WeekDays.Mon
print(day1)
print(WeekDays.Tue)
print(WeekDays["Tue"])
print(WeekDays.Tue.value)
print(day1 == WeekDays.Tue)
print(day1 == WeekDays.Mon)
# 枚举所有成员
for name, member in WeekDays.__members__.items():
    print(name, "--", member, "--", member.value)


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student2('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
