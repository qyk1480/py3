import os
from multiprocessing import Pool,Manager


# 多进程拷贝文件
def copyFile(name, oldFolder, newFolder, queue):
    fr = open(oldFolder + os.sep + name, encoding='utf-8')
    fw = open(newFolder + os.sep + name, 'w')
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)


def main():
    oldFolder = input("文件夹名：")
    newFolder = oldFolder + '_'
    os.mkdir(newFolder)

    files = os.listdir(oldFolder)

    pool = Pool(5)
    queue = Manager().Queue()
    for name in files:
        pool.apply_async(copyFile(name, oldFolder, newFolder, queue))
        # pool.apply_async(copyFile(name, oldFolder, newFolder))

    num = 0
    allNum = len(files)
    while num < allNum:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\r进度：%.2f%%" % (copyRate*100), end="")


if __name__ == '__main__':
    main()
