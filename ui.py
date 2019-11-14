import sys
import os
from PyQt5 import QtWidgets, QtGui
import Client
from PyQt5 import QtCore
import pickle
import join
import login
import profile
import main


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self._client = Client.client()

        self.login_uii = login.login_ui(self._client)
        self.join_uii = join.join_ui(self._client)
        self.main_uii = main.main_ui(self._client)
        self.profile_uii = profile.profile_ui(self._client)

        self.login_uii.start_main_signal.connect(self.startMainUI)
        self.login_uii.start_join_signal.connect(self.startJoinUI)
        self.main_uii.my_profile_button.clicked.connect(self.startProfileUI)
        self.profile_uii.start_main_signal.connect(self.startMainUI)
        self.join_uii.start_login_signal.connect(self.startLoginUI)
        '''
        self.main_uii.do_match_button.clicked.connect(self.startDomatchUI)
        self.main_uii.my_match_button.clicked.connect(self.startMymatchUI)
        self.main_uii.statistics_button.clicked.connect(self.startStatisticsUI)
        self.main_uii.random_chat_button.clicked.connect(self.startRandomchatUI)
        '''
        #self._client.start()

        self.startLoginUI()

    def startLoginUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.login_uii.show()

    def startJoinUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.join_uii.show()

    def startMainUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.main_uii.count_users()
        self.main_uii.show()

    def startProfileUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.main_uii.close_button_clicked()
        self.profile_uii.pic_1.setPixmap(QtGui.QPixmap(self._client.my_dir + '/' + 'me1.jpg'))
        self.profile_uii.pic_2.setPixmap(QtGui.QPixmap(self._client.my_dir + '/' + 'me2.jpg'))
        self.profile_uii.pic_3.setPixmap(QtGui.QPixmap(self._client.my_dir + '/' + 'me3.jpg'))
        f = open(self._client.my_dir+'/my_profile.txt','rb')
        profile = pickle.loads(f.read())
        f.close()
        self.profile_uii.editline_nickname.setText(profile[5])
        self.profile_uii.editline_password.setText(profile[1])
        self.profile_uii.editline_residence.setText(profile[2])
        self.profile_uii.editline_hobby.setText(profile[3])
        self.profile_uii.editline_age.setText(profile[4])
        self.profile_uii.show()
    '''
    def startDomatchUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.do_match_uii.show()
        
    def startMymatchUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.my_match_uii.show()
        
    def startStatisticsUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.statistics_uii.show()
    
    def startRandomchatUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.random_chat_uii.show()
    '''

'''
class loginUI(QtWidgets.QWidget, join):
    def __init__(self, _client, parent=None):
        super(loginUI, self).__init__(parent)
        self._client=_client
        
        #login_ui = resource_path("./login.ui")
        #uic.loadUi(login_ui, self)
        #QPushButton signal, 생성자 내부에 작성돼야함
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.login_button.clicked.connect(self.login_button_clicked)
        #self.join_button.clicked.connect(self.join_button_clicked)
        self.editline_password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def exit_button_clicked(self):
        QtWidgets.QMessageBox.about(self, "exit", "종료합니다")
        self.close()

    def login_button_clicked(self):
        QtWidgets.QMessageBox.about(self, "login", "로그인 합니다")
        self._client.id = self.editline_id.text()
    
    def setUpUI(self):
        self.show()
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
