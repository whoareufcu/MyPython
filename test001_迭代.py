my_list = [1, 2, 3, 4, 5, 7]
d = {'a': 1, 'b': 2, 'c': 3}


# 只要是可迭代对象，无论有无下标，都可以迭代

# list迭代
def listForIn():
    for l in my_list:
        print(l)


# listForIn()
# dict迭代
def dictForIn():
    for key in d:
        print(key, d[key])


def dictForIn2():
    for value in d.values():
        print(value)


def dictForIn3():
    for key in d.keys():
        print(key)


def dictForIn4():
    for k, v in d.items():
        print(k, v)


# dictForIn2()
# str迭代
def strForIn():
    for s in 'ABDCH':
        print(s)

# strForIn()
# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for l in L:
            if l > max:
                max = l
            if l < min:
                min = l
        return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
