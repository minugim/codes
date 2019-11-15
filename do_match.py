# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'do_match.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

class do_match_ui(QtWidgets.QWidget):
    start_main_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(do_match_ui, self).__init__(parent)
        self._client=_client
        self.id_yours=''
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(750, 520)

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 671, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(320, 20, 331, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget.setObjectName("widget")
        self.label_pic1 = QtWidgets.QLabel(self.widget)
        self.label_pic1.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic1.setObjectName("label_pic1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_2.setObjectName("widget_2")
        self.label_pic2 = QtWidgets.QLabel(self.widget_2)
        self.label_pic2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic2.setObjectName("label_pic2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_3.setObjectName("widget_3")
        self.label_pic3 = QtWidgets.QLabel(self.widget_3)
        self.label_pic3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic3.setObjectName("label_pic3")
        self.tabWidget.addTab(self.tab_3, "")

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 271, 311))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_nickname = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname.setGeometry(QtCore.QRect(40, 50, 56, 12))
        self.label_nickname.setObjectName("label_nickname")
        self.label_residence = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.label_residence.setObjectName("label_residence")
        self.label_age = QtWidgets.QLabel(self.groupBox_2)
        self.label_age.setGeometry(QtCore.QRect(40, 200, 56, 12))
        self.label_age.setObjectName("label_age")
        self.label_hobby = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.label_hobby.setObjectName("label_hobby")
        self.label_nickname_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname_text.setGeometry(QtCore.QRect(150, 50, 56, 12))
        self.label_nickname_text.setObjectName("label")
        self.label_residence_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence_text.setGeometry(QtCore.QRect(150, 100, 56, 12))
        self.label_residence_text.setObjectName("label_residence_text")
        self.label_hobby_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby_text.setGeometry(QtCore.QRect(150, 150, 56, 12))
        self.label_hobby_text.setObjectName("label_hobby_text")
        self.label_age_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_age_text.setGeometry(QtCore.QRect(150, 200, 56, 12))
        self.label_age_text.setObjectName("label_age_text")
        self.like_button = QtWidgets.QPushButton(self.groupBox)
        self.like_button.setGeometry(QtCore.QRect(150, 370, 75, 41))
        self.like_button.setObjectName("like_button")
        self.pass_button = QtWidgets.QPushButton(self.groupBox)
        self.pass_button.setGeometry(QtCore.QRect(300, 370, 75, 41))
        self.pass_button.setObjectName("pass_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(450, 370, 75, 41))
        self.back_button.setObjectName("back_button")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.back_button.clicked.connect(self.back_button_clicked)
        self.pass_button.clicked.connect(self.pass_button_clicked)
        self.like_button.clicked.connect(self.like_button_clicked)

    def initiate_match(self):
        self._client.msg_list.append('initiate_match')
        self._client.msg_list.append(self._client.my_id)

        self._client.client_send()
        # recv ['initiate_match',True,내id, [상대id,nickname,residence,hobby,age,gender]]
        self._client.client_recv()
        can_match = self._client.msg_list_server[1]

        if can_match:
            print('match정보 도달')
            f = open('tmp_profile.txt', 'wb')
            f.write(pickle.dumps(self._client.msg_list_server[3]))
            f.close()

            self.label_nickname_text.setText(self._client.msg_list_server[3][1])
            self.label_residence_text.setText(self._client.msg_list_server[3][2])
            self.label_hobby_text.setText(self._client.msg_list_server[3][3])
            self.label_age_text.setText(self._client.msg_list_server[3][4])

            self.id_yours = self._client.msg_list_server[3][0]
            # ['img_recv',상대id,사진index]
            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(1)
            self._client.client_ftp_recv()

            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(2)
            self._client.client_ftp_recv()

            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(3)
            self._client.client_ftp_recv()

            self.label_pic1.setPixmap(QtGui.QPixmap('tmp1.jpg'))
            self.label_pic2.setPixmap(QtGui.QPixmap('tmp2.jpg'))
            self.label_pic3.setPixmap(QtGui.QPixmap('tmp3.jpg'))

        else:
            print('매치 가능한 사람이 없음')
            QtWidgets.QMessageBox.about(self, 'fail', 'no more person to match')
            self.back_button_clicked()

    def pass_button_clicked(self):
        # ['match_pass', 내id, 상대id]
        self._client.msg_list.append('match_pass')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)
        self.id_yours = ''
        self.initiate_match()

    def like_button_clicked(self):
        #['match_like', 내id, 상대id]
        self._client.msg_list.append('match_pass')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)
        self.id_yours = ''
        self.initiate_match()

    def back_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.id_yours=''
        self.start_main_signal.emit()
        self.close()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_pic1.setText(_translate("Form", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "사진1"))
        self.label_pic2.setText(_translate("Form", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "사진2"))
        self.label_pic3.setText(_translate("Form", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "사진3"))
        self.groupBox_2.setTitle(_translate("Form", "상대 프로필"))
        self.label_nickname.setText(_translate("Form", "nickname"))
        self.label_residence.setText(_translate("Form", "Residence"))
        self.label_age.setText(_translate("Form", "Age"))
        self.label_hobby.setText(_translate("Form", "Hobby"))
        self.label_nickname_text.setText(_translate("Form", "nickname"))
        self.label_residence_text.setText(_translate("Form", "residence"))
        self.label_hobby_text.setText(_translate("Form", "hobby"))
        self.label_age_text.setText(_translate("Form", "age"))
        self.like_button.setText(_translate("Form", "Like"))
        self.pass_button.setText(_translate("Form", "Pass"))
        self.back_button.setText(_translate("Form", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = do_match_ui(1)
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

