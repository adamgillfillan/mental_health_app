__author__ = 'Adam'

import socket
s = socket.socket()

udp_host = socket.gethostname()
udp_port = 3001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_host, udp_port))

while 1:
    data, addr = sock.recvfrom(1024)
    print("Message: ", data)