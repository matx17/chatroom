#!/usr/bin/python
import socket,select,sys,re
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv)!=3):
   print("How to use in terminal-> ./chatclient server_ip_add:port nick")
   exit(1)
args = str(sys.argv[1]).split(':')
host = str(args[0])
port = int(args[1])
nick = str(sys.argv[2])
s.connect((host, port))
print('connect to server')
temp = s.recv(1024).decode('utf-8')
print(temp)
s.send(("NICK "+nick).encode('utf-8'))
validate = s.recv(1024).decode('utf-8')
if re.search(r'ERROR',validate):
    print(validate)
    exit()
else:
   re.search(r'OK',validate)
   print(validate)
valid = s.recv(1024).encode('utf-8')
if re.search(r'ERROR',valid):
    print(valid)
    exit()
print(valid)
while 1:
    Socket_list=[sys.stdin,s]
    read_list,write_list,error_list=select.select(Socket_list,[],[])
    for conn in read_list:
        if conn ==s:
            message =s.recv(1024).decode('utf-8')
            if re.search(r'ERROR',message):
               print(message)
            else:
               print(message)
        else:
            message = sys.stdin.readline()
            message = 'MSG '+ message
            if message == '\n':
                continue
            else:
                s.sendall(message.encode('utf-8'))


s.close()
