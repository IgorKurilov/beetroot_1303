import socket

def udp_server(host='127.0.0.1', port=12345):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the address and port
    server_address = (host, port)
    sock.bind(server_address)
    
    print(f"UDP server is up and listening on {host}:{port}")
    
    while True:
        # Wait for a datagram from a client
        data, address = sock.recvfrom(4096)
        
        print(f"Received {len(data)} bytes from {address}")
        print(f"Data: {data.decode()}")
        
        if data:
            sent = sock.sendto(data, address)
            print(f"Sent {sent} bytes back to {address}")

if __name__ == "__main__":
    udp_server()
