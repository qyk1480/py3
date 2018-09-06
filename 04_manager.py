from multiprocessing import Manager, Pool
# import time
import os


# 进程间通信--Pool
def writer(q):
    print('write pid==%d' % os.getpid())
    for i in 'qwertyu':
        q.put(i)


def reader(q):
    print('read pid==%d' % os.getpid())
    for i in range(q.qsize()):
        print('read==%s' % q.get(True))


if __name__ == '__main__':
    print('%s start' % os.getpid())
    q = Manager().Queue()
    po = Pool(10)

    po.apply_async(writer(q))
    po.apply_async(reader(q))
    po.close()
    po.join()
