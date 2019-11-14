# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import pickle

class profile_ui(QtWidgets.QWidget, QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()

    def __init__(self,_client,parent=None):
        super(profile_ui, self).__init__(parent)
        self._client=_client
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(750, 520)

        self.box = QtWidgets.QHBoxLayout()

        self.groupBox_2 = QtWidgets.QGroupBox()
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 331, 421))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_nickname = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname.setGeometry(QtCore.QRect(50, 80, 56, 12))
        self.label_nickname.setObjectName("label_nickname")
        self.editline_nickname = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_nickname.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.editline_nickname.setObjectName("editline_nickname")
        self.label_password = QtWidgets.QLabel(self.groupBox_2)
        self.label_password.setGeometry(QtCore.QRect(50, 140, 56, 12))
        self.label_password.setObjectName("label_password")
        self.label_hobby = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby.setGeometry(QtCore.QRect(50, 260, 56, 12))
        self.label_hobby.setObjectName("label_hobby")
        self.label_residence = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence.setGeometry(QtCore.QRect(50, 200, 61, 12))
        self.label_residence.setObjectName("label_residence")
        self.label_age = QtWidgets.QLabel(self.groupBox_2)
        self.label_age.setGeometry(QtCore.QRect(50, 320, 56, 12))
        self.label_age.setObjectName("label_age")

        self.editline_age = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_age.setGeometry(QtCore.QRect(160, 320, 113, 20))
        self.editline_age.setObjectName("editline_age")
        self.editline_residence = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_residence.setGeometry(QtCore.QRect(160, 200, 113, 20))
        self.editline_residence.setObjectName("editline_residence")
        self.editline_hobby = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_hobby.setGeometry(QtCore.QRect(160, 260, 113, 20))
        self.editline_hobby.setObjectName("editline_hobby")
        self.editline_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_password.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.editline_password.setObjectName("editline_password")
        self.revise_button = QtWidgets.QPushButton(self.groupBox_2)
        self.revise_button.setGeometry(QtCore.QRect(80, 400, 81, 31))
        self.revise_button.setObjectName("revise_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox_2)
        self.back_button.setGeometry(QtCore.QRect(220, 400, 81, 31))
        self.back_button.setObjectName("back_button")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(360, 30, 371, 421))
        self.groupBox.setObjectName("groupBox")
        self.erase_pic_button = QtWidgets.QPushButton(self.groupBox)
        self.erase_pic_button.setGeometry(QtCore.QRect(250, 390, 75, 23))
        self.erase_pic_button.setObjectName("erase_pic_button")
        self.find_button = QtWidgets.QPushButton(self.groupBox)
        self.find_button.setGeometry(QtCore.QRect(150, 390, 75, 21))
        self.find_button.setObjectName("find_button")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 331, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget.setObjectName("widget")
        self.pic_1 = QtWidgets.QLabel(self.widget)
        self.pic_1.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_1.setObjectName("pic_1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_2.setObjectName("widget_2")
        self.pic_2 = QtWidgets.QLabel(self.widget_2)
        self.pic_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_2.setObjectName("pic_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_3.setObjectName("widget_3")
        self.pic_3 = QtWidgets.QLabel(self.widget_3)
        self.pic_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_3.setObjectName("pic_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.revise_pic_button = QtWidgets.QPushButton(self.groupBox)
        self.revise_pic_button.setGeometry(QtCore.QRect(50, 390, 71, 21))
        self.revise_pic_button.setObjectName("revise_pic_button")
        self.editline_filepath = QtWidgets.QLineEdit(self.groupBox)
        self.editline_filepath.setGeometry(QtCore.QRect(20, 350, 331, 20))
        self.editline_filepath.setObjectName("editline_filepath")

        self.box.addWidget(self.groupBox_2)
        self.box.addWidget(self.groupBox)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.box)

        self.back_button.clicked.connect(self.back_button_clicked)
        self.find_button.clicked.connect(self.find_button_clicked)
        self.revise_pic_button.clicked.connect(self.revise_pic_button_clicked)
        self.erase_pic_button.clicked.connect(self.erase_pic_button_clicked)
        self.revise_button.clicked.connect(self.revise_button_clicked)

    def revise_button_clicked(self):
        tmp_list=[]
        tmp_list.append(self._client.my_id)
        tmp_list.append(self.editline_password.text())
        tmp_list.append(self.editline_residence.text())
        tmp_list.append(self.editline_hobby.text())
        tmp_list.append(self.editline_age.text())
        tmp_list.append(self.editline_nickname.text())
        fread = open(self._client.my_dir + '/my_profile.txt', 'rb')
        if tmp_list == pickle.loads(fread.read()):
            fread.close()
            QtWidgets.QMessageBox.about(self, 'revise failed', 'same with old profile')
            return
        else:
            fwrite = open(self._client.my_dir+'/my_profile.txt','wb')
            fwrite.write(pickle.dumps(tmp_list))
            fwrite.close()
            fread.close()
            QtWidgets.QMessageBox.about(self, 'revise success', 'your profile changed')

        self._client.msg_list.append('new_profile')
        self._client.msg_list.append(tmp_list)
        self._client.client_send()
        self._client.client_recv()

    def erase_pic_button_clicked(self):
        fread = open('base_image.jpg','rb')
        fwrite = open(self._client.my_dir+'/me'+str(self.tabWidget.currentIndex()+1)+'.jpg','wb')
        fwrite.write(fread.read())
        fread.close()
        fwrite.close()
        self.pic_1.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me1.jpg'))
        self.pic_2.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me2.jpg'))
        self.pic_3.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me3.jpg'))

    def revise_pic_button_clicked(self):
        #print(self._client.my_id)
        if not self.editline_filepath.text():
            QtWidgets.QMessageBox.about(self, 'revise failed', 'select a picture')
            return
        else:
            self._client.img_resize(self.editline_filepath.text())
            fread = open('resized.jpg','rb')
            fwrite = open(self._client.my_dir+'/me'+str(self.tabWidget.currentIndex()+1)+'.jpg','wb')
            fwrite.write(fread.read())
            fread.close()
            fwrite.close()
            self._client.msg_list.append('img_send')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(self.tabWidget.currentIndex()+1)
            print('이미지 보내기')
            print(self._client.msg_list)
            self._client.client_send()
            self._client.img_send('resized.jpg')
            self._client.client_recv()
            self.pic_1.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me1.jpg'))
            self.pic_2.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me2.jpg'))
            self.pic_3.setPixmap(QtGui.QPixmap(self._client.my_dir + '/me3.jpg'))

    def back_button_clicked(self):
        '''
        tmp = self._client.number_of_widgets - 1
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if not tmp:
            self._client.msg_list.append('close_thread')
            self._client.client_send()
        else:
        '''
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_main_signal.emit()
        self.close()

    def find_button_clicked(self):
        #print(self.tabWidget.currentIndex())
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.editline_filepath.setText(fname[0])
        if os.path.getsize(fname[0]) == 0:
            QtWidgets.QMessageBox.about(self, 'fail', 'select another file')
            return


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.back_button.setText(_translate("Form", "돌아가기"))
        self.groupBox.setTitle(_translate("Form", "내 프로필 사진"))
        self.erase_pic_button.setText(_translate("Form", "사진삭제"))
        self.find_button.setText(_translate("Form", "사진찾기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "사진1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "사진2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "사진3"))
        self.revise_pic_button.setText(_translate("Form", "사진수정"))
        self.groupBox_2.setTitle(_translate("Form", "내 프로필"))

        self.label_age.setText(_translate("Form", "age"))
        self.label_nickname.setText(_translate("Form", "nickname"))
        #self.editline_nickname.setText(_translate("Form", "my_nickname"))
        self.label_password.setText(_translate("Form", "Password"))
        self.label_hobby.setText(_translate("Form", "Hobby"))
        self.label_residence.setText(_translate("Form", "Residence"))
        #self.editline_residence.setText(_translate("Form", "my_residence"))
        #self.editline_hobby.setText(_translate("Form", "my_hobby"))
        #self.editline_password.setText(_translate("Form", "empty"))
        self.revise_button.setText(_translate("Form", "수정"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = profile_ui(1)
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

