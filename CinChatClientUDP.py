import socket
import threading
import os
from datetime import datetime


# Client configuration with server inputs
HOST = str(input('Enter the IP address of the server : '))
PORT = int(input('Enter the server port: '))
BUFFER_SIZE = 1024

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((HOST, PORT))

name = str(input('Hi, my name is : '))

#receives files from the server
def receive_message():
    while True:
        try:
            message, _ = client_socket.recvfrom(BUFFER_SIZE)
            print(message.decode())
        except:
            pass

thread = threading.Thread(target=receive_message).start()

#receives message when clients enter chat
client_socket.sendto(f'{name} Entered the chat room.'.encode(), (HOST, PORT))

print("\t\t\t=====================================================================")
print("\t\t\t=====================================================================")
print("\t\t\t========================== Welcome CinCHAT ==========================")
print("\t\t\t=====================================================================")
print("\t\t\t=====================================================================")

print('<send> to send the file or <bye> to get out')

while True:
    option = str(input(' '))
    if option == 'send':
        #open file
        with open('filename.txt', 'r') as file:
            # Send the file data
            message = file.read(BUFFER_SIZE)
            # Include IP address, port, date, and time in the message
            client_address = client_socket.getsockname()
            current_time = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            client_socket.sendto(f'{client_address}/~{name}: {message}{current_time}'.encode(), (HOST, PORT))
    elif option=='bye':
        print('goodbye! ;)')
        os._exit(1)
    else:
        print('<send> or <bye>')
    
    


