# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Joe', 'Bob', 'Jane']
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)
print('长度:%s' % len(classmates))
print('倒数第一个：%s' % classmates[-1])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Bill')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(0, 'Albus')
print(classmates)
# 要删除list末尾的元素，用pop()方法：
# classmates.pop()
# print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# classmates.pop(1)
# print(classmates)


# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，
# 但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
name = ('A', 'B', 'C')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
# 1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t2 = (1,)
