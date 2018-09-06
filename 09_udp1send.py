# import socket
# #tcp套接字，传输控制协议，稳定，慢，不丢数据，web服务器
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #udp套接字，用户数据包协议，不稳定，快，丢数据
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

from socket import socket, AF_INET, SOCK_DGRAM

udpSocket = socket(AF_INET, SOCK_DGRAM)

# recvAddr = ('192.168.179.131', 8080)
ipAddr = input("目标IP：")
port = int(input("目标端口："))
recvAddr = (ipAddr, port)
# python3须是b'qwe'
sendData = input("发送的数据：")
# sendData = b'qwer'

# sendData.encode('gb2312')
udpSocket.sendto(sendData.encode('utf-8'), recvAddr)
udpSocket.close()
