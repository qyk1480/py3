from socket import socket, AF_INET, SOCK_DGRAM
import struct

udpSocket = socket(AF_INET, SOCK_DGRAM)
sendReq = struct.pack('!H7sb5sb', 2, b'10up.py', 0, b'octet', 0)
sendAddr = ('192.168.179.1', 69)
udpSocket.sendto(sendReq, sendAddr)

num = 0
file = open('10up.py', 'rb')

while True:
    recvData, recvAddr = udpSocket.recvfrom(1024)

    print(recvData, recvAddr)
    opCodes = struct.unpack('!HH', recvData[:4])
    print(opCodes)

    if opCodes[0] == 4:
        jpgData = file.read(512)
        print(len(jpgData))

        num += 1
        data = struct.pack('!HH512s', 3, num, jpgData)
        udpSocket.sendto(data, recvAddr)

        if len(jpgData) < 512:
            file.close()
            break


udpSocket.close()
