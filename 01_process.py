# import os
from multiprocessing import Process
import time


def test(name):
    for i in range(5):
        print('123%s' % name)
        time.sleep(1)


if __name__ == "__main__":
    p = Process(target=test('qwe'))
    p.start()
    # p.join()

    while True:
        print('main')
        time.sleep(1)
