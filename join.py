# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, uic
import pickle
import copy


class join_ui(QtWidgets.QWidget,QtCore.QObject):
    start_login_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(join_ui, self).__init__(parent)
        QtCore.QObject.__init__(self)
        self._client = _client
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(750, 520)

        self.join_interface = QtWidgets.QHBoxLayout()
        gb = QtWidgets.QGroupBox('회원가입')
        self.join_interface.addWidget(gb)
        self.join_box = QtWidgets.QVBoxLayout()
        gb1=QtWidgets.QGroupBox('정보')
        #gb2=QtWidgets.QGroupBox('사진')
        self.join_info_box = QtWidgets.QHBoxLayout()
        self.join_text = QtWidgets.QHBoxLayout()
        self.join_text_label = QtWidgets.QVBoxLayout()
        #self.join_text_label.setContentsMargins(0,0,0,0)
        self.join_text_edit = QtWidgets.QVBoxLayout()
        #self.join_text_edit.setContentsMargins(0, 0, 0, 0)
        self.join_pic = QtWidgets.QVBoxLayout()
        self.join_buttons = QtWidgets.QHBoxLayout()
        self.join_radio = QtWidgets.QHBoxLayout()

        self.male_radio = QtWidgets.QRadioButton('남성',self)
        self.male_radio.setChecked(True)
        self.female_radio = QtWidgets.QRadioButton('여성', self)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(190, 310, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_5.setFixedSize(100,20)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(190, 370, 56, 12))
        self.label_6.setObjectName("label_6")
        self.label_6.setFixedSize(100, 20)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(100, 20)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(190, 250, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFixedSize(100, 20)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(530, 200, 150, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setFixedSize(150, 20)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(190, 130, 56, 12))
        self.label.setObjectName("label")
        self.label.setFixedSize(100, 20)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(190, 430, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setFixedSize(100, 20)

        self.join_button = QtWidgets.QPushButton(self)
        self.join_button.setGeometry(QtCore.QRect(230, 440, 81, 31))
        self.join_button.setObjectName("join_button")

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(390, 440, 81, 31))
        self.close_button.setObjectName("close_button")

        self.find_button = QtWidgets.QPushButton(self)
        self.find_button.setGeometry(QtCore.QRect(540, 300, 81, 31))
        self.find_button.setObjectName("find_button")

        self.editline_id = QtWidgets.QLineEdit(self)
        self.editline_id.setGeometry(QtCore.QRect(300, 130, 113, 20))
        self.editline_id.setObjectName("editline_id")
        self.editline_id.setFixedSize(200,30)

        self.editline_password = QtWidgets.QLineEdit(self)
        self.editline_password.setGeometry(QtCore.QRect(300, 190, 113, 20))
        self.editline_password.setObjectName("editline_password")
        self.editline_password.setFixedSize(200,30)

        self.editline_residence = QtWidgets.QLineEdit(self)
        self.editline_residence.setGeometry(QtCore.QRect(300, 250, 113, 20))
        self.editline_residence.setObjectName("editline_residence")
        self.editline_residence.setFixedSize(200,30)

        self.editline_hobby = QtWidgets.QLineEdit(self)
        self.editline_hobby.setGeometry(QtCore.QRect(300, 310, 113, 20))
        self.editline_hobby.setObjectName("editline_hobby")
        self.editline_hobby.setFixedSize(200,30)

        self.editline_age = QtWidgets.QLineEdit(self)
        self.editline_age.setGeometry(QtCore.QRect(300, 370, 113, 20))
        self.editline_age.setObjectName("editline_age")
        self.editline_age.setFixedSize(200,30)

        self.editline_nickname = QtWidgets.QLineEdit(self)
        self.editline_nickname.setGeometry(QtCore.QRect(300, 430, 113, 20))
        self.editline_nickname.setObjectName("editline_nickname")
        self.editline_nickname.setFixedSize(200, 30)

        self.editline_filepath = QtWidgets.QLineEdit(self)
        self.editline_filepath.setGeometry(QtCore.QRect(500, 250, 160, 20))
        self.editline_filepath.setObjectName("editline_filepath")
        self.editline_filepath.setFixedSize(200,30)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.join_button.clicked.connect(self.join_button_clicked)
        self.close_button.clicked.connect(self.close_button_clicked)
        self.find_button.clicked.connect(self.find_button_clicked)

        self.join_text_label.addWidget(self.label)
        self.join_text_label.addWidget(self.label_2)
        self.join_text_label.addWidget(self.label_4)
        self.join_text_label.addWidget(self.label_5)
        self.join_text_label.addWidget(self.label_6)
        self.join_text_label.addWidget(self.label_8)

        self.join_text_edit.addWidget(self.editline_id)
        self.join_text_edit.addWidget(self.editline_password)
        self.join_text_edit.addWidget(self.editline_residence)
        self.join_text_edit.addWidget(self.editline_hobby)
        self.join_text_edit.addWidget(self.editline_age)
        self.join_text_edit.addWidget(self.editline_nickname)

        self.join_radio.addWidget(self.male_radio)
        self.join_radio.addWidget(self.female_radio)

        self.join_pic.addLayout(self.join_radio)
        self.join_pic.addWidget(self.label_7)
        self.join_pic.addWidget(self.editline_filepath)
        self.join_pic.addWidget(self.find_button)

        self.join_text.addLayout(self.join_text_label)
        self.join_text.addLayout(self.join_text_edit)
        gb1.setLayout(self.join_text)
        #gb2.setLayout(self.join_pic)

        self.join_info_box.addWidget(gb1)
        #self.join_info_box.addWidget(gb2)
        self.join_info_box.addLayout(self.join_pic)

        self.join_buttons.addWidget(self.join_button)
        self.join_buttons.addWidget(self.close_button)

        self.join_box.addLayout(self.join_info_box)
        self.join_box.addLayout(self.join_buttons)

        gb.setLayout(self.join_box)
        self.setLayout(self.join_interface)

    # 파일 경로를 찾으면 copy를 생성하고 join_button_clicked가 호출되면 사진정보도 보내줌
    def find_button_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open  file', './')
            if not fname:
                return
            self.editline_filepath.setText(fname[0])

            if os.path.getsize(fname[0]) == 0:
                QtWidgets.QMessageBox.about(self, 'fail', 'select another file')
                return

        except Exception as e:
            print(e)
            return

    def join_button_clicked(self):
        #self._client.msg_list.append('join_info')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self.editline_password.text())
        self._client.msg_list.append(self.editline_residence.text())
        self._client.msg_list.append(self.editline_hobby.text())
        self._client.msg_list.append(self.editline_age.text())
        self._client.msg_list.append(self.editline_nickname.text())
        if self.male_radio.isChecked():
            self._client.msg_list.append('남성')
        else:
            self._client.msg_list.append('여성')

        tmp_list = copy.deepcopy(self._client.msg_list)
        self._client.msg_list.insert(0,'join_info')
        if self.editline_filepath.text() and self.editline_id.text() and self.editline_password.text() and self.editline_residence.text() and self.editline_hobby.text() and self.editline_age.text() and self.editline_nickname.text() :
            self._client.client_send()
            self._client.client_recv()
            print("recving list")
        else:
            QtWidgets.QMessageBox.about(self, 'join fail', 'fill the empty space')
            return

        if self._client.msg_list_server[1]:
            self._client.mkdir()
            f = open(os.getcwd() + '/id_' + self.editline_id.text() + '/my_profile.txt', 'wb')
            f.write(pickle.dumps(tmp_list))
            f.close()
            QtWidgets.QMessageBox.about(self, 'join success', 'welcome to here')
        else:
            QtWidgets.QMessageBox.about(self, 'join failed', 'ID already exists')
            return
        print(self._client.msg_list_server[1])


        self._client.img_resize(self.editline_filepath.text())
        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('resized.jpg'))
        self._client.msg_list.append(1)
        self._client.client_ftp_send('resized.jpg')
        #self._client.img_send('resized.jpg')
        fp = open('resized.jpg','rb')
        f = open(os.getcwd()+'/id_'+self.editline_id.text()+'/me1.jpg','wb')
        f.write(fp.read())
        f.close()
        fp.close()

        self._client.img_resize('base_image.png')
        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('resized.jpg'))
        self._client.msg_list.append(2)
        self._client.client_ftp_send('resized.jpg')
        #self._client.img_send('base_image.jpg')
        #self._client.client_recv()
        fp = open('resized.jpg', 'rb')
        fread = fp.read()
        fp.close()
        f = open(os.getcwd() + '/id_' + self.editline_id.text() + '/me2.jpg', 'wb')
        f.write(fread)
        f.close()

        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('resized.jpg'))
        self._client.msg_list.append(3)
        self._client.client_ftp_send('resized.jpg')
        #self._client.img_send('base_image.jpg')
        #self._client.client_recv()
        f = open(os.getcwd() + '/id_' + self.editline_id.text() + '/me3.jpg', 'wb')
        f.write(fread)
        f.close()
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_login_signal.emit()
        self.close()

    def close_button_clicked(self):
        '''
        tmp = self._client.number_of_widgets -1
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if not tmp:
            self._client.msg_list.append('close_thread')
            self._client.client_send()
        '''
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_login_signal.emit()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "회원가입"))
        self.label_5.setText(_translate("Form", "Hobby"))
        #self.label_3.setText(_translate("Form", "Insert Your Profile"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Residence"))
        self.label_6.setText(_translate("Form", "Age"))
        self.label_8.setText(_translate("Form","Nickname"))
        self.label_7.setText(_translate("Form", "*register your picture"))
        self.label.setText(_translate("Form", "ID"))
        self.join_button.setText(_translate("Form", "Join"))
        self.close_button.setText(_translate("Form", "Close"))
        self.find_button.setText(_translate("Form", "Find path"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    ui = join_ui(1)
    #ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
