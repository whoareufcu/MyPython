print("from the spam.py")
money = 1000


def read1():
    print("spam模块 %s:" % money)


def read2():
    print("spam模块")
    read1()
