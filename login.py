# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import win32con
import win32gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow
# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep



class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge()
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Şimdi Değil')]") \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Şimdi Değil')]") \
            .click()
        sleep(4)

    def searchHashtag(self, hashtag):
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag)

    def likePhotos(self, amount):
        self.driver.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i <= amount:
            time.sleep(7)
            self.driver.find_element_by_class_name("fr66n").click()
            self.driver.find_element_by_class_name("l8mY4").click()
            i += 1



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 592)
        Form.setStyleSheet("background-color: 0000;\n"
"")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(90, 20, 451, 531))
        self.groupBox.setStyleSheet("background-color: #FAFAFA;\n"
"border-radius: 15;\n"
"text-align: center;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        self.btn_login.setGeometry(QtCore.QRect(40, 420, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{background-color:#B2DFFC;\n"
"border-radius: 5;\n"
"color:white;\n"
"font-size: 15px;}\n"
"font-size: 15px;}\n"
"\n"
"QPushButton:hover{background-color:#0095F6;\n"
"border-radius: 5;\n"
"color:white;\n"
"font-size: 15px;}")
        self.btn_login.setObjectName("btn_login")
        self.txt_username = QtWidgets.QLineEdit(self.groupBox)
        self.txt_username.setGeometry(QtCore.QRect(80, 150, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_username.sizePolicy().hasHeightForWidth())
        self.txt_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid #717072;\n"
"color: #717072;\n"
"font-size: 20px;\n"
"padding-left:15px;\n"
"\n"
"")
        self.txt_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(self.groupBox)
        self.txt_password.setGeometry(QtCore.QRect(80, 220, 291, 41))
        self.txt_password.setStyleSheet("background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid #717072;\n"
"color: #717072;\n"
"font-size: 20px;\n"
"padding-left:15px;")
        self.txt_password.setInputMask("")
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 10, 341, 151))
        self.groupBox_2.setStyleSheet("background-color:transparent;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.img_insta = QtWidgets.QLabel(self.groupBox_2)
        self.img_insta.setGeometry(QtCore.QRect(20, 10, 331, 141))
        self.img_insta.setStyleSheet("background-color: transparent;\n"
"image: url(:/insta/images/instalogin.png);")
        self.img_insta.setText("")
        self.img_insta.setScaledContents(True)
        self.img_insta.setObjectName("img_insta")
        self.lbl_durum = QtWidgets.QLabel(self.groupBox)
        self.lbl_durum.setGeometry(QtCore.QRect(30, 480, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_durum.setFont(font)
        self.lbl_durum.setObjectName("lbl_durum")
        self.btn_Close = QtWidgets.QPushButton(self.groupBox)
        self.btn_Close.setGeometry(QtCore.QRect(420, 10, 20, 20))
        self.btn_Close.setStyleSheet("QPushButton{\n"
"background-color: #FD5754;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #37AED4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btn_Close.setText("")
        self.btn_Close.setObjectName("btn_Close")
        self.btn_Mini = QtWidgets.QPushButton(self.groupBox)
        self.btn_Mini.setGeometry(QtCore.QRect(400, 10, 20, 20))
        self.btn_Mini.setStyleSheet("QPushButton{\n"
"background-color: orange;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #37AED4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btn_Mini.setText("")
        self.btn_Mini.setObjectName("btn_Mini")
        self.txt_tag = QtWidgets.QLineEdit(self.groupBox)
        self.txt_tag.setGeometry(QtCore.QRect(80, 290, 291, 41))
        self.txt_tag.setStyleSheet("background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid #717072;\n"
"color: #717072;\n"
"font-size: 20px;\n"
"padding-left:15px;")
        self.txt_tag.setInputMask("")
        self.txt_tag.setText("")
        self.txt_tag.setObjectName("txt_tag")

        self.txt_likenumber = QtWidgets.QLineEdit(self.groupBox)
        self.txt_likenumber.setGeometry(QtCore.QRect(80, 360, 291, 41))
        self.txt_likenumber.setStyleSheet("background: transparent;\n"
                                   "    border: none;\n"
                                   "    border-bottom: 1px solid #717072;\n"
                                   "color: #717072;\n"
                                   "font-size: 20px;\n"
                                   "padding-left:15px;")
        self.txt_likenumber.setInputMask("")
        self.txt_likenumber.setText("")
        self.txt_likenumber.setObjectName("txt_likenumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_login.setText(_translate("Form", "LOGIN"))
        self.txt_username.setPlaceholderText(_translate("Form", "Username"))
        self.txt_password.setPlaceholderText(_translate("Form", "Password"))
        self.lbl_durum.setText(_translate("Form", "Durum: Başlamadı"))
        self.txt_tag.setPlaceholderText(_translate("Form", "Tag"))
        self.txt_likenumber.setPlaceholderText(_translate("Form", "Number of Likes"))



import source
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()

        self.show()

        self.ui.btn_Close.clicked.connect(self.close)
        self.ui.btn_Mini.clicked.connect(self.minimize)


        self.ui.btn_login.clicked.connect(self.startLike)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def close(self):
        sys.exit()

    def minimize(self):
        mini = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(mini, win32con.SW_MINIMIZE)


    def startLike(self):
        self.ui.lbl_durum.setText("Durum: Başladı")
        insta = InstaBot(self.ui.txt_username.text(), self.ui.txt_password.text())
        insta.searchHashtag(self.ui.txt_tag.text())
        insta.likePhotos(int(self.ui.txt_likenumber.text()))
        self.ui.lbl_durum.setText("Durum: Bitti")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    logg = Login()
    app.setWindowIcon(QtGui.QIcon("images/logo.png"))
    """QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)"""
    #MainForm.show()
    sys.exit(app.exec_())
