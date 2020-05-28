# 唯一性检查
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
import os
import random
import secrets
import sys
import time
from collections import Counter


def unique(L):
    if len(L) == len(set(L)):
        print('没有重复的')
    else:
        print('有重复的')


# unique([1, 2, 3, 1])
# unique([1, 2, 3, 4, 5])

# 数字化
# 下面代码将一个整形数转成一个数字化的对象：
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def int2list():
    num = 12345
    list_num = list(map(int, str(num)))
    return list_num


# print(int2list())


# 随机取样
# 下面的例子中，使用 random 库，实现了从列表中随机取样。
def myrandom1():
    my_list = ['a', 'b', 'c', 'd', 'e']
    num_samples = 2
    samples = random.sample(my_list, num_samples)
    print(samples)


def myrandom2():
    secure_random = secrets.SystemRandom()  # creates a secure random object.
    my_list = ['a', 'b', 'c', 'd', 'e']
    num_samples = 2
    samples = secure_random.sample(my_list, num_samples)
    print(samples)


# myrandom1()
# myrandom2()

# 字符串反转
# 下面的代码片段，使用 Python 中 slicing 操作，来实现字符串反转：
# 切片操作一般针对于list tuple这样的有序集合
def reversed():
    my_str = 'ABCDE'
    print(my_str[::-1])


# reversed()


# 首字母大写
# 下面的代码片段，可以将字符串进行首字母大写，使用的是 String 类的 title() 方法：
def str2up():
    my_string = "my name is chaitanya baweja"
    # using the title() function of string class
    new_string = my_string.title()
    print(new_string)


# str2up()


# 取组成字符串的元素
# 下面的代码片段，可以用来找出一个字符串中所有组成他的元素，我们使用的是 set 中只能存储不重复的元素 这一特性：
def temp():
    my_string = "aavvccccddddeee"
    # converting the string to a set
    temp_set = set(my_string)
    # stitching set into a string using join
    new_string = ''.join(temp_set)
    print(new_string)


# temp()


# 重复输出String/List
# 可以对 String/List 进行乘法运算，这个方法，可以使用它们任意倍增。
def repet():
    n = 3  # number of repetitions
    my_string = "abcd"
    my_list = [1, 2, 3]
    print(my_string * n)
    # abcdabcdabcd
    print(my_list * n)


# repet()


# 列表推导式
# 列表推导式提供了一种更优雅的方式处理列表。
# 以下代码片段中，将旧列表中的元素乘以2来创建新的列表：
def original():
    # 列表推导式提供了一种更优雅的方式处理列表。
    # 以下代码片段中，将旧列表中的元素乘以2来创建新的列表：
    original_list = [1, 2, 3, 4]
    new_list = [x * 2 for x in original_list]
    print(new_list)


# original()

# 交换两个变量值
# Python 交换两个变量的值不需要创建一个中间变量，很简单就可以实现：
def exchange():
    a = 1
    b = 2
    a, b = b, a
    print(a, b)


# exchange()


# 字符串拆分
# 使用 split() 方法可以将一个字符串拆分成多个子串，你也可以将分割符作为参数传递进行，进行分割。
def my_split():
    string_1 = "My name is Chaitanya Baweja"
    string_2 = "sample/ string 2"
    print(string_1.split())
    print(string_2.split('/'))


# my_split()


# 字符串拼接
# join()方法可以将字符串列表组合成一个字符串，下面的代码片段中，我使用,将所有的字符串拼接到一起：
def myjoin():
    list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']
    # Using join with the comma separator
    print(','.join(list_of_strings))


# myjoin()


# 回文检测
# 在前面，我们已经说过了，如何翻转一个字符串，所以回文检测非常的简单：
def check():
    my_str = 'abcde'
    if my_str == my_str[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


# check()


# 元素重复次数
# 在Python中，有很多方法可以做这件事情，但是我最喜欢的还是 Counter 这个类。
# Counter会计算每一个元素出现的次数，Counter()会返回一个字典，元素作为key，出现的次数作为 value。
# 我们也可以使用 most_common() 这个方法来获取出现字数最多的元素。
def repeat_times():
    my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']
    count = Counter(my_list)  # defining a counter object
    print(count)  # Of all elements
    # Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
    print(count['b'])  # of individual element
    # 3
    print(count.most_common(1))  # most frequent element
    # [('d', 5)]


# repeat_times()


# 变位词
# 使用Counter的一个很有意思的用法是找变位词：
# 变位词一种把某个词或句子的字母的位置（顺序）加以改换所形成的新词。
# 使用 Counter 得到的两个对象如果相等，则他们是变位词：

def bwc():
    str_1, str_2, str_3 = "acbde", "abced", "abcda"
    cnt_1, cnt_2, cnt_3 = Counter(str_1), Counter(str_2), Counter(str_3)

    if cnt_1 == cnt_2:
        print('1 and 2 anagram')
    if cnt_1 == cnt_3:
        print('1 and 3 anagram')


# bwc()

# try-except-else
# 在Python中，使用 try-except 进行异常捕获。else 可用于当没有异常发生时执行。
# 如果你需要执行一些代码，不管是否发生过异常，请使用 final：

def yichang():
    a, b = 1, 0

    try:
        print(a / b)
        # exception raised when b is 0
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("no exceptions raised")
    finally:
        print("Run this always")


# yichang()

# 枚举遍历
# 下面的代码片段中，遍历列表中的值和对应的索引：
def enum_bl():
    my_list = ['a', 'b', 'c', 'd', 'e']
    for index, value in enumerate(my_list):
        print('{0}: {1}'.format(index, value))


# enum_bl()


# 对象使用内存大小
def disksize():
    num = 21
    print(sys.getsizeof(num))


# disksize()

# 合并两个字典
# 在 Python 2 中，使用 update() 方法来合并，在 Python 3.5 中，
# 更加简单，在下面的代码片段中，合并了两个字典，在两个字典存在交集的时候，则使用后一个进行覆盖。

def hb_dict():
    dict_1 = {'apple': 9, 'banana': 6}
    dict_2 = {'banana': 4, 'orange': 8}
    combined_dict = {**dict_1, **dict_2}
    print(combined_dict)


# hb_dict()

# 代码执行时间
# 下面的代码片段中，使用了 time 这个库，来计算代码执行的时间：
def run_time():
    start_time = time.time()
    # Code to check follows
    a, b = 1, 2
    c = a + b
    # Code to check ends
    end_time = time.time()
    time_taken_in_micro = (end_time - start_time) * (10 ** 6)
    print(" Time taken in micro_seconds:%s ms" % time_taken_in_micro)


# run_time()


# 列表展开
# 有时候，你不知道你当前列表的嵌套深度，但是你希望把他们展开，放到一维的列表中。下面教你实现它：


# 路径拼接
def pinje():
    path1 = 'aaaa/'
    path2 = 'bbbb/'
    print(os.path.join(path1, path2, 'text.txt'))


pinje()
