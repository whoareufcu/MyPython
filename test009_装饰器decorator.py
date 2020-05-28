def now():
    print("10:30")


f = now
print(f)
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        print("args={}".format(*args))
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(test.__name__ + "param: " + p)


test("im a param")
