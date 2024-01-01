import socket
import os

# Server configuration
IP_ADDRESS = str(input('Server IP Address : '))
PORT = int(input('Server Port : '))

# Buffer size for receiving data
BUFFER_SIZE = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_ADDRESS, PORT))

print(f"Server listening on {IP_ADDRESS}:{PORT}")

def receive_file(filename):
    with open(filename, 'wb') as file:
        while True:
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            if not data:
                break
            file.write(data)

def main():
    try:
        while True:
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            message = data.decode('utf-8')

            if message.startswith("FILE:"):
                # If the message starts with "FILE:", it means a file is being sent
                _, filename = message.split(":")
                filename = filename.strip()

                print(f"Receiving file: {filename}")
                receive_file(filename)

                print(f"File received: {filename}")
            else:
                print(f"Received message from {client_address}: {message}")

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    main()

