import socket,select,sys
from sys import argv
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
script,host,port,nickname = argv
Host=""
port=6000
s.connect(("", 6000))
print('connect to server')
NICK = nickname
s.send(NICK)
while 1:
    Socket_list=[sys.stdin,s]
    read_list,write_list,error_list=select.select(Socket_list,[],[])
    for k in read_list:
        if k ==s:
            message =s.recv(1024)
            print(message)
            if not message :
                print("disconnect")
                exit()
        else:
            message = sys.stdin.readline()
            s.send(message.encode('utf-8'))
            sys.stdout.write("me:")
            sys.stdout.write(message)
            sys.stdout.flush()

s.close()
