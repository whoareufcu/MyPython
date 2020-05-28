from functools import reduce


def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, L)
print(list(r))


def add(x, y):
    return x + y


sum = reduce(add, L)
print("reduce求和：" + str(sum))

# 把str转换为int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int("123445"))


# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    # return name[0].upper() + name[1:].lower()
    return name.title()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    i = s.index(".")

    def str1(s):
        print("去掉小数点：" + str(s[:i] + s[i + 1:]))
        return str(s[:i] + s[i + 1:])

    def str2num(s):
        return DIGITS[s]

    return reduce(lambda x, y: x * 10 + y, map(str2num, str1(s))) / (10 ** i)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
