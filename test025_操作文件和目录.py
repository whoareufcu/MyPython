import os
import shutil

# 查看当前目录的绝对路径


path = os.path.abspath(".")
print(path)
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join("D:\mypy1", "testdir")
# 然后创建一个目录:
# os.mkdir(r"D:\mypy1\testdir")
# 删掉一个目录
# os.rmdir(r"D:\mypy1\testdir")

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
# os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# shutil.copyfile()

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
L = [x for x in os.listdir(".") if os.path.isdir(x)]
print("当前目录下所有目录：", L)
# 列出当前目录下所有文件
L1 = [x for x in os.listdir(".") if os.path.isfile(x)]
print("当前目录下所有文件：", L1)
# 列出当前目录下所有.py文件
L2 = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"]
print("当前目录下所有.py文件：", L2)


# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序。
#
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。