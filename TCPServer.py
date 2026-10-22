import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12345))
    s.listen(1)

    print("Waiting for client...")
    conn, addr = s.accept()
    print("Connected:", addr)

    data = conn.recv(1024)
    print("Client:", data.decode())

    conn.sendall(b"Hello from TCP server")
    conn.close()
    s.close()

def main():
    server()

main()





