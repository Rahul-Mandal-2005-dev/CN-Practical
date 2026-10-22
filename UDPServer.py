# 8C:

import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 12345))

    print("Waiting for UDP message...")
    data, addr = s.recvfrom(1024)
    print("Client:", data.decode())

    s.sendto(b"Hello from UDP server", addr)
    s.close()

def main():
    server()

main()