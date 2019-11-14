# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QAction, qApp
from PyQt5.QtGui import QIcon
import copy


class login_ui(QtWidgets.QWidget, QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()
    start_join_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(login_ui, self).__init__(parent)
        QtCore.QObject.__init__(self)
        self._client = _client
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(750, 520)

        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setGeometry(QtCore.QRect(150, 330, 111, 61))
        self.login_button.setObjectName("login_button")
        self.login_button.setFixedSize(100, 50)

        self.join_button = QtWidgets.QPushButton(self)
        self.join_button.setGeometry(QtCore.QRect(315, 330, 101, 61))
        self.join_button.setObjectName("join_button")
        self.join_button.setFixedSize(100,50)

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(QtCore.QRect(480, 330, 111, 61))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setFixedSize(100, 50)

        self.label_id = QtWidgets.QLabel(self)
        self.label_id.setGeometry(QtCore.QRect(140, 100, 56, 12))
        self.label_id.setObjectName("label_id")
        self.label_id.setFixedSize(150, 30)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setGeometry(QtCore.QRect(140, 200, 56, 12))
        self.label_password.setObjectName("label_password")
        self.label_password.setFixedSize(150,30)

        self.editline_id = QtWidgets.QLineEdit(self)
        self.editline_id.setGeometry(QtCore.QRect(290, 80, 161, 51))
        self.editline_id.setText("")
        self.editline_id.setObjectName("editline_id")
        self.editline_id.setFixedSize(300,30)


        self.editline_password = QtWidgets.QLineEdit(self)
        self.editline_password.setGeometry(QtCore.QRect(290, 180, 161, 51))
        self.editline_password.setText("")
        self.editline_password.setObjectName("editline_password")
        self.editline_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editline_password.setFixedSize(300,30)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.login_button.clicked.connect(self.login_button_clicked)
        self.join_button.clicked.connect(self.join_button_clicked)
        self.exit_button.clicked.connect(self.exit_button_clicked)

        login_ = QtWidgets.QVBoxLayout()
        gb = QtWidgets.QGroupBox('로그인')
        login_.addWidget(gb)

        login_interface = QtWidgets.QVBoxLayout()
        login_box = QtWidgets.QHBoxLayout()
        login_label = QtWidgets.QVBoxLayout()
        login_text = QtWidgets.QVBoxLayout()
        login_button = QtWidgets.QHBoxLayout()

        login_box.addLayout(login_label)
        login_box.addLayout(login_text)
        login_interface.addLayout(login_box)
        login_interface.addLayout(login_button)

        login_button.addWidget(self.login_button)
        login_button.addWidget(self.join_button)
        login_button.addWidget(self.exit_button)

        login_label.addWidget(self.label_id)
        login_label.addWidget(self.label_password)

        login_text.addWidget(self.editline_id)
        login_text.addWidget(self.editline_password)

        gb.setLayout(login_interface)
        self.setLayout(login_)


    def login_button_clicked(self):
        self._client.msg_list.append('login_info')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self.editline_password.text())
        #self._client.instruction = 'login_info'
        self._client.client_send()
        self._client.client_recv()
        if self._client.msg_list_server[1]:
            QtWidgets.QMessageBox.about(self, 'login success', 'welcome to here')
            self._client.mkdir()
            self._client.my_id = copy.deepcopy(self.editline_id.text())
            self._client.my_dir = self._client.my_dir + self._client.my_id
            self._client.number_of_widgets = self._client.number_of_widgets - 1
            self.start_main_signal.emit()
            self.close()
        else:
            QtWidgets.QMessageBox.about(self, 'login failed', 'confirm your id and password or join')

    def join_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_join_signal.emit()
        self.close()

    def exit_button_clicked(self):
        tmp = self._client.number_of_widgets - 1
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if not tmp:
            self._client.msg_list.append('close_thread')
            self._client.client_send()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "application name"))
        self.join_button.setText(_translate("Form", "join"))
        self.label_password.setText(_translate("Form", "Password"))
        self.exit_button.setText(_translate("Form", "exit"))
        self.label_id.setText(_translate("Form", "ID"))
        self.login_button.setText(_translate("Form", "login"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    ui = login_ui(1)
    ui.show()
    sys.exit(app.exec_())
