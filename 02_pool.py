from multiprocessing import Pool
import time
import os


def worker(num):
    for i in range(4):
        print('==%d==%d' % (os.getpid(), num))
        time.sleep(1)


pool = Pool(10)

for i in range(10):
    print('---%d--' % i)
    pool.apply_async(worker(i))
    # pool.apply(worker)

pool.close()
pool.join()
