import itertools as its
import string


def createDict(path, repeats, words):
    dict = its.product(words, repeat=repeats)
    '''这里的words是要迭代的字符串，repeats是生成的密码长度，生成的dict是一个返回元组的迭代器'''
    f = open(path, 'a')
    for cipher in dict:
        f.write(''.join(cipher) + '\n')
    f.close()


def main():
    # numbers = string.digits  # 包含0-9的字符串
    numbers = string.ascii_letters  #
    path = r'C:\Users\whoareu\Desktop\UT12\mydict2.txt'
    length = 7
    for i in range(1, length):
        createDict(path, i, numbers)


if __name__ == "__main__":
    main()
