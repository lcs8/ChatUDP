import socket
import sys

def start_udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if len(sys.argv) != 3:
        print("Como Usar: python3 CinChatServUDP.py ip porta")
        print("Ex: pytnon3 CinChatServUDP.py 127.0.0.1 2310")
        exit()

    # Bind the socket to a specific address and port
    server_address = str(sys.argv[1])
    server_port = int(sys.argv[2])
    server_socket.bind((server_address,server_port))
    
    
    print(f"Server listening on {server_address}:{server_port}")

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        print("Received from client {}: {}".format(client_address, data.decode('utf-8')))

        # Send a response back to the client
        response = "Server received: {}".format(data.decode('utf-8'))
        server_socket.sendto(response.encode('utf-8'), client_address)

if __name__ == "__main__":
    start_udp_server()

