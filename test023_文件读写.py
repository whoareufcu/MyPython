def openFile1(path, type):
    try:
        f = open(path, type)
        print(f.read())
    finally:
        if f:
            f.close()


# openFile1(r"D:\mypy1\IO\mydict.txt", "r")


# 这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
def openFile2(path, type):
    with open(path, type) as f:
        print(f.read())
        # print(f.read(8))
        # print(f.readline())
        # L = f.readlines()
        # for l in L:
        #     print(l)


# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。
# 因此，要根据需要决定怎么调用。

# openFile2(r"D:\mypy1\IO\mydict.txt", "r")
# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# openFile2(r"D:\mypy1\IO\man.png", "rb")

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
def openFile3(path, type):
    with open(path, type, encoding="gbk") as f:
        print(f.read())


# openFile3(r"D:\mypy1\IO\gbk.txt", "r")


# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
def writeFile(path, type, content):
    f = open(path, type)
    f.write(content)
    f.close()
    print("写入完毕")


# writeFile(r"D:\mypy1\IO\gbk.txt", "w", "Hello,Wrold")

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
# 所以，还是用with语句来得保险：
def writeFile2(path, type, content):
    with open(path, type) as f:
        f.write(content)
        print("写入完毕！")


# writeFile2(r"D:\mypy1\IO\gbk.txt", "w", "Hello,Wrold")

# 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
# writeFile2(r"D:\mypy1\IO\gbk.txt", "a", "Hello,Wrold")
