import threading

# 首先借助一个小程序来看看多线程环境下全局变量的同步问题。
global_num = 0
local = threading.Lock()


def thread_call():
    global global_num
    for i in range(1000):
        local.acquire()  # 加锁
        global_num += 1
        local.release()  # 解锁


def startThread():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_call))
        threads[i].start()
    for i in range(10):
        threads[i].join()


# startThread()
# print(global_num)

# 局部变量
def show2(num):
    print(threading.current_thread().getName(), num)


def thread_call2():
    local_num = 0
    for i in range(1000):
        local_num += 1
    show2(local_num)


def startThread2():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_call2))
        threads[i].start()
    for i in range(10):
        threads[i].join()

# startThread2()
# 上面程序中我们需要给 show 函数传递 local_num 局部变量，并没有什么不妥。
# 不过考虑在实际生产环境中，我们可能会调用很多函数，每个函数都需要很多局部变量，
# 这时候用传递参数的方法会很不友好。
# 为了解决这个问题，一个直观的的方法就是建立一个全局字典，保存进程 ID 到该进程局部变量的映射关系，
# 运行中的线程可以根据自己的 ID 来获取本身拥有的数据。这样，就可以避免在函数调用中传递参数，如下示例：