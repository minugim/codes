# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class main_ui(QtWidgets.QWidget):
    def __init__(self,_client,parent=None):
        super(main_ui,self).__init__(parent)
        self._client=_client
        self.number_of_users=0
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(750, 520)

        self.my_profile_button = QtWidgets.QPushButton(self)
        self.my_profile_button.setGeometry(QtCore.QRect(40, 460, 75, 41))
        self.my_profile_button.setObjectName("my_profile_button")
        self.do_match_button = QtWidgets.QPushButton(self)
        self.do_match_button.setGeometry(QtCore.QRect(150, 460, 75, 41))
        self.do_match_button.setObjectName("do_match_button")
        self.my_match_button = QtWidgets.QPushButton(self)
        self.my_match_button.setGeometry(QtCore.QRect(260, 460, 75, 41))
        self.my_match_button.setObjectName("my_match_button")
        self.statistics_button = QtWidgets.QPushButton(self)
        self.statistics_button.setGeometry(QtCore.QRect(370, 460, 75, 41))
        self.statistics_button.setObjectName("statistics_button")
        self.random_chat_button = QtWidgets.QPushButton(self)
        self.random_chat_button.setGeometry(QtCore.QRect(480, 460, 101, 41))
        self.random_chat_button.setObjectName("random_chat_button")
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(620, 460, 75, 41))
        self.close_button.setObjectName("close_button")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 481, 421))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 451, 370))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.editline_notice1 = QtWidgets.QLineEdit(self.tab)
        self.editline_notice1.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice1.setObjectName("editline_notice1")
        self.editline_title1 = QtWidgets.QLineEdit(self.tab)
        self.editline_title1.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title1.setObjectName("editline_title1")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.editline_notice2 = QtWidgets.QLineEdit(self.tab_2)
        self.editline_notice2.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice2.setObjectName("editline_notice2")
        self.editline_title2 = QtWidgets.QLineEdit(self.tab_2)
        self.editline_title2.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title2.setObjectName("editline_title2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.editline_title3 = QtWidgets.QLineEdit(self.tab_3)
        self.editline_title3.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title3.setObjectName("editline_title3")
        self.editline_notice3 = QtWidgets.QLineEdit(self.tab_3)
        self.editline_notice3.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice3.setObjectName("editline_notice3")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.editline_title4 = QtWidgets.QLineEdit(self.tab_4)
        self.editline_title4.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title4.setObjectName("editline_title4")
        self.editline_notice4 = QtWidgets.QLineEdit(self.tab_4)
        self.editline_notice4.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice4.setObjectName("editline_notice4")
        self.tabWidget.addTab(self.tab_4, "")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self)
        self.dateTimeEdit.setGeometry(QtCore.QRect(510, 60, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_num_clients = QtWidgets.QLabel(self)
        self.label_num_clients.setGeometry(QtCore.QRect(520, 110, 101, 16))
        self.label_num_clients.setObjectName("label_num_clients")
        self.label_num_clients_2 = QtWidgets.QLabel(self)
        self.label_num_clients_2.setGeometry(QtCore.QRect(640, 110, 56, 12))
        self.label_num_clients_2.setObjectName("label_num_clients_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 160, 241, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.editline_vote = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_vote.setGeometry(QtCore.QRect(10, 30, 221, 81))
        self.editline_vote.setObjectName("editline_vote")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(80, 130, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 170, 90, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.submit_Button = QtWidgets.QPushButton(self.groupBox_2)
        self.submit_Button.setGeometry(QtCore.QRect(80, 210, 75, 23))
        self.submit_Button.setObjectName("submit_Button")


        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.close_button.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        tmp = self._client.number_of_widgets - 1
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if not tmp:
            self._client.msg_list.append('close_thread')
            self._client.client_send()
        self.close()

    def count_users(self):
        self._client.msg_list.append('count_users')
        self._client.client_send()
        self._client.client_recv()
        self.number_of_users = self._client.msg_list_server[1]
        self.label_num_clients_2.setText(str(self.number_of_users)+'명')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.my_profile_button.setText(_translate("Form", "my_profile"))
        self.do_match_button.setText(_translate("Form", "do_match"))
        self.my_match_button.setText(_translate("Form", "my_match"))
        self.statistics_button.setText(_translate("Form", "statistics"))
        self.random_chat_button.setText(_translate("Form", "random_chat"))
        self.close_button.setText(_translate("Form", "close"))

        self.groupBox.setTitle(_translate("Form", "공지사항"))
        self.editline_notice1.setText(_translate("Form", "a"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.editline_notice2.setText(_translate("Form", "b"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.editline_notice3.setText(_translate("Form", "c"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Tab 3"))
        self.editline_notice4.setText(_translate("Form", "d"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Tab 4"))
        self.label_num_clients.setText(_translate("Form", "현재 접속자 수 :"))
        self.label_num_clients_2.setText(_translate("Form", "xxx 명"))
        self.groupBox_2.setTitle(_translate("Form", "투표"))
        self.submit_Button.setText(_translate("Form", "제출하기"))
        self.radioButton_2.setText(_translate("Form", "2번 선택지"))
        self.editline_vote.setText(_translate("Form", "투표를 통해 선호도를 조사해서 그룹을 묶은다음, 매치에 뜨는 사람에 반영함"))
        self.radioButton.setText(_translate("Form", "1번 선택지"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = main_ui(1)
    ui.show()
    sys.exit(app.exec_())

