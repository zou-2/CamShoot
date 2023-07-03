# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginVertDegradeAKZtpT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# import logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 465)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 590, 420))
        self.widget.setStyleSheet(u"QPushButton#seConnecter{\n"
"	background-color: rgba(85, 98, 112, 255);\n"
"	color: rgba(255, 255, 255, 200);	\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#seConnecter:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color: #8fe31c;\n"
"	background-position: calc(100%  - 10px)center;\n"
"}\n"
"\n"
"QPushButton#seConnecter:hover{\n"
"	background-color: #8fe31c;\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 40, 260, 330))
        self.label.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 25, 270, 360))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #8fe31c, stop:1 #008102);\n"
"border-radius: 15px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 80, 121, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(0,0,0,200);")
        self.inputUser = QLineEdit(self.widget)
        self.inputUser.setObjectName(u"inputUser")
        self.inputUser.setGeometry(QRect(330, 140, 190, 40))
        font1 = QFont()
        font1.setPointSize(9)
        self.inputUser.setFont(font1)
        self.inputUser.setStyleSheet(u"background-color: rgb(0,0 , 0, 0);\n"
"border: 2px solid rgb(0,0 , 0, 0);\n"
"border-bottom-color: rgb(46,82 , 101, 200);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.inputPswrd = QLineEdit(self.widget)
        self.inputPswrd.setObjectName(u"inputPswrd")
        self.inputPswrd.setGeometry(QRect(330, 220, 190, 40))
        self.inputPswrd.setFont(font1)
        self.inputPswrd.setStyleSheet(u"background-color: rgb(0,0 , 0, 0);\n"
"border: 2px solid rgb(0,0 , 0, 0);\n"
"border-bottom-color: rgb(46,82 , 101, 200);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.inputPswrd.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 90, 61, 71))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 200, 121, 121))
        self.label_5.setStyleSheet(u"color: #8fe31c;")
        self.seConnecter = QPushButton(self.widget)
        self.seConnecter.setObjectName(u"seConnecter")
        self.seConnecter.setGeometry(QRect(330, 300, 191, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.seConnecter.setFont(font2)

        self.retranslateUi(Form)
        
        self.seConnecter.clicked.connect(self.Connexion)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    def Connexion(self):
            #eto code connexion
            
            
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Connexion", None))
        self.inputUser.setPlaceholderText(QCoreApplication.translate("Form", u"nom d'utilisateur", None))
        self.inputPswrd.setPlaceholderText(QCoreApplication.translate("Form", u"mot de passe", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/Pictures/logo.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/Pictures/masque.png\"/></p></body></html>", None))
        self.seConnecter.setText(QCoreApplication.translate("Form", u"Se connecter", None))
    # retranslateUi

