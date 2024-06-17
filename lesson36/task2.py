import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            self.client_socket.sendall(data)
        self.client_socket.close()

def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server started on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handler = ClientHandler(client_socket)
        handler.start()

if __name__ == "__main__":
    echo_server()
