import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = './html'

def handle_client(cliSocket):
    request_data = cliSocket.recv(1024)
    print(request_data)
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)
    request_start_line = request_lines[0]
    print(request_start_line.decode('utf-8'))
    filename = re.match(r'\w+ +(/[^ ]*) ', request_start_line.decode('utf-8')).group(1)

    if '/' == filename:
        filename = '/index.html'

    try:
        file = open(HTML_ROOT_DIR + filename, 'rb')
    except IOError:
        response_start_line = 'HTTP/1.1 404 Not Found\r\n'
        response_headers = 'Server: My server\r\n'
        response_body = 'The Page is not Found!'
    else:
        file_data = file.read()
        file.close()

        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server: My server\r\n'
        response_body = file_data.decode('utf-8')

    response = response_start_line + response_headers + '\r\n' + response_body
    print('response_data:', response)

    cliSocket.send(bytes(response, 'utf-8'))
    cliSocket.close()


def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('', 8060))
    serverSocket.listen(128)

    while True:
        cliSocket, cliAddr = serverSocket.accept()
        print('[%s: %s]' % cliAddr)
        handleCliProcess = Process(target=handle_client, args=(cliSocket,))
        handleCliProcess.start()
        cliSocket.close()


if __name__ == '__main__':
    main()
