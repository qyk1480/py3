from socket import socket, AF_INET, SOCK_STREAM
# tcp服务端2个套接字，一个等待，一个交互
tcpServerSocket = socket(AF_INET, SOCK_STREAM)

tcpServerSocket.bind(('', 9696))

tcpServerSocket.listen(6)
# 新套接字，新套接字的ip和port
# py 运行，等待对方连接
clientSocket, clientInfo = tcpServerSocket.accept()
# 连接后，等待对方发数据
recvData = clientSocket.recv(1024)

print('%s: %s' % (str(clientInfo), recvData))

clientSocket.close()
tcpServerSocket.close()
