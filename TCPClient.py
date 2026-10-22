# 8B:

import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 12345))

    s.sendall(b"Hello from TCP client")
    data = s.recv(1024)

    print("Server:", data.decode())
    s.close()

def main():
    client()

main()