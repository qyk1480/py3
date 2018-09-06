from multiprocessing import Pool
import time
import os


# 异步
def test():
    print('pid=%d,ppid=%d' % (os.getpid(), os.getppid()))
    for i in range(3):
        print('--%d--' % i)
        time.sleep(1)
    return 'qwe'


def test2(args):
    print('callback func pid=%d' % os.getpid())
    # --->ppid
    print('callback func args=%s' % args)
    # --->'qwe'


pool = Pool(3)
# linux可以win不可以
pool.apply_async(func=test, callback=test2)

while True:
    time.sleep(1)
    print("主进程-pid=%d" % os.getpid())
