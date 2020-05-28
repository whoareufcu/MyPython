def is_odd(n):
    return n % 2 == 1


L1 = [1, 2, 4, 5, 6, 9, 10, 15]
L2 = list(filter(is_odd, L1))
print(L2)


# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(is_palindrome("12345"))
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')