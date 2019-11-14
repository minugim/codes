from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

port = 5614


class CWidget(QWidget):
    def __init__(self):
        super().__init__()

        #self.c = client.ClientSocket(self)

        self.initUI()


    def initUI(self):
        self.resize(520,400)
        self.setWindowTitle('클라이언트')
        '''
        # 클라이언트 설정 부분
        ipbox = QHBoxLayout()
        
        gb = QGroupBox('서버 설정')
        ipbox.addWidget(gb)
        
        box = QHBoxLayout()

        label = QLabel('Server IP')
        self.ip = QLineEdit()
        self.ip.setInputMask('000.000.000.000;_')
        box.addWidget(label)
        box.addWidget(self.ip)

        label = QLabel('Server Port')
        self.port = QLineEdit(str(port))
        box.addWidget(label)
        box.addWidget(self.port)

        self.btn = QPushButton('접속')
        box.addWidget(self.btn)

        gb.setLayout(box)
        '''
        # 채팅창 부분
        infobox = QHBoxLayout()
        #gg = QGroupBox("채팅2")
        gb = QGroupBox('채팅')
        infobox.addWidget(gb)
        #infobox.addWidget(gg)

        box = QVBoxLayout()

        label = QLabel('메시지')
        #vertical_layout에 라벨 추가
        box.addWidget(label)

        self.recvmsg = QListWidget()
        # vertical_layout에 채팅창(리스트위젯) 추가
        box.addWidget(self.recvmsg)

        label = QLabel('보낼 메시지')
        # vertical_layout에 라벨 추가
        box.addWidget(label)

        self.sendmsg = QTextEdit()
        self.sendmsg.setFixedHeight(50)
        # vertical_layout에 채팅입력창(textedit) 추가
        box.addWidget(self.sendmsg)

        #버튼을 수평으로 배치하기위한 horizontal_layout
        hbox = QHBoxLayout()

        #기존의 vertical_layout에 버튼 두개를 포함하는 horizontal_layout 추가
        box.addLayout(hbox)
        self.sendbtn = QPushButton('보내기')
        self.sendbtn.setAutoDefault(True)

        self.clearbtn = QPushButton('나가기')

        hbox.addWidget(self.sendbtn)
        hbox.addWidget(self.clearbtn)
        gb.setLayout(box)

        # 전체 배치
        #vbox = QVBoxLayout()
        #vbox.addLayout(ipbox)
        #vbox.addLayout(infobox)
        #self.setLayout(vbox)
        self.setLayout(infobox)
        self.show()

    '''
    def connectClicked(self):
        if self.c.bConnect == False:
            ip = self.ip.text()
            port = self.port.text()
            if self.c.connectServer(ip, int(port)):
                self.btn.setText('접속 종료')
            else:
                self.c.stop()
                self.sendmsg.clear()
                self.recvmsg.clear()
                self.btn.setText('접속')
        else:
            self.c.stop()
            self.sendmsg.clear()
            self.recvmsg.clear()
            self.btn.setText('접속')
 
    def updateMsg(self, msg):
        self.recvmsg.addItem(QListWidgetItem(msg))
 
    def updateDisconnect(self):
        self.btn.setText('접속')
 
    def sendMsg(self):
        sendmsg = self.sendmsg.toPlainText()       
        self.c.send(sendmsg)        
        self.sendmsg.clear()
 
    def clearMsg(self):
        self.recvmsg.clear()
 
    def closeEvent(self, e):
        self.c.stop()
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())