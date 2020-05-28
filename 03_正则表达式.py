# \d 可以匹配一个数字
# \w 可以匹配一个字母或数字
# '00\d'可以匹配'007'，但无法匹配'00A'；
# '\d\d\d'可以匹配'010'；
# '\w\w\d'可以匹配'py3'；
# .可以匹配任意字符，所以：'py.'可以匹配'pyc'、'pyo'、'py!'等等。
# *表示任意个字符（包括0个）
# 用+表示至少一个字符
# 用?表示0个或1个字符
# 用{n}表示n个字符，用{n,m}表示n-m个字符
# \s可以匹配一个空格（也包括Tab等空白符）

# 例子：\d{3}\s+\d{3,8}
# 我们来从左到右解读一下：
# \d{3}表示匹配3个数字，例如'010'；
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
# \d{3,8}表示3-8个数字，例如'1234567'。

# 进阶
# 要做更精确地匹配，可以用[]表示范围，比如：
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由数字、字母或者下划线组成的字符串，也就是Python合法的变量；
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。
# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。


# re模块
# 有了准备知识，我们就可以在Python中使用正则表达式了。
# Python提供re模块，包含所有正则表达式的功能。
# 由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001'
# Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
s = r'ABC\-001'
# Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

# 先看看如何判断正则表达式是否匹配：
import re


def mate1():
    print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))


def mate2():
    print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))


mate1()
mate2()


# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
# 常见的判断方法就是：
def mate3():
    test = '010-12345'
    if re.match(r'^\d{3}\-\d{3,8}$', test):
        print('ok')
    else:
        print('failed')


mate3()

# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
print('a b   c'.split(' '))


# ['a', 'b', '', '', 'c']
# 无法识别连续的空格，用正则表达式试试：
def mysplit():
    test = 'a b   c'
    print(re.split(r'\s+', test))


mysplit()


# 无论多少个空格都可以正常分割。加入,试试：
def mysplit1():
    test = 'a,b, c  d'
    print(re.split(r'[\s\,]+', test))


mysplit1()


# 再加入;试试：
def mysplit2():
    test = 'a,b;; c  d'
    print(re.split(r'[\s\,\;]+', test))


mysplit2()


# 如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
def group1():
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print('group0:%s group1:%s group2:%s ' % (m.group(0), m.group(1), m.group(2)))


group1()


# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。


# 贪婪匹配
# 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
def greed():
    m = re.match(r'^(\d+)(0*)$', '102300')
    print(m.groups())


greed()


# 结果为('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
# +? 表示在整个匹配成功的前提下，使用最少的重复
def greed_not():
    m = re.match(r'^(\d+?)(0*)$', '102300')
    print(m.groups())


greed_not()


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2.用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
def pre_compile():
    # 编译
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    # 使用
    print(re_telephone.match('010-12345').groups())
    print(re_telephone.match('010-8086').groups())


pre_compile()


# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。


# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#
# someone@gmail.com
# bill.gates@microsoft.com
def is_valid_email(addr):
    if re.match(r'^[a-z]+[a-z\.]*\@[a-z]+\.com$', addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok通过验证')


# 练习
# 版本二可以提取出带名字的Email地址：
#
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

def name_of_email(addr):
    m = re.match(r'^<?([\w\s]*)>?[\w\s]*@\w+.org$', addr)
    print(m.groups())
    return m.group(1)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
