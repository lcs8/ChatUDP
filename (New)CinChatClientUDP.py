import socket
import os


# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_file(filename,HOST,PORT):
    with open(filename, 'rb') as file:
        # Prefix the filename with "FILE:" to indicate a file transfer
        message = (f"FILE:{filename}")
        client_socket.sendto(message.encode('utf-8'), (HOST, PORT))

        # Send the file data
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendto(data, (HOST, PORT))
def send(name,HOST,PORT):
	while True:
		message = input(f"{name} >> ")
		if message == "quit":
			os._exit(1)
		sm = "{} : {}".format(name,message)
		client_socket.sendto(sm.encode() , (HOST,int(PORT)))

def received():
	while True:
		msg = client_socket.recvfrom(1024)
		print("\t\t\t\t >> " + msg[0].decode())
		print(">> ")

def main():
    print("\t\t\t=========================================")
    print("\t\t\t============ Welcome CinCHAT ============")
    print("\t\t\t=========================================")
    
    # Client configuration
    HOST = str(input('Enter the IP address of the server : '))
    PORT = int(input('Enter the server port : '))

    name = input("ENTER YOUR NAME : ")
    options =str(input('File to be send or quit'))
    parei aqui agora tem que pegar essa variavel option se ele digitar
    send pedir a função send_file.
    
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()

