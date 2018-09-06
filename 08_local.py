import threading

# 解决线程中对全局变量的污染
localS = threading.local()


def process_student():
    std = localS.student
    print('%s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的stud
    localS.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('qwe',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('asd',), name='Thread-B')
t1.start()
t2.start()
