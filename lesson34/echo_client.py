import socket

def udp_client(host='127.0.0.1', port=12345, message="Hello, UDP Server!", shift=3):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
    
    try:
        # Prepare the data to send (message|shift)
        data = f"{message}|{shift}"
        print(f"Sending: {data}")
        
        # Send data
        sent = sock.sendto(data.encode(), server_address)
        
        # Receive response
        print("Waiting for response...")
        data, server = sock.recvfrom(4096)
        print(f"Received: {data.decode()}")
        
    finally:
        print("Closing socket")
        sock.close()

if __name__ == "__main__":
    udp_client()
