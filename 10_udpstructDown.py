from socket import socket, AF_INET, SOCK_DGRAM
import struct

udpSocket = socket(AF_INET, SOCK_DGRAM)
sendReq = struct.pack('!H6sb5sb', 1, b'72.jpg', 0, b'octet', 0)
sendAddr = ('192.168.179.1', 69)
udpSocket.sendto(sendReq, sendAddr)

# 块编号
num = 0

while True:
    recvData, recvAddr = udpSocket.recvfrom(1024)
    lenReData = len(recvData)

    # print(recvData)
    # print(lenReData) --->516

    # dataPackageOpCodes是元祖，0操作码，1块编号
    opCodes = struct.unpack('!HH', recvData[:4])
    # print(opCodes)  --->(3,1)
    if opCodes[0] == 3:
        # 第一次接收则创建文件
        if opCodes[1] == 1:
            file = open('72.jpg', 'ab')

        if opCodes[1] == (num + 1):
            file.write(recvData[4:])
            num += 1
            print("%d次接收数据" % num)

            ackCode = struct.pack('!HH', 4, num)
            udpSocket.sendto(ackCode, recvAddr)

        if lenReData < 516:
            file.close()
            print("完成！")
            break

    if opCodes[0] == 5:
        print('error num: %d' % opCodes[1])
        break

udpSocket.close()
