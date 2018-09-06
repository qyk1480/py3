from threading import Thread
from socket import socket, AF_INET, SOCK_DGRAM


def recvData(udpSocket):
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        content, ipPort = recvInfo
        print('\r>>>[%s: %s]' % (ipPort, content.decode('gbk')), end='')
        print('\r\n<<<', end='')


def sendData(udpSocket, ip, port):
    while True:
        sendInfo = input('<<<')
        udpSocket.sendto(sendInfo.encode('gbk'), (ip, port))


def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 7228))

    ip = input('ip:')
    port = int(input('port:'))

    # ts = Thread(target=sendData(udpSocket, ip, port))
    tr = Thread(target=recvData, args=(udpSocket,))
    ts = Thread(target=sendData, args=(udpSocket, ip, port))
    tr.start()
    ts.start()
    tr.join()
    ts.join()


if __name__ == '__main__':
    main()
