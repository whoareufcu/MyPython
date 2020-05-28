g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
for n in g:
    print(n)
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：