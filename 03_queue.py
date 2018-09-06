from multiprocessing import Queue, Process
import time
# import os


# 进程间通信--Process
def write(q):
    for val in ['a', 'b', 'c']:
        print('put %s' % val)
        q.put(val)
        time.sleep(1)


def read(q):
    while True:
        if not q.empty():
            val = q.get(True)
            print('get %s' % val)
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    # 进程中的队列
    q = Queue()
    pw = Process(target=write(q))
    pr = Process(target=read(q))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
