import socket
import threading
import random
import os



# Client configuration
HOST = str(input('Enter the IP address of the server : '))
PORT = int(input('Enter the server port: '))
    
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((HOST, random.randint(1024,49151)))

name = input("ENTER YOUR NAME : ")

def receive():
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print(message.decode())
        except:
            pass

thread = threading.Thread(target=receive)
thread.start()

client_socket.sendto(f'Hi, my name is: {name}'.encode(), (HOST, PORT))

print("\t\t\t=====================================================================")
print("\t\t\t=====================================================================")
print("\t\t\t========================== Welcome CinCHAT ==========================")
print("\t\t\t=====================================================================")
print("\t\t\t=====================================================================")

print('<send> to send the file or <bye> to get out')

while True:
    option = input(' ')
    if option == 'send':
        #open file
        with open('filename.txt', 'rb') as file:
            # Send the file data
            message = file.read(1024)
            client_socket.sendto(f'/~{name}: {message}'.encode(), (HOST, PORT))
    else:
        os._exit(1)
    
    


