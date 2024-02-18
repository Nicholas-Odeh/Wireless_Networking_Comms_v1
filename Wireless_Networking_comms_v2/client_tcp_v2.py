#client_tcp_v2
import time  #allows for a update to be timed
import psutil #PROCESSING SYSTEM UTILITY
import colorama
import socket
colorama.init(autoreset=True)

last_rec = psutil.net_io_counters().bytes_recv  #Gives current total amount of bytes recv
last_sent = psutil.net_io_counters().bytes_sent #Gives total amount of bytes sent
last_total = last_rec + last_sent #give complete total amount of bytes



#auto hostip finder...for localhost testing only
#auto hostip finder...for localhost testing only
gethost = socket.gethostbyname(socket.gethostname())  #gets the localhost socket IP
print (f'Server IP to connect to {gethost}') #visual aid
HOST = gethost # change this to the IP you want to connect to if not testing on your local machine.
PORT = 5678  #port & host ip must be the same in client and server
print (f" Your Server's IP is  \033[0;32m{HOST}\033[0m, connecting to Port: \033[0;32m{PORT}\033[0m ")  #visual aid


#TCP SOCKET SERVER
while True: #endless loop
    bytes_rec = psutil.net_io_counters().bytes_recv  #does the same as line 4 -6
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total =  bytes_rec +  bytes_sent
#bandwidth calc
    new_rec = bytes_rec - last_rec
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total
            #1024->kb / 1024-> mb
    mb_new_rec = new_rec / 1024  / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024
    #.2f gives .002 | .5f give .00005

    last_rec = bytes_rec
    last_sent = bytes_sent  #new data points for cal to use after each refresh
    last_total = bytes_total

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # connects
        while True:
            client_comment = input(
                "What would you like to tell the server?: ")  # lets user write string to send to server.
            s.send(client_comment.encode('utf-8'))  # encodes data for transfer.
            if client_comment.lower() == 'quit':  # Lets user exit if they type in the word  "quit"
                break
            response = s.recv(1024).decode('utf-8')  # server response to user packet.
            print(f"{colorama.Fore.RED}{response}")
            print(colorama.Style.RESET_ALL)
            print(f' Bandwidth Usage: \033[33m{mb_new_rec:.2f} MB received, {mb_new_sent:.2f} MB send, {mb_new_total:.2f} total usage \033[0m')  # visual for bandwidth
            break
