# 列表生成式，Python内置简单又强大的，用来创建list的生成式
my_list = [x * x for x in range(1, 5)]
# print(my_list)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
my_list1 = [x * x for x in range(1, 11) if x % 2 == 0]
# print(my_list1)
# 还可以使用两层循环，可以生成全排列：
my_list2 = [m + n for m in 'ABC' for n in 'DEF']
# print(my_list2)
my_list3 = [m + n for m in range(1, 5) for n in range(1, 5)]
# print(my_list3)
my_list4 = [m + n for m in range(1, 5) if m % 2 == 0 for n in range(1, 5) if n % 2 == 0]
# print(my_list4)
my_list5 = [str(x) + str(y) for x in range(1, 5) for y in range(1, 5)]
# print(my_list5)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# 因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
my_list6 = [k + '=' + v for k, v in d.items()]
print(my_list6)

# 把list中的所有字符串都变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
my_list7 = [l.lower() for l in L]
print(my_list7)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
