# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
import logging
import pdb

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    # print("---n:%d" % n)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo("0")


# main()

# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

s = '0'
n = int(s)
# logging.info('n = %d' % n)
pdb.set_trace()
print(10 / n)
