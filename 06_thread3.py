import threading
# import time

num = 0


def test1():
    global num

    for i in range(1000000):
        # 锁定
        mutex.acquire()
        num += 1
        # 释放
        mutex.release()
    print('test1 === %d' % num)


def test2():
    global num
    # 锁定
    for i in range(1000000):
        mutex.acquire()
        num += 1
        # 释放
        mutex.release()
    print('test2 === %d' % num)


# 互斥锁
mutex = threading.Lock()
p1 = threading.Thread(target=test1)
p1.start()
p2 = threading.Thread(target=test2)
p2.start()

# 线程 全局变量共用，非全局变量不共享，不需要加锁
# mutex.acquire(2) 等待2秒，超时时间
