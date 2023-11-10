import datetime
import sys
from PIL import Image
from keras.models import load_model
import numpy as np
from numpy import asarray
from numpy import expand_dims
import pickle
import cv2
import sqlite3
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from facial.logic import face_detector
from facial.services.model_singleton import ModelSingleton
# from facial.services.model_singleton import ModelSingleton
# from facial.logic.face_detector import face_detector
# from services.model_singleton import ModelSingleton

import time
from PySide2 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal


import resources_rc

class Worker(QThread):
    finished = pyqtSignal()
    
    def run(self):
        import Get_BD
        
        self.finished.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 494)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"QLineEdit{\n"
" background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:#1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"\n"
"#frame_4, #frame_8,#popupNotificationSubContainer{\n"
"	background-color:#16191d;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#headerContainer,#footerContainer{\n"
"	background-color:#2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(12)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.accueilBtn = QPushButton(self.frame_2)
        self.accueilBtn.setObjectName(u"accueilBtn")
        self.accueilBtn.setFont(font)
        self.accueilBtn.setStyleSheet(u"background-color:#1F232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accueilBtn.setIcon(icon1)
        self.accueilBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.accueilBtn)

        self.gestionBtn = QPushButton(self.frame_2)
        self.gestionBtn.setObjectName(u"gestionBtn")
        self.gestionBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gestionBtn.setIcon(icon2)
        self.gestionBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.gestionBtn)

        self.passageBtn = QPushButton(self.frame_2)
        self.passageBtn.setObjectName(u"passageBtn")
        self.passageBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.passageBtn.setIcon(icon3)
        self.passageBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.passageBtn)

        self.videoBtn = QPushButton(self.frame_2)
        self.videoBtn.setObjectName(u"videoBtn")
        self.videoBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.videoBtn.setIcon(icon4)
        self.videoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.videoBtn)

        self.chargerBdBtn = QPushButton(self.frame_2)
        self.chargerBdBtn.setObjectName(u"chargerBdBtn")
        self.chargerBdBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chargerBdBtn.setIcon(icon5)
        self.chargerBdBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.chargerBdBtn)
#####################################################################################################
####################################GIF##############################################################
#####################################################################################################
        self.labelGif = QLabel(self.frame_2)
        self.labelGif.setObjectName(u"labelGif")
        self.labelGif.setMaximumSize(QSize(40, 40))
        
        self.labelGif.setAlignment(QtCore.Qt.AlignCenter)
        
        self.verticalLayout_3.addWidget(self.labelGif)
        movie = QMovie('Pictures/loading2.gif')
        self.labelGif.setMovie(movie)
        movie.start() 
        self.labelGif.setVisible(False)  # Défaut : caché


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.parametreBtn = QPushButton(self.frame_3)
        self.parametreBtn.setObjectName(u"parametreBtn")
        self.parametreBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.parametreBtn.setIcon(icon6)
        self.parametreBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.parametreBtn)

        self.informationBtn = QPushButton(self.frame_3)
        self.informationBtn.setObjectName(u"informationBtn")
        self.informationBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.informationBtn.setIcon(icon7)
        self.informationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.informationBtn)

        self.aideBtn = QPushButton(self.frame_3)
        self.aideBtn.setObjectName(u"aideBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aideBtn.setIcon(icon8)
        self.aideBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aideBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon9)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setStyleSheet(u"")
        self.page_reglages = QWidget()
        self.page_reglages.setObjectName(u"page_reglages")
        self.label_2 = QLabel(self.page_reglages)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(82, 9, 40, 40))
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setPixmap(QPixmap(u":/icons/edit.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_11 = QFrame(self.page_reglages)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 150, 181, 241))
        self.frame_11.setMinimumSize(QSize(0, 150))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.currentMdp = QLineEdit(self.frame_11)
        self.currentMdp.setObjectName(u"currentMdp")
        self.currentMdp.setEnabled(True)
        self.currentMdp.setGeometry(QRect(30, 60, 131, 26))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currentMdp.sizePolicy().hasHeightForWidth())
        self.currentMdp.setSizePolicy(sizePolicy1)
        self.currentMdp.setEchoMode(QLineEdit.Password)
        self.currentMdp.setClearButtonEnabled(False)
        self.newMdp = QLineEdit(self.frame_11)
        self.newMdp.setObjectName(u"newMdp")
        self.newMdp.setGeometry(QRect(30, 110, 131, 26))
        self.newMdp.setEchoMode(QLineEdit.Password)
        self.editUserName = QLineEdit(self.frame_11)
        self.editUserName.setObjectName(u"editUserName")
        self.editUserName.setEnabled(True)
        self.editUserName.setGeometry(QRect(30, 10, 131, 26))
        sizePolicy1.setHeightForWidth(self.editUserName.sizePolicy().hasHeightForWidth())
        self.editUserName.setSizePolicy(sizePolicy1)
        self.editUserName.setAlignment(Qt.AlignCenter)
        self.confirmNewMdp = QLineEdit(self.frame_11)
        self.confirmNewMdp.setObjectName(u"confirmNewMdp")
        self.confirmNewMdp.setGeometry(QRect(30, 160, 131, 26))
        self.confirmNewMdp.setEchoMode(QLineEdit.Password)
        self.validerBtn = QPushButton(self.page_reglages)
        self.validerBtn.setObjectName(u"validerBtn")
        self.validerBtn.setGeometry(QRect(40, 360, 131, 31))
        self.validerBtn.setMaximumSize(QSize(16777215, 16777215))
        self.validerBtn.setStyleSheet(u"border-radius: 5px;\n"
"background: #00ff00;\n"
"color: white;")
        self.centerMenuPages.addWidget(self.page_reglages)
        self.page_information = QWidget()
        self.page_information.setObjectName(u"page_information")
        self.label_3 = QLabel(self.page_information)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 300, 136, 21))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.page_information)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 340, 131, 21))
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.page_information)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 380, 201, 21))
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.page_information)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(70, 400, 136, 21))
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.page_information)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 440, 171, 21))
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.page_information)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 480, 181, 21))
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.page_information)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(80, 500, 111, 21))
        self.label_20.setFont(font2)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.page_information)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 140, 136, 21))
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.centerMenuPages.addWidget(self.page_information)
        self.page_aide = QWidget()
        self.page_aide.setObjectName(u"page_aide")
        self.verticalLayout_9 = QVBoxLayout(self.page_aide)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_aide)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_aide)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setFont(font)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u":/images/logoB.png"))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon10)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon11)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon12)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimiseBtn = QPushButton(self.frame_7)
        self.minimiseBtn.setObjectName(u"minimiseBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimiseBtn.setIcon(icon13)
        self.minimiseBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.minimiseBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon14)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon15)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.mainBodyContent.setMinimumSize(QSize(608, 313))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_accueil = QWidget()
        self.page_accueil.setObjectName(u"page_accueil")
        self.verticalLayout_16 = QVBoxLayout(self.page_accueil)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_10 = QLabel(self.page_accueil)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)

        self.mainPages.addWidget(self.page_accueil)
        self.pagePassages = QWidget()
        self.pagePassages.setObjectName(u"pagePassages")
        self.photoArea = QWidget(self.pagePassages)
        self.photoArea.setObjectName(u"photoArea")
        self.photoArea.setGeometry(QRect(620, 120, 451, 341))
        self.photoArea.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.labelPhotoAfficher = QLabel(self.photoArea)
        self.labelPhotoAfficher.setObjectName(u"labelPhotoAfficher")
        self.labelPhotoAfficher.setGeometry(QRect(30, 30, 161, 161))
        self.labelPhotoAfficher.setStyleSheet(u"")
        self.lblNomAffiche = QLabel(self.photoArea)
        self.lblNomAffiche.setObjectName(u"lblNomAffiche")
        self.lblNomAffiche.setGeometry(QRect(230, 70, 31, 31))
        self.lblNomAffiche.setFont(font1)
        self.lblNomAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblPrenomAffiche = QLabel(self.photoArea)
        self.lblPrenomAffiche.setObjectName(u"lblPrenomAffiche")
        self.lblPrenomAffiche.setGeometry(QRect(230, 120, 51, 31))
        self.lblPrenomAffiche.setFont(font1)
        self.lblPrenomAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblAdresseAffiche = QLabel(self.photoArea)
        self.lblAdresseAffiche.setObjectName(u"lblAdresseAffiche")
        self.lblAdresseAffiche.setGeometry(QRect(30, 210, 51, 31))
        self.lblAdresseAffiche.setFont(font1)
        self.lblAdresseAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblMailAffiche = QLabel(self.photoArea)
        self.lblMailAffiche.setObjectName(u"lblMailAffiche")
        self.lblMailAffiche.setGeometry(QRect(30, 240, 31, 31))
        self.lblMailAffiche.setFont(font1)
        self.lblMailAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblIdAffiche = QLabel(self.photoArea)
        self.lblIdAffiche.setObjectName(u"lblIdAffiche")
        self.lblIdAffiche.setGeometry(QRect(230, 30, 61, 31))
        self.lblIdAffiche.setFont(font1)
        self.lblIdAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblTelephoneAffiche = QLabel(self.photoArea)
        self.lblTelephoneAffiche.setObjectName(u"lblTelephoneAffiche")
        self.lblTelephoneAffiche.setGeometry(QRect(30, 270, 71, 31))
        self.lblTelephoneAffiche.setFont(font1)
        self.lblTelephoneAffiche.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblIdAffiche_2 = QLabel(self.photoArea)
        self.lblIdAffiche_2.setObjectName(u"lblIdAffiche_2")
        self.lblIdAffiche_2.setGeometry(QRect(300, 30, 141, 31))
        self.lblIdAffiche_2.setFont(font1)
        self.lblIdAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblNomAffiche_2 = QLabel(self.photoArea)
        self.lblNomAffiche_2.setObjectName(u"lblNomAffiche_2")
        self.lblNomAffiche_2.setGeometry(QRect(270, 70, 171, 31))
        self.lblNomAffiche_2.setFont(font1)
        self.lblNomAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblPrenomAffiche_2 = QLabel(self.photoArea)
        self.lblPrenomAffiche_2.setObjectName(u"lblPrenomAffiche_2")
        self.lblPrenomAffiche_2.setGeometry(QRect(290, 120, 151, 31))
        self.lblPrenomAffiche_2.setFont(font1)
        self.lblPrenomAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblAdresseAffiche_2 = QLabel(self.photoArea)
        self.lblAdresseAffiche_2.setObjectName(u"lblAdresseAffiche_2")
        self.lblAdresseAffiche_2.setGeometry(QRect(90, 210, 351, 31))
        self.lblAdresseAffiche_2.setFont(font1)
        self.lblAdresseAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblMailAffiche_2 = QLabel(self.photoArea)
        self.lblMailAffiche_2.setObjectName(u"lblMailAffiche_2")
        self.lblMailAffiche_2.setGeometry(QRect(70, 240, 371, 31))
        self.lblMailAffiche_2.setFont(font1)
        self.lblMailAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTelephoneAffiche_2 = QLabel(self.photoArea)
        self.lblTelephoneAffiche_2.setObjectName(u"lblTelephoneAffiche_2")
        self.lblTelephoneAffiche_2.setGeometry(QRect(110, 270, 331, 31))
        self.lblTelephoneAffiche_2.setFont(font1)
        self.lblTelephoneAffiche_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.table2 = QTableWidget(self.pagePassages)
        if (self.table2.columnCount() < 3):
            self.table2.setColumnCount(3)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setForeground(brush);
        self.table2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setForeground(brush);
        self.table2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setForeground(brush);
        self.table2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table2.setObjectName(u"table2")
        self.table2.setGeometry(QRect(300, 120, 301, 341))
        self.table2.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.barRecherche2 = QWidget(self.pagePassages)
        self.barRecherche2.setObjectName(u"barRecherche2")
        self.barRecherche2.setGeometry(QRect(300, 50, 771, 61))
        self.barRecherche2.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.input_Recherche2 = QLineEdit(self.barRecherche2)
        self.input_Recherche2.setObjectName(u"input_Recherche2")
        self.input_Recherche2.setGeometry(QRect(180, 10, 581, 41))
        self.input_Recherche2.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.BtnRecherche2 = QPushButton(self.barRecherche2)
        self.BtnRecherche2.setObjectName(u"BtnRecherche2")
        self.BtnRecherche2.setGeometry(QRect(10, 10, 151, 41))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.BtnRecherche2.sizePolicy().hasHeightForWidth())
        self.BtnRecherche2.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setPointSize(16)
        self.BtnRecherche2.setFont(font4)
        self.BtnRecherche2.setStyleSheet(u"border-radius: 5px;\n"
"background: green;\n"
"color: white;")
        icon16 = QIcon()
        icon16.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnRecherche2.setIcon(icon16)
        self.BtnRecherche2.setIconSize(QSize(24, 24))
        self.label_22 = QLabel(self.pagePassages)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 10, 172, 21))
        self.label_22.setFont(font2)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.pagePassages)
        self.page_gestion = QWidget()
        self.page_gestion.setObjectName(u"page_gestion")
        self.label_11 = QLabel(self.page_gestion)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 10, 172, 21))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.page_gestion)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(331, 451, 701, 80))
        self.widget.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.BtnSupp = QPushButton(self.widget)
        self.BtnSupp.setObjectName(u"BtnSupp")
        self.BtnSupp.setGeometry(QRect(250, 20, 201, 41))
        self.BtnSupp.setFont(font4)
        self.BtnSupp.setStyleSheet(u"border-radius: 5px;\n"
"background: #FF0000;\n"
"color: white;")
        icon17 = QIcon()
        icon17.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnSupp.setIcon(icon17)
        self.BtnSupp.setIconSize(QSize(24, 24))
        self.BtnModif = QPushButton(self.widget)
        self.BtnModif.setObjectName(u"BtnModif")
        self.BtnModif.setGeometry(QRect(480, 20, 201, 41))
        self.BtnModif.setFont(font4)
        self.BtnModif.setStyleSheet(u"border-radius: 5px;\n"
"background: #0080ff;\n"
"color: white;")
        icon18 = QIcon()
        icon18.addFile(u":/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnModif.setIcon(icon18)
        self.BtnModif.setIconSize(QSize(24, 24))
        self.BtnActualiser = QPushButton(self.widget)
        self.BtnActualiser.setObjectName(u"BtnActualiser")
        self.BtnActualiser.setGeometry(QRect(20, 20, 201, 41))
        self.BtnActualiser.setFont(font4)
        self.BtnActualiser.setStyleSheet(u"border-radius: 5px;\n"
"background: gray;\n"
"color: white;")
        self.BtnActualiser.setIcon(icon5)
        self.BtnActualiser.setIconSize(QSize(24, 24))
        self.barRecherche = QWidget(self.page_gestion)
        self.barRecherche.setObjectName(u"barRecherche")
        self.barRecherche.setGeometry(QRect(331, 61, 701, 61))
        self.barRecherche.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.input_Recherche = QLineEdit(self.barRecherche)
        self.input_Recherche.setObjectName(u"input_Recherche")
        self.input_Recherche.setGeometry(QRect(240, 10, 441, 41))
        self.input_Recherche.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.BtnRecherche = QPushButton(self.barRecherche)
        self.BtnRecherche.setObjectName(u"BtnRecherche")
        self.BtnRecherche.setGeometry(QRect(20, 10, 201, 41))
        sizePolicy4.setHeightForWidth(self.BtnRecherche.sizePolicy().hasHeightForWidth())
        self.BtnRecherche.setSizePolicy(sizePolicy4)
        self.BtnRecherche.setFont(font4)
        self.BtnRecherche.setStyleSheet(u"border-radius: 5px;\n"
"background: green;\n"
"color: white;")
        self.BtnRecherche.setIcon(icon16)
        self.BtnRecherche.setIconSize(QSize(24, 24))
        self.table = QTableWidget(self.page_gestion)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setForeground(brush);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setForeground(brush);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setForeground(brush);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        __qtablewidgetitem6.setForeground(brush);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        __qtablewidgetitem7.setForeground(brush);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        __qtablewidgetitem8.setForeground(brush);
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        __qtablewidgetitem9.setForeground(brush);
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(331, 131, 701, 301))
        self.table.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.panel_Rec = QWidget(self.page_gestion)
        self.panel_Rec.setObjectName(u"panel_Rec")
        self.panel_Rec.setGeometry(QRect(21, 61, 301, 471))
        self.panel_Rec.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.input_id_pers = QLineEdit(self.panel_Rec)
        self.input_id_pers.setObjectName(u"input_id_pers")
        self.input_id_pers.setGeometry(QRect(30, 20, 241, 31))
        self.input_id_pers.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_nom = QLineEdit(self.panel_Rec)
        self.input_nom.setObjectName(u"input_nom")
        self.input_nom.setGeometry(QRect(30, 70, 241, 31))
        self.input_nom.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_prenom = QLineEdit(self.panel_Rec)
        self.input_prenom.setObjectName(u"input_prenom")
        self.input_prenom.setGeometry(QRect(30, 120, 241, 31))
        self.input_prenom.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_photo = QLineEdit(self.panel_Rec)
        self.input_photo.setObjectName(u"input_photo")
        self.input_photo.setGeometry(QRect(30, 170, 131, 31))
        self.input_photo.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_telephone = QLineEdit(self.panel_Rec)
        self.input_telephone.setObjectName(u"input_telephone")
        self.input_telephone.setGeometry(QRect(30, 220, 241, 31))
        self.input_telephone.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_mail = QLineEdit(self.panel_Rec)
        self.input_mail.setObjectName(u"input_mail")
        self.input_mail.setGeometry(QRect(30, 270, 241, 31))
        self.input_mail.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_adresse = QLineEdit(self.panel_Rec)
        self.input_adresse.setObjectName(u"input_adresse")
        self.input_adresse.setGeometry(QRect(30, 320, 241, 31))
        self.input_adresse.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.BtnAjouter = QPushButton(self.panel_Rec)
        self.BtnAjouter.setObjectName(u"BtnAjouter")
        self.BtnAjouter.setGeometry(QRect(40, 390, 201, 41))
        self.BtnAjouter.setFont(font4)
        self.BtnAjouter.setStyleSheet(u"border-radius: 5px;\n"
"background: #00ff00;\n"
"color: white;")
        icon19 = QIcon()
        icon19.addFile(u":/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnAjouter.setIcon(icon19)
        self.BtnAjouter.setIconSize(QSize(24, 24))
        self.BtnCharger = QPushButton(self.panel_Rec)
        self.BtnCharger.setObjectName(u"BtnCharger")
        self.BtnCharger.setGeometry(QRect(170, 170, 101, 31))
        self.BtnCharger.setStyleSheet(u"background: gray;\n"
"color: white;\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/icons/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnCharger.setIcon(icon20)
        self.BtnCharger.setIconSize(QSize(16, 16))
        self.mainPages.addWidget(self.page_gestion)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 295))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon9)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_18 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.popupNotificationSubContainer)
        self.label_13.setObjectName(u"label_13")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_13.setFont(font5)

        self.verticalLayout_19.addWidget(self.label_13)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setPointSize(8)
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon21)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_9)


        self.verticalLayout_18.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)
        
        
        
        
############################################### BTN CLICKED ###################################################
###############################################################################################################
###############################################################################################################

        self.BtnCharger.clicked.connect(self.loadImage)
        self.BtnAjouter.clicked.connect(self.insert)
        self.BtnModif.clicked.connect(self.edit)
        self.validerBtn.clicked.connect(self.editAccount)
        self.BtnSupp.clicked.connect(self.delete)
        self.table.cellClicked.connect(self.handle_cell_clicked)
        self.table2.cellClicked.connect(self.handle_cell_clicked2)
        self.BtnRecherche.clicked.connect(self.search)
        self.BtnRecherche2.clicked.connect(self.search2)
        self.chargerBdBtn.clicked.connect(self.chargerBd)
        self.ligne = self.table.cellClicked.connect(self.on_cell_clicked)
        self.BtnActualiser.clicked.connect(self.reflesh)
        self.videoBtn.clicked.connect(self.getFace)
        
        self.showTableData()
        self.showTableData2()
     
        
        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    
    
    def chargerBd(self):
        # Afficher le GIF
        self.labelGif.setVisible(True)
        
        self.worker = Worker()
        self.worker.finished.connect(self.onFinished)
        self.worker.start()

    def onFinished(self):
        self.labelGif.setVisible(False)
    
    ###################################################################################################################
    ############################################### FACE RECOGNITION ########################################################
    
    def record(self,identity,D_H):
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        identity = str(identity)
        cur.execute("select id_Pers from Personnes where prenom = (?)", (identity,))
        con.commit()
        RqtResult = cur.fetchall()
        cur.execute("insert into Passages (dateHeure,ID_Pers)values (?,?)", (D_H, RqtResult[0][0]),)
        con.commit()   
        #RqtResult = cur.fetchall()
        con.close()
                
    def getFace(self):
        # HaarCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        HaarCascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'))
        #MyFaceNet = load_model("facenet_keras.h5")


        myfile = open("data.pkl", "rb")
        database = pickle.load(myfile)
        myfile.close()

        cap = cv2.VideoCapture(0)

        detected_identities = []
        # À l'extérieur de la boucle principale, initialisez un compteur pour créer des noms de fichiers uniques
        unknown_counter = 1

    
        while True:
            _, gbr1 = cap.read()

            wajah = HaarCascade.detectMultiScale(gbr1, 1.1, 4)

            if len(wajah) > 0:
                x1, y1, width, height = wajah[0]
            else:
                continue

            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height

            gbr = cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB)
            gbr = Image.fromarray(gbr)
            gbr_array = asarray(gbr)

            face = gbr_array[y1:y2, x1:x2]

            face = Image.fromarray(face)
            face = face.resize((160, 160))
            face = asarray(face)

            face = face.astype('float32')
            mean, std = face.mean(), face.std()
            face = (face - mean) / std

            signature = face_detector.face_detector(face)

            min_dist = 100
            identity = ' '
            date_heure = datetime.datetime.now()
            date_heure_texte = date_heure.strftime("%Y-%m-%d %H:%M:%S")

            for key, value in database.items():
                dist = np.linalg.norm(value - signature)
                if dist < min_dist:
                    min_dist = dist
                    color = (0, 255, 0)
                    identity = f"{key}"
                    

                    if identity not in detected_identities:
                        detected_identities.append(identity)

                    if identity != "non_reconnu":
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)

            cv2.putText(gbr1, identity, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (color), 2, cv2.LINE_AA)
            cv2.rectangle(gbr1, (x1, y1), (x2, y2), (color), 2)

            cv2.imshow('res', gbr1)

            # Vérifier si la liste detected_identities contient uniquement l'identité "non_reconnu" et prendre une photo
            if len(detected_identities) == 1 and detected_identities[0] == "non_reconnu":
                shoot_face_unknown = gbr1[y1:y2, x1:x2]
                chemin_dossier = "Photo/"
                img_item = f"{chemin_dossier}unknown_unknown_{time.time()}_face_{unknown_counter}.png"
                # img_item = "sary_test.png"
                cv2.imwrite(img_item, shoot_face_unknown)

                # Incrémenter le compteur pour le prochain fichier
                unknown_counter += 1
                
                self.record(identity,date_heure_texte)
                # Pour activer le bouton
                self.label_12.setText("Une personne vient de passer")
                self.notificationBtn.setEnabled(True)
                
            else:
                    
                self.record(identity,date_heure_texte)
                self.label_12.setText("Une personne vient de passer")
                self.notificationBtn.setEnabled(True)
            
            detected_identities = []

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()
    
    ###################################################################################################################
    ############################################### SHOW TABLE ########################################################    
    
    def showTableData2(self):
         # Connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Passages")
        con.commit()
        RqtResult = cur.fetchall()
        
        self.table2.clearContents()
        self.table2.setRowCount(0)
        
        for row_number, row_data in enumerate(RqtResult):
            self.table2.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                self.table2.setItem(row_number, column_number, QTableWidgetItem(item))
                
        con.close()
    
    
    def showTableData(self):
        # Connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Personnes where id_Pers != 0")
        con.commit()
        RqtResult = cur.fetchall()
        
        self.table.clearContents()
        self.table.setRowCount(0)
        
        # Définissez la hauteur de ligne fixe (par exemple, 100 pixels)
        row_height = 100
        
        for row_number, row_data in enumerate(RqtResult):
            
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 1:  # Colonne contenant les données binaires de l'image
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(column_data)
                    label = QtWidgets.QLabel()
                    label.setPixmap(pixmap)
                    # Redimensionnez l'image pour qu'elle s'affiche à sa taille normale
                    label.setScaledContents(True)
                    # Encapsulez le QLabel dans un QWidget
                    widget = QtWidgets.QWidget()
                    layout = QtWidgets.QHBoxLayout()
                    layout.addWidget(label)
                    widget.setLayout(layout)
                    self.table.setCellWidget(row_number, column_number, widget)
                else:
                    self.table.setItem(row_number, column_number, QTableWidgetItem(item))
                    # Définissez la hauteur de la ligne
                    self.table.setRowHeight(row_number, row_height)
        con.close()

        # Ajustez automatiquement la hauteur des lignes pour afficher les images en entier
        # for row_number in range(self.table.rowCount()):
        #     self.table.resizeRowToContents(row_number)
    
    #######################################################################################################
    ############################################### SEARCH ################################################
    def search(self):
        search_term = self.input_Recherche.text()
        found_rows = []
        try:
            search_value = int(search_term)
            for row_number in range(self.table.rowCount()):
                for column_number in range(self.table.columnCount()):
                    item = self.table.item(row_number, column_number)
                    if item and item.text().isdigit() and search_value == int(item.text()):
                        found_rows.append(row_number)
                        break
        except ValueError:
            for row_number in range(self.table.rowCount()):
                found = False
                for column_number in range(self.table.columnCount()):
                    item = self.table.item(row_number, column_number)
                    if item and search_term in item.text():
                        found = True
                        break
                if found:
                    found_rows.append(row_number)
        
        for row_number in range(self.table.rowCount()):
            if row_number in found_rows:
                self.table.showRow(row_number)
            else:
                self.table.hideRow(row_number)
        
        if not found_rows:
            QMessageBox.information(self, "Information", "Aucune ligne trouvée avec la recherche : {}".format(search_term))
            
            
    def search2(self):
        search_term = self.input_Recherche2.text()
        found_rows = []
        try:
            search_value = int(search_term)
            for row_number in range(self.table2.rowCount()):
                for column_number in range(self.table2.columnCount()):
                    item = self.table2.item(row_number, column_number)
                    if item and item.text().isdigit() and search_value == int(item.text()):
                        found_rows.append(row_number)
                        break
        except ValueError:
            for row_number in range(self.table2.rowCount()):
                found = False
                for column_number in range(self.table2.columnCount()):
                    item = self.table2.item(row_number, column_number)
                    if item and search_term in item.text():
                        found = True
                        break
                if found:
                    found_rows.append(row_number)
        
        for row_number in range(self.table2.rowCount()):
            if row_number in found_rows:
                self.table2.showRow(row_number)
            else:
                self.table2.hideRow(row_number)
        
        if not found_rows:
            QMessageBox.information(self, "Information", "Aucune ligne trouvée avec la recherche : {}".format(search_term))
    ###################################################################################################################
    ############################################### handle_cell_clicked ########################################################
    
    def  handle_cell_clicked(self,row, column):
        identifiant = self.table.item(row,0).text()
        # photo = self.table.item(row,1).text()
        nom = self.table.item(row,2).text()
        prenom = self.table.item(row,3).text()
        mail = self.table.item(row,4).text()
        telephone = self.table.item(row,5).text()
        adresse =self.table.item(row,6).text()
        ohatra = self.table.item(row,6).text()
        
        #desplacement données
        self.input_id_pers.setText(identifiant)
        self.input_nom.setText(nom)
        self.input_prenom.setText(prenom)
        # self.input_photo.setText(photo)
        self.input_mail.setText(mail)
        self.input_telephone.setText(telephone)
        self.input_adresse.setText(adresse)
        self.input_adresse.setText(ohatra)
        
        
    def  handle_cell_clicked2(self,row, column):
        identifiant = self.table2.item(row,2).text()
        
        
        # Connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Personnes where id_Pers =?",(identifiant,))
        con.commit()
        RqtResult = cur.fetchall()
        
        # photo = RqtResult[0][1]
        photo_blob = RqtResult[0][1]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo_blob)
        self.labelPhotoAfficher.setScaledContents(True)
        
        nom = RqtResult[0][2]
        prenom = RqtResult[0][3]
        mail = RqtResult[0][4]
        telephone = RqtResult[0][5]
        adresse = RqtResult[0][6]
        
        #desplacement données
        self.lblIdAffiche_2.setText(identifiant)
        self.lblNomAffiche_2.setText(nom)
        self.lblPrenomAffiche_2.setText(prenom)
        self.lblAdresseAffiche_2.setText(adresse)
        self.lblMailAffiche_2.setText(mail)
        self.lblTelephoneAffiche_2.setText(telephone)
        self.labelPhotoAfficher.setPixmap(pixmap)
        
    
    #fonction recuperant ligne table    
    def on_cell_clicked(self, row):
        return row
    #fonction actualisant la table    
    def reflesh(self):
        self.showTableData()
########################################################### INSERT #########################################################
############################################################################################################################
############################################################################################################################
    def insert(self):
        identifiant = self.input_id_pers.text()
        nom = self.input_nom.text()
        prenom = self.input_prenom.text()
        # photo = self.input_photo.text()
        telephone = self.input_telephone.text()
        mail = self.input_mail.text()
        adresse = self.input_adresse.text()
        
        # Ouverture du fichier image et conversion en données binaires
        with open(self.input_photo.text(), 'rb') as image_file:
                image_binary = image_file.read()
        

        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("insert into Personnes (id_Pers,photo,nom,prenom,mail,telephone,adresse)values (?,?,?,?,?,?,?)", (identifiant, image_binary, nom, prenom, mail, telephone, adresse))
        con.commit()   
        #RqtResult = cur.fetchall()
        con.close()
        self.label_12.setText("Ajout d'une personne")
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
        
    ############################################################ EDIT ##########################################################
    ############################################################################################################################
    ############################################################################################################################
    def editAccount(self):
        userName = self.editUserName.text()
        password = self.currentMdp.text()
        newPassword = self.newMdp.text()
        confirmNewPassword = self.confirmNewMdp.text()
        
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Login")
        
        RqtResult = cur.fetchall()
        
        oldPassword = RqtResult[0][2]
        
        print(f" current:{password}, oldpass: {oldPassword}, newpass: {newPassword}, confirmpass: {confirmNewPassword}")
        # print(RqtResult[0][2])
        # print(newPassword)
        
        if userName == "":
            userName = "Admin"
        
        if ((str(password) == str(oldPassword)) and (str(newPassword) == str(confirmNewPassword))):
        
            cur.execute("update Login set userName=?,password=?where Identifiant=?",
            (userName, newPassword, 1))
            self.label_12.setText("Compte mise à jours")
            self.editUserName.setText("")
            self.currentMdp.setText("")
            self.newMdp.setText("")
            self.confirmNewMdp.setText("")
            
        con.commit()
        con.close()
        
        self.showTableData()
        
        
    def edit(self):
        identifiant = self.input_id_pers.text()
        # photo = self.input_photo.text()
        nom = self.input_nom.text()
        prenom = self.input_prenom.text()
        telephone = self.input_telephone.text()
        mail = self.input_mail.text()
        adresse = self.input_adresse.text()
        
        # Ouverture du fichier image et conversion en données binaires
        with open(self.input_photo.text(), 'rb') as image_file:
                image_binary = image_file.read()
        
        print(identifiant)
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("update Personnes set id_Pers=?,photo=?,nom=?,prenom=?,mail=?,telephone=?,adresse=? where id_Pers=?",
            (identifiant, image_binary, nom, prenom, mail, telephone, adresse,identifiant))
        con.commit()
        con.close()
        
        self.label_12.setText("Modification d'une personne")
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
    def delete(self):
        
        identifiant = self.input_id_pers.text()
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("delete from Personnes where id_Pers = ?",(identifiant,))
        con.commit()   
        con.close()
        
        self.label_12.setText("Suppression d'une personne")    
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
    
####################################################################################################################

################################################LOAD IMAGE##########################################################
    def loadImage(self):   
        FileName = QFileDialog.getOpenFileName(None, 'open file','E:\Photo_nathan\Albert.jpg')
        self.input_photo.setText(FileName[0])
    
    
    
    
    
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.accueilBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Accueil", None))
#endif // QT_CONFIG(tooltip)
        self.accueilBtn.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
#if QT_CONFIG(tooltip)
        self.gestionBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Gestion des personnels", None))
#endif // QT_CONFIG(tooltip)
        self.gestionBtn.setText(QCoreApplication.translate("MainWindow", u"Gestion des personnels ", None))
        self.passageBtn.setText(QCoreApplication.translate("MainWindow", u"Gestion des passages", None))
#if QT_CONFIG(tooltip)
        self.videoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Camera", None))
#endif // QT_CONFIG(tooltip)
        self.videoBtn.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.chargerBdBtn.setText(QCoreApplication.translate("MainWindow", u"Charger BD", None))
        self.labelGif.setText("")
#if QT_CONFIG(tooltip)
        self.parametreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Param\u00e8tre", None))
#endif // QT_CONFIG(tooltip)
        self.parametreBtn.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tre", None))
#if QT_CONFIG(tooltip)
        self.informationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.informationBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.aideBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Aide", None))
#endif // QT_CONFIG(tooltip)
        self.aideBtn.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plus de menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText("")
        self.currentMdp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe courant", None))
        self.newMdp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nouveau mot de passe", None))
        self.editUserName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.confirmNewMdp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmer Nouveau mot de passe", None))
        self.validerBtn.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nom: RANJALAHY", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Prenom: T.herizo", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Adresse: PRES VS 52 HDQ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Avaratr'ankatso", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"M\u00e9tier: D\u00e9veloppeur", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact: 261329045525", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"261346257586", None))
        self.label_21.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CamShoot", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimiseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimiseBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bienvenu \U0001F31D", None))
        self.labelPhotoAfficher.setText("")
        self.lblNomAffiche.setText(QCoreApplication.translate("MainWindow", u"Nom:", None))
        self.lblPrenomAffiche.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom:", None))
        self.lblAdresseAffiche.setText(QCoreApplication.translate("MainWindow", u"Adresse:", None))
        self.lblMailAffiche.setText(QCoreApplication.translate("MainWindow", u"Mail:", None))
        self.lblIdAffiche.setText(QCoreApplication.translate("MainWindow", u"Identifiant:", None))
        self.lblTelephoneAffiche.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone:", None))
        self.lblIdAffiche_2.setText("")
        self.lblNomAffiche_2.setText("")
        self.lblPrenomAffiche_2.setText("")
        self.lblAdresseAffiche_2.setText("")
        self.lblMailAffiche_2.setText("")
        self.lblTelephoneAffiche_2.setText("")
        ___qtablewidgetitem = self.table2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identifiant", None));
        ___qtablewidgetitem1 = self.table2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date et Heure", None));
        ___qtablewidgetitem2 = self.table2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Id du passant", None));
        self.input_Recherche2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"recherchez ici", None))
        self.BtnRecherche2.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Gestion des passages", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gestion des personnels", None))
        self.BtnSupp.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.BtnModif.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.BtnActualiser.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.input_Recherche.setPlaceholderText(QCoreApplication.translate("MainWindow", u"recherchez ici", None))
        self.BtnRecherche.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Identifiant", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Photo", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Mail", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        self.input_id_pers.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identifiant", None))
        self.input_nom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.input_prenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.input_photo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.input_telephone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None))
        self.input_mail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.input_adresse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.BtnAjouter.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.BtnCharger.setText(QCoreApplication.translate("MainWindow", u"Charger image", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Menu droit", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Plus...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"notification", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CopyRight 2022", None))
    # retranslateUi

