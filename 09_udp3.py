from socket import socket, AF_INET, SOCK_DGRAM


def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 8080))

    while True:
        recvData = udpSocket.recvfrom(1024)
        content, ipPort = recvData
        print(['%s--->%s' % (ipPort, content.decode('gbk'))])
        # echo服务器，接收什么就怎么回
        udpSocket.sendto(content, ipPort)


if __name__ == '__main__':
    main()
