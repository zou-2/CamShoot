# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrincipaljMhEPv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
import sqlite3
from PyQt5.QtWidgets import QFileDialog
#from PyQt5 import QtWidgets

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 494)
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

        self.imprimerBtn = QPushButton(self.frame_2)
        self.imprimerBtn.setObjectName(u"imprimerBtn")
        self.imprimerBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imprimerBtn.setIcon(icon3)
        self.imprimerBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.imprimerBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        icon4 = QIcon()
        icon4.addFile(u":/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.parametreBtn.setIcon(icon4)
        self.parametreBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.parametreBtn)

        self.informationBtn = QPushButton(self.frame_3)
        self.informationBtn.setObjectName(u"informationBtn")
        self.informationBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.informationBtn.setIcon(icon5)
        self.informationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.informationBtn)

        self.aideBtn = QPushButton(self.frame_3)
        self.aideBtn.setObjectName(u"aideBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aideBtn.setIcon(icon6)
        self.aideBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aideBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

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
        icon7 = QIcon()
        icon7.addFile(u":/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setPixmap(QPixmap(u":/icons/edit.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 150))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lineEdit = QLineEdit(self.frame_11)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_17.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_17.addWidget(self.lineEdit_2)


        self.verticalLayout_7.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)

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
        icon8 = QIcon()
        icon8.addFile(u":/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon10)
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
        icon11 = QIcon()
        icon11.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimiseBtn.setIcon(icon11)
        self.minimiseBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.minimiseBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)
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
        self.page_gestion = QWidget()
        self.page_gestion.setObjectName(u"page_gestion")
        self.label_11 = QLabel(self.page_gestion)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(9, 9, 172, 21))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.page_gestion)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(450, 470, 701, 80))
        self.widget.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.BtnSupp = QPushButton(self.widget)
        self.BtnSupp.setObjectName(u"BtnSupp")
        self.BtnSupp.setGeometry(QRect(140, 20, 201, 41))
        font4 = QFont()
        font4.setPointSize(16)
        self.BtnSupp.setFont(font4)
        self.BtnSupp.setStyleSheet(u"border-radius: 5px;\n"
"background: #FF0000;\n"
"color: white;")
        self.BtnModif = QPushButton(self.widget)
        self.BtnModif.setObjectName(u"BtnModif")
        self.BtnModif.setGeometry(QRect(360, 20, 201, 41))
        self.BtnModif.setFont(font4)
        self.BtnModif.setStyleSheet(u"border-radius: 5px;\n"
"background: #0080ff;\n"
"color: white;")
        self.barRecherche = QWidget(self.page_gestion)
        self.barRecherche.setObjectName(u"barRecherche")
        self.barRecherche.setGeometry(QRect(450, 80, 701, 61))
        self.barRecherche.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.input_Recherche = QLineEdit(self.barRecherche)
        self.input_Recherche.setObjectName(u"input_Recherche")
        self.input_Recherche.setGeometry(QRect(240, 10, 431, 41))
        self.input_Recherche.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.BtnRecherche = QPushButton(self.barRecherche)
        self.BtnRecherche.setObjectName(u"BtnRecherche")
        self.BtnRecherche.setGeometry(QRect(20, 10, 201, 41))
        self.BtnRecherche.setFont(font4)
        self.BtnRecherche.setStyleSheet(u"border-radius: 5px;\n"
"background: green;\n"
"color: white;")
        self.table = QTableWidget(self.page_gestion)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setForeground(brush);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setForeground(brush);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setForeground(brush);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setForeground(brush);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setForeground(brush);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setForeground(brush);
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        __qtablewidgetitem6.setForeground(brush);
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(450, 150, 701, 301))
        self.table.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.panel_Rec = QWidget(self.page_gestion)
        self.panel_Rec.setObjectName(u"panel_Rec")
        self.panel_Rec.setGeometry(QRect(70, 80, 351, 471))
        self.panel_Rec.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.input_id_pers = QLineEdit(self.panel_Rec)
        self.input_id_pers.setObjectName(u"input_id_pers")
        self.input_id_pers.setGeometry(QRect(70, 20, 201, 31))
        self.input_id_pers.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_nom = QLineEdit(self.panel_Rec)
        self.input_nom.setObjectName(u"input_nom")
        self.input_nom.setGeometry(QRect(70, 70, 201, 31))
        self.input_nom.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_prenom = QLineEdit(self.panel_Rec)
        self.input_prenom.setObjectName(u"input_prenom")
        self.input_prenom.setGeometry(QRect(70, 120, 201, 31))
        self.input_prenom.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_photo = QLineEdit(self.panel_Rec)
        self.input_photo.setObjectName(u"input_photo")
        self.input_photo.setGeometry(QRect(70, 170, 111, 31))
        self.input_photo.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_telephone = QLineEdit(self.panel_Rec)
        self.input_telephone.setObjectName(u"input_telephone")
        self.input_telephone.setGeometry(QRect(70, 220, 201, 31))
        self.input_telephone.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_mail = QLineEdit(self.panel_Rec)
        self.input_mail.setObjectName(u"input_mail")
        self.input_mail.setGeometry(QRect(70, 270, 201, 31))
        self.input_mail.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.input_adresse = QLineEdit(self.panel_Rec)
        self.input_adresse.setObjectName(u"input_adresse")
        self.input_adresse.setGeometry(QRect(70, 320, 201, 31))
        self.input_adresse.setStyleSheet(u"background:#1b1b27;\n"
" padding: 5px 10px;\n"
" border-radius: 5px;")
        self.BtnAjouter = QPushButton(self.panel_Rec)
        self.BtnAjouter.setObjectName(u"BtnAjouter")
        self.BtnAjouter.setGeometry(QRect(70, 390, 201, 41))
        self.BtnAjouter.setFont(font4)
        self.BtnAjouter.setStyleSheet(u"border-radius: 5px;\n"
"background: #00ff00;\n"
"color: white;")
        self.BtnCharger = QPushButton(self.panel_Rec)
        self.BtnCharger.setObjectName(u"BtnCharger")
        self.BtnCharger.setGeometry(QRect(190, 170, 81, 31))
        self.BtnCharger.setStyleSheet(u"background: gray;\n"
"color: white;\n"
"")
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
        self.closeRightMenuBtn.setIcon(icon7)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setPointSize(8)
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon14)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
############################################### BTN CLICKED ###################################################
###############################################################################################################
###############################################################################################################

        self.BtnCharger.clicked.connect(self.Insert)
        self.BtnAjouter.clicked.connect(self.loadImage)
        #self.BtnCharger.clicked.connect(self.showTableData)
        self.showTableData()
    # setupUi

    ###################################################################################################################
################################################SHOW TABLE#########################################################    
    def showTableData(self):
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute(" select * from Personnes ")
        con.commit()
        RqtResult = cur.fetchall()
        for row_number, row_data in enumerate(RqtResult):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if(column_number != 0):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(item))
        con.close()
    
############################################################INSERT##########################################################
############################################################################################################################
############################################################################################################################
    def Insert(self):
        identifiant = self.input_id_pers.text()
        nom = self.input_nom.text()
        prenom = self.input_prenom.text()
        photo = self.input_photo.text()
        telephone = self.input_telephone.text()
        mail = self.input_mail.text()
        adresse = self.input_adresse.text()
        

        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("insert into Personnes (id_Pers,photo,nom,prenom,mail,telephone,adresse)values (?,?,?,?,?,?,?)", (identifiant, photo, nom, prenom, mail, telephone, adresse))
        con.commit()
        RqtResult = cur.fetchall()
        con.close()
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
       
        
    
####################################################################################################################

################################################LOAD IMAGE##########################################################
    def loadImage(self):   
        FileName = QFileDialog.getOpenFileName(self.parent, 'open file','E:\Photo_nathan\Albert.jpg')
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
        self.gestionBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Gestion des pesonnels", None))
#endif // QT_CONFIG(tooltip)
        self.gestionBtn.setText(QCoreApplication.translate("MainWindow", u"Gestion des personnels ", None))
#if QT_CONFIG(tooltip)
        self.imprimerBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Imprimer", None))
#endif // QT_CONFIG(tooltip)
        self.imprimerBtn.setText(QCoreApplication.translate("MainWindow", u"Imprimer", None))
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
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe courant", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nouveau mot de passe", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
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
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gestion des personnels", None))
        self.BtnSupp.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.BtnModif.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.input_Recherche.setPlaceholderText(QCoreApplication.translate("MainWindow", u"entrer Id", None))
        self.BtnRecherche.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identifiant", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Photo", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mail", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
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

