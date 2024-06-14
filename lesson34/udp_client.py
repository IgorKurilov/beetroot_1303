import socket

def udp_client(host='127.0.0.1', port=12345, message="Hello, UDP Server!"):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
    
    try:
        # Send data
        print(f"Sending: {message}")
        sent = sock.sendto(message.encode(), server_address)
        
        # Receive response
        print("Waiting for response...")
        data, server = sock.recvfrom(4096)
        print(f"Received: {data.decode()}")
        
    finally:
        print("Closing socket")
        sock.close()

if __name__ == "__main__":
    udp_client()
