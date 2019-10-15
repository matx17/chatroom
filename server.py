import socket
from threading import Thread
from sys import argv
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
script,host,port=argv
list = int(port)
Host=""
port=list
clients={}
cli_socket=[]
s.bind(("",port))

def broadcast(message, cli_conn):
    for k in cli_socket:
         if k != s and k != cli_conn :
            k.send(message)

def acpt_clients():
    while 1:
        conn,addr=s.accept()
        print("connected with", addr)
        conn.send("HELLO 2 \n".encode('utf-8'))
        cli_socket.append(conn)
        Thread(target=handler, args=(conn,addr)).start()



def  handler(conn, addr):
    data = conn.recv(1024)
    name = data.strip("NICK ")
    if len(name)<=10:
       conn.send("Ok \n")
    else:
       conn.send("ERROR - Length of the nickname is greater than 10 \n")
    message = "%s connect to chat \n"%name
    broadcast(message,conn)
    clients[conn] =data


    while 1:
        message= conn.recv(1024)
        msg = message.strip("MSG ")
        if msg == 'quits':
            conn.close()
            del clients[conn]
            mail="%s left from chat \n"% name
            broadcast(mail,conn)
            break

        else :
            if len(message) >200:
                conn.send("ERROR - message is valid \n")
            else:
                mail_data =name + ":" + msg      
            broadcast(mail_data,conn)
while True:
      s.listen(100)
      print("connection is waiting")
      iThread = Thread(target=acpt_clients)
      iThread.daemon = True
      iThread.start()
      iThread.join()
s.close()
