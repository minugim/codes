import socket
import pickle
import os
class ftp:
    def __init__(self,data_list):
        self.host = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host)
        self.port = 6666

        '''
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        '''
        self.data_list = data_list
        self.my_dir = os.getcwd()

    def img_recv(self):
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        ftp_socket.bind((self.host,self.port))
        ftp_socket.listen()
        (ftp_client_socket, addr) = ftp_socket.accept()
        #ftp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        size = self.data_list[2]
        recvd = 0
        fwrite = open(self.my_dir+'/id_'+self.data_list[1]+'/me'+str(self.data_list[3])+'.jpg','wb')

        while size > recvd:
            data = ftp_client_socket.recv(4096)
            tmp = len(data)
            recvd = recvd+ tmp
            fwrite.write(data)
            print(tmp)

        fwrite.close()
        ftp_client_socket.close()

    # ['img_recv',사진 가져갈 id, 사진index]
    def img_send(self):
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ftp_socket.bind((self.host, self.port))
        ftp_socket.listen()
        (ftp_client_socket, addr) = ftp_socket.accept()
        #self.ftp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('보낼게요')
        filepath = self.my_dir+'/id_'+self.data_list[1]+'/me'+str(self.data_list[2])+'.jpg'
        fread = open(filepath,'rb')
        data = fread.read()
        fread.close()

        ftp_client_socket.send(pickle.dumps(len(data)))
        ftp_client_socket.send(data)

        self.data_list.insert(1,True)
        ftp_client_socket.close()
