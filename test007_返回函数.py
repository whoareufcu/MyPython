def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = lazy_sum(*L)
print(f())
