#client_v1-by nicholas for Wireless Networking Comms
import socket
import colorama
colorama.init(autoreset=True)

#auto hostip finder...for localhost testing only
gethost = socket.gethostbyname(socket.gethostname())  #gets the localhost socket IP
print (f'Server IP to connect to {gethost}') #visual aid


HOST = gethost # change this to the IP you want to connect to if not testing on your local machine.
PORT = 5678  #port & host ip must be the same in client and server
print (f" Your Server's IP is  \033[0;32m{HOST}\033[0m, connecting to Port: \033[0;32m{PORT}\033[0m ")  #visual aid



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connects
    while True:
        client_comment = input("What would you like to tell the server?: ") #lets user write string to send to server.
        s.send(client_comment.encode('utf-8')) #encodes data for transfer.
        if client_comment.lower() == 'quit':  # Lets user exit if they type in the word  "quit"
            break
        response = s.recv(1024).decode('utf-8')  #server response to user packet.
        print(f"{colorama.Fore.RED}{response}")
        print(colorama.Style.RESET_ALL)



#note: still a wip, user cannot send more than 1 message before ports closed. New version will resolve this issue. :)