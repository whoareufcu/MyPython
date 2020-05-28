class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Student object (name:%s)" % self.__name

    def __getattr__(self, item):
        if item == "score":
            return 99
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self, *args, **kwargs):
        print("My name is %s" % self.__name)


s = Student("Joe")
print(s)


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 1000:
            raise StopIteration()
        return self.__a


for f in Fib():
    print(f)

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性

print("调用不存在的属性：%s" % s.score)
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，
# 我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
s()
