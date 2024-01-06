import socket
import os
import threading #Por se tratar de um Chat com múltiplos usuários, precisamos importar a biblioteca threading.
import time
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Variável de controle indicando quando as threads devem ser encerradas
exit_flag = False

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
    global exit_flag 

    while True:
        if exit_flag:
            break #sair do loop se a variável indicar a saída
        message = input(f"{name} >> ")
        if message == "quit":
            exit_flag = True #Sinalizando para as threads encerrarem
            break
        sm = "{} : {}".format(name, message)
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
    
    #Implementação da biblioteca threading para envio e recebimento de mensagens
    send_thread = threading.Thread(target=send, args=(name, HOST, PORT))
    receive_thread = threading.Thread(target=received)

    #Iniciar threads
    send_thread.start()
    receive_thread.start()

    #Implementação do menu interativo do usuário.
    while True:
        option = str(input('Enter "send" to send a file, "wait" to stay in the chat and receive messages, or "quit" to leave the chatroom: '))

        if option.lower() == 'send':
            pass #Vou implementar o envio de arquivos posteriormente.
        elif option.lower() == 'wait':
            pass #Nesse estado o cliente vai ficar somente lendo as mensagens, sem enviar nada, até decidir enviar algo novamente
        elif option.lower() == 'quit':
            print("Exiting the program in ", end='', flush = True)

            for i in range(3, 0, -1):
                 time.sleep(1)
                 print(f"{i}...", end='', flush = True)

            print("Goodbye! o/")
            break #Sai do loop e permite a conclusão ordenada das threads.
        else:
             print('Invalid option. Please enter "send" to send a file, "wait" to receive messages, or "quit" to exit. ')
    
 
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()

