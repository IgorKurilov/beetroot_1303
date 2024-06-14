import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

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
        
        if data:
            # Data format: "message|shift"
            message, shift = data.decode().rsplit('|', 1)
            shift = int(shift)
            
            print(f"Received message: {message} with shift: {shift} from {address}")
            
            # Encrypt the message
            encrypted_message = caesar_cipher(message, shift)
            
            # Send the encrypted message back to the client
            sent = sock.sendto(encrypted_message.encode(), address)
            print(f"Sent encrypted message: {encrypted_message} to {address}")

if __name__ == "__main__":
    udp_server()
