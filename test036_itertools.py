# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
#
# 首先，我们看看itertools提供的几个“无限”迭代器：
import itertools


def my_count():
    # 参数start step
    natuals = itertools.count(1, 2)
    for i in natuals:
        print(i)


# my_count()
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来

# cycle()会把传入的一个序列无限重复下去：
def my_cycle():
    cs = itertools.cycle('ABC')
    for i in cs:
        print(i)


# my_cycle()
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
def my_repeat():
    ns = itertools.repeat('A', 5)
    for i in ns:
        print(i)


# my_repeat()

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
#
# 它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
#
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
def my_takewhile():
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x < 10, natuals)
    print(list(ns))


# my_takewhile()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
def my_chain():
    for i in itertools.chain('ABC', 'XYZ'):
        print(i)


# my_chain()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
def my_groupby():
    d = dict()
    for key, group in itertools.groupby('AABBCCDKK'):
        l = list(group)
        d[key] = l
        print(key, l)
    print('dict:', d)


# my_groupby()

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
def my_groupby2():
    d = dict()
    for key, group in itertools.groupby('AaaBbbbUuuuDddd', lambda x: x.upper()):
        l = list(group)
        d[key] = l
        print(key, l)
    print('dict:', d)


# my_groupby2()
# 练习
# 计算圆周率可以根据公式：
#
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # L1=range(1,N,2)
    L1 = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    L2 = itertools.takewhile(lambda x: x <= 2 * N - 1, L1)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    n = -1
    list = []
    for l in L2:
        n = n * -1
        num = n * 4 / l
        list.append(num)
    # step 4: 求和:
    return sum(list)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
