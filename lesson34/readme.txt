How to run the server and client

Run the UDP server: Open a terminal or command prompt and run the UDP server script. This will start the server and it will begin listening for incoming datagrams on the specified host and port.
python echo_server.py

Run the UDP client: Open another terminal or command prompt and run the UDP client script. This will send a message along with the shift key to the UDP server and wait for the encrypted response.
python echo_client.py

Explanation

    Caesar Cipher Function:
        This function takes a text and a shift value and returns the encrypted text using the Caesar cipher algorithm.

    UDP Server:
        The server now expects data in the format message|shift, where message is the text to be encrypted and shift is the Caesar cipher shift key.
        It splits the received data to extract the message and the shift value, encrypts the message using the Caesar cipher, and sends the encrypted message back to the client.

    UDP Client:
        The client sends the message and the shift value in the format message|shift to the server.
        It waits for the encrypted response from the server and prints it.

This setup allows the client to send a message and a shift key to the server, which then encrypts the message using the Caesar cipher and sends the encrypted message back to the client.
