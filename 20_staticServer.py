import socket
from multiprocessing import Process

def handle_client(cliSocket):
    request_data = cliSocket.recv(1024)
    print(request_data)
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My server\r\n'
    response_body = 'Hello qwe!'
    response = response_start_line + response_headers + '\r\n' + response_body
    print('response_data:', response)
    cliSocket.send(bytes(response, 'utf-8'))
    cliSocket.close()


def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 8020))
    serverSocket.listen(128)

    while True:
        cliSocket, cliAddr = serverSocket.accept()
        print('[%s: %s]' % cliAddr)
        handleCliProcess = Process(target=handle_client, args=(cliSocket,))
        handleCliProcess.start()
        cliSocket.close()


if __name__ == '__main__':
    main()
