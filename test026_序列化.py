# Python提供了pickle模块来实现序列化。
import json
import pickle

d = dict(name="Bob", age=20, score=88)
pickle.dumps(d)


# 写入文件
def writeInTxt():
    with open(r"D:\mypy1\IO\dump.txt", "wb") as f:
        pickle.dump(d, f)
        print("写入成功")


# writeInTxt()
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

def readInTxt():
    with open(r"D:\mypy1\IO\dump.txt", "rb") as f:
        d = pickle.load(f)
        print(d)


# readInTxt()
# 我们先看看如何把Python对象变成一个JSON：

def dictToJson():
    d = dict(name="Joe", age=19, score=77)
    s = json.dumps(d)
    print("dict2json: ", s)


# dictToJson()

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化：

def json2Dict():
    str_json = '{"name": "Joe", "age": 19, "score": 77}'
    d2 = json.loads(str_json)
    print("json2dict: ", d2)


# json2Dict()
# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，
# 比如定义Student类，然后序列化：

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("WW", 1, 11)


# print(json.dumps(s))
# 运行代码，毫不留情地得到一个TypeError：
# 错误的原因是Student对象不是一个可序列化为JSON的对象。
# 如果连class的实例对象都无法序列化为JSON，这肯定不合理！
# 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，
# dumps()方法还提供了一大堆的可选参数：
# https://docs.python.org/3/library/json.html#json.dumps
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# 我们只需要为Student专门写一个转换函数，再把函数传进去即可：

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


d3 = json.dumps(s, default=student2dict)
print("Student序列化：", d3)
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
d4 = json.dumps(s, default=lambda obj: obj.__dict__)
print('Student序列化2：', d4)


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# 反序列化
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2Student(dic):
    return Student(dic['name'], dic['age'], dic['score'])


print('反序列化：', json.loads(d3, object_hook=dict2Student))

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print('练习：', s)
