#server_v1-by nicholas for Wireless Networking Comms
import socket
import colorama
colorama.init(autoreset=True)


#auto hostip finder...for localhost testing only
gethost = socket.gethostbyname(socket.gethostname())
print (f'This is your host IP for your server:\033[0;32m  {gethost} \033[0m') #visual aid

HOST = gethost #No need to change this.
PORT = 5678  #port must be same in client and server

#TCP SOCKET SERVER
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT)) #binds host and port to the server being made
print( f' \n \033[0;31m          ///Binding Server//// \033[0m' )
print(f'Host binded to:\033[0;32m {HOST}\033[0m Port binded to: \033[0;32m{PORT}\033[0m')  #visual aid
print( f'  \033[0;31m          ///Binding Done//// \033[0m' )
print (f'\n')

server_response = ("   PACKET RECEIVED |  SYN/ACK    ")
server_response_2 = ("    ACK RECEIVED, ENDING CONNECTION NOW")   #possible server responses...only SYN/ACK enabled for now.
server_response_3 = ("   SERVER ERROR.. Try again later. ")
server.listen(5) #limits  connects allowed....more than 5 connnects = reject


#where the actual commuincation happens.
while True:
    comms_socket, address = server.accept()  #comms socket used to talk to client.
    print(f' You are connected! :) ') #visual for connection with client
    message = comms_socket.recv(1024).decode('utf-8') #Message from client is decoded and buffered for bits
    print (f' Client message:\033[0;32m {message} \033[0m')
    comms_socket.send((server_response).encode('utf-8'))  #encodes server's SYN/ACK response.
    comms_socket.close() #closes the connection between the client and server. Ends the program.



#Note: still a wip, user cannot send more than 1 message before ports close on server. New version will resolve this issue. :)