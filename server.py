import socket
import sys
import threading
import time
import pickle
import db
import os
import copy

'''
msg_list format:
login_info : [instruction, match(bool), args]
join_info : [instruction, match(bool), args]
'''



class thread_server():
    def __init__(self):
        self.host = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host)
        self.port = 5555
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.host,self.port))
        self.server_socket.listen()
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.c_list={}
        self.client_list={} # thread_object : client_socket
        self.server_db=db.database()
        self.my_dir = os.getcwd()
        self.msg_list=[]
        self.instruction=' '
        self.number_of_clients = 0

        self.count_thread = threading.Thread(target=self.count_clients, name=None)
        self.count_thread.start()

    def accept_client(self):
        print('waiting for client')
        (self.client_socket, addr) = self.server_socket.accept()
        my_thread=threading.Thread(target=self.server_process, name=None, args=(self.client_socket,))
        #mutex
        self.client_list[my_thread]=self.client_socket
        self.c_list[my_thread]=self.client_socket
        #mutex
        my_thread.start()

    def server_recv(self,clntsock):  # instruction receive
        try:
            print('waiting to recv message from client')
            data_recv=clntsock.recv(2048)
            print(data_recv)
            data=pickle.loads(data_recv)
            print(data)

            if data[0] == 'close_thread':
                return False
            else:
                self.server_db.get_data(data,clntsock)
                if data[0]=='count_users':
                    data.append(self.number_of_clients)
                self.server_send(data,clntsock)
                return True
        except:
            print('비정상 종료 at recv')
            return False

    def server_send(self, data_list, clntsock):
        #cur_thread = threading.current_thread()
        #clntsock=self.client_list[cur_thread]
        print(f'sending {data_list}')
        clntsock.send(pickle.dumps(data_list))

    #thread running function
    def server_process(self,clntsock):
        while self.server_recv(clntsock):
            pass
        my_thread=threading.currentThread()
        del(self.client_list[my_thread])
        del(self.c_list[my_thread])
        print('thread ends')

    def count_clients(self):
        while True:
            self.number_of_clients = len(self.c_list)
            #print(self.number_of_clients)

if __name__=='__main__':
    server=thread_server()
    while True:
        #mutex
        server.accept_client()
        #mutex
'''
server=thread_server()
print('waiting for client')
(server.client_socket, addr) = server.server_socket.accept()

size=pickle.loads(server.client_socket.recv(1024))
print(size)
a=0
f = open('123.jpg','wb')
while size > a:
    data=server.client_socket.recv(10240)
    b=len(data)
    print(b)
    a=a+b
    f.write(data)
f.close()
'''




