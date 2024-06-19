import socket
from multiprocessing import Process

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started on {host}:{port}")
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_client, args=(conn, addr))
            p.start()

if __name__ == "__main__":
    start_server()
