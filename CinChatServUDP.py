import socket
import threading
import queue

messages = queue.Queue()
clients = []

# Server configuration
IP_ADDRESS = str(input('Server IP Address : '))
PORT = int(input('Server Port : '))

# Buffer size for receiving data
BUFFER_SIZE = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_ADDRESS, PORT))

print(f"Server listening on {IP_ADDRESS}:{PORT}")

#receives files from the client
def receive_file():
    while True:
        try:
            message,address = server_socket.recvfrom(BUFFER_SIZE)
            messages.put((message, address))
        except:
            pass

#forward the message to all clients within the chat
def broadcast():
    while True:
        while not messages.empty():
            message, address = messages.get()
            print(message.decode())
            if address not in clients:
                clients.append(address)
            for client in clients:
                try:
                    if message.decode().startswith('Entered the chat room.'):
                        name = message.decode()[message.decode().index(':')+1:]
                    else:
                        server_socket.sendto(message, client)
                except:
                    clients.remove(client)

thread1 = threading.Thread(target=receive_file).start()
thread2 = threading.Thread(target=broadcast).start()

