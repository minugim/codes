import socket
import sys
import os
from PyQt5.QtCore import QThread
import cloudpickle
import copy
import base64
import pickle
from PIL import Image


# [ 'img_send', id , file_size , pic_number ]
'''
msg_list format:
login_info : [instruction, args]
join_info : [instruction, args]
'''


class client(QThread):

    def __init__(self):
        super().__init__()
        self.host = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host)
        self.port = 5555
        self.ftp_port = 6666
        self.instruction = ' '
        self.msg_list = []
        self.number_of_widgets = 0
        self.my_id = ''
        self.my_dir = os.getcwd()+'/id_'
        #self.login_success = False
        self.msg_list_server = []
        self.instruction_server = ' '

        print('connecting to %d port' % self.port)
        self.server_addr = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect(self.server_addr)

    def client_ftp_send(self,filepath):
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_send()
        self.ftp_sock.connect(self.ftp_server_addr)

        f = open(filepath,'rb')
        data=f.read()
        f.close()
        self.ftp_sock.send(data)
        self.ftp_sock.close()
        self.client_recv()

    def client_ftp_recv(self):
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        pic_index = self.msg_list[2]
        self.client_send()
        self.ftp_sock.connect(self.ftp_server_addr)
        print('받을게요')
        size = pickle.loads(self.ftp_sock.recv(1024))
        recvd=0
        fwrite = open('tmp' + str(pic_index) + '.jpg', 'wb')
        while size > recvd:
            data = self.ftp_sock.recv(4096)
            tmp = len(data)
            recvd = recvd + tmp
            fwrite.write(data)
            print(tmp)
        fwrite.close()
        self.ftp_sock.close()
        self.client_recv()

    def client_send(self):
        print("sending {0}".format(self.msg_list))
        print(pickle.dumps(self.msg_list))
        self.sock.send(pickle.dumps(self.msg_list))  # send(bytes) returns the number of bytes sent
        self.instruction = ' '
        self.msg_list = []
        # self.client_recv()

    def client_recv(self):
        data = self.sock.recv(2048)
        data = pickle.loads(data)
        self.msg_list_server = copy.deepcopy(data)
        print(f'recv {data}')

    def img_send(self, file_path):
        f = open(file_path, 'rb')
        data = f.read()
        self.sock.send(pickle.dumps(len(data)))
        print(len(data))
        self.sock.send(data)
        f.close()
        print('보냄')

    def img_recv(self, file_bytes, file_name):
        pass

    def mkdir(self):
        dir_path = os.getcwd() + '/id_' + self.msg_list_server[2]
        try:
            if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))
        except OSError:
            print('failed to mkdir' + self.msg_list_server[2])
            return
        try:
            if not (os.path.isdir(dir_path+'/match')):
                os.makedirs(os.path.join(dir_path+'/match'))

        except OSError:
            print('failed to mkdir' + self.msg_list_server[2]+'/match')
            return

    def img_resize(self,file_path):
        source_image = file_path
        target_image = 'resized.jpg'
        image = Image.open(source_image)
        image = image.convert('RGB')
        image.save(target_image)
        # resize 할 이미지 사이즈
        resize_image = image.resize((330, 300))
        # 저장할 파일 Type : JPEG, PNG 등
        # 저장할 때 Quality 수준 : 보통 95 사용
        resize_image.save(target_image, mode='jpg', quality=95)

    def img_size(self,filepath):
        f = open(filepath,'rb')
        size = len(f.read())
        f.close()
        return size

    def run(self):
        while True:
            self.client_send()
            # self.client_recv()


if __name__ == '__main__':
    app = QApplication()
    myWindow = My
    # myWindow.show()
    # app.exec_()
    id = myWindow.editline_id.text()
    # my_thread = threading.Thread(target=run, args=(myWindow,))
    # my_thread.start()
    # time.sleep(5)
