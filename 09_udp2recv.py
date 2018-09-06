from socket import socket, AF_INET, SOCK_DGRAM

udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定，''IP不写则由系统随机分配
# bindAddr = ('', 8080)
# udpSocket.bind(bindAddr)
udpSocket.bind(('', 8080))

# 1024为最大接收字节
recvData = udpSocket.recvfrom(1024)
# 解包
content, ipPort = recvData

print(content.decode('gbk'))
print(ipPort)
# udpSocket.close()
