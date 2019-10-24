import socket,select,sys,re
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv)!=3):
   print("How to use in terminal-> python chatclient.py serveripadd:port nick")
args = str(sys.argv[1]).split(':')
host = str(args[0])
port = int(args[1])
nick = str(sys.argv[2])
s.connect((host, port))
print('connect to server')
temp = s.recv(1024).decode('utf-8')
print(temp)
s.send(('NICK '+nick).encode('utf-8'))
validate = s.recv(1024).decode('utf-8'))
if re.search(r'Error',validate)
   print(validate)
   exit()
print(validate)
while 1:
    Socket_list=[sys.stdin,s]
    read_list,write_list,error_list=select.select(Socket_list,[],[])
    for conn in read_list:
        if conn ==s:
            message =s.recv(1024).decode('utf-8')
            if re.search(r'Error',message):
               print(message)
            else:
               message = message[4:]
               print(message)
        else:
            message = sys.stdin.readline()
            s.send(('MSG '+message).encode('utf-8'))
            sys.stdout.write("me:")
            sys.stdout.write(message)
            sys.stdout.flush()

s.close()
