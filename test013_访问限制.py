class Student(object):
    def __init__(self, name, sore):
        self.__name = name
        self.__sore = sore

    def print_msg(self):
        print("%s:%s" % (self.__name, self.__sore))

    # 提供方法使外部代码可以访问内部的私有变量
    def get_name(self):
        return self.__name

    def get_sore(self):
        return self.__sore

    # 提供方法使外部代码可以修改内部的私有变量
    def set_name(self, name):
        self.__name = name

    def set_sore(self, sore):
        if 0 <= sore <= 100:
            self.__sore = sore
        else:
            raise TypeError("bad sore")


bart = Student("Joe", 12)
bart.print_msg()
# print("无法从外部访问实例变量：%s" % bart.__name)

# 如果外部代码需要获取实例变量：
print("通过内部方法从外部访问实例变量：%s %s" % (bart.get_name(), bart.get_sore()))

bart.set_name("Albus")
bart.set_sore(89)
print("修改后的私有变量：%s %s" % (bart.get_name(), bart.get_sore()))
# bart.set_sore(101)


# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student1('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')