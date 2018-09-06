import socket

dest = ('<broadcast>', 7788)
# udp有广播，TCP无
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto('Hi', dest)
print("等待回复")

while True:
    (buf, address) = s.resvfrom(2048)
    print('receive from %s: %s' % (address, buf))
