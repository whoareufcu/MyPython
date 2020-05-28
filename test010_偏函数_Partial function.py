# //str转int
# 默认十进制
import functools

print(int("12345"))
# 二进制转十进制
print(int("1001000", base=2))
# 8进制转十进制
print(int("12345", base=8))
# 16进制转十进制
print(int("12345", base=16))


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
# 于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
# 这样，我们转换二进制就非常方便了：
def int2(x, base=2):
    return int(x, base)


print(int2("1111"))

# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
int3 = functools.partial(int, base=2)
print(int3("100001"))
