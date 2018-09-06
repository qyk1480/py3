from socket import socket, AF_INET, SOCK_STREAM

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('192.168.179.131', 9797))

clientSocket.send('zxcv'.encode('gbk'))

recvData = clientSocket.recv(1024)
print('recvData: %s' % recvData)

clientSocket.close()
