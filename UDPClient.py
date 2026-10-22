# 8D:

import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(b"Hello from UDP client", ("127.0.0.1", 12345))
    data, addr = s.recvfrom(1024)

    print("Server:", data.decode())
    s.close()

def main():
    client()

main()