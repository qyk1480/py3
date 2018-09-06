import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = self.name + '@' + str(i)
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        # start()中调用run()
        t.start()


if __name__ == '__main__':
    test()
