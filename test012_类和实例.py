class Student(object):
    pass


bart = Student()
print("类： %s" % Student)
print("实例： %s" % bart)
bart.name = "Joe"
print("姓名：%s" % bart.name)


class Student1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_msg(self):
        print("%s:%s" % (self.name, self.age))


bart1 = Student1("Albus", 18)
print("姓名：%s" % bart1.name)
print("年龄：%s" % bart1.age)
bart1.print_msg()
