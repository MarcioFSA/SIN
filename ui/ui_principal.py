# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import Outros_rc
import Imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 700)
        MainWindow.setMinimumSize(QSize(1024, 700))
        MainWindow.setMaximumSize(QSize(1024, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1024, 700))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(5, 9, 1020, 700))
        self.stackedWidget.setMinimumSize(QSize(1020, 700))
        self.stackedWidget.setMaximumSize(QSize(1020, 700))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(210, 80))
        self.label_4.setStyleSheet(u"image: url(:/Imagem/Logo SIN.png);")

        self.verticalLayout_13.addWidget(self.label_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)


        self.gridLayout_6.addLayout(self.verticalLayout_13, 0, 0, 1, 3)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(290, 440))
        font1 = QFont()
        font1.setFamilies([u"Reem Kufi"])
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 110, 251, 80))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.btn_fnea = QPushButton(self.groupBox_2)
        self.btn_fnea.setObjectName(u"btn_fnea")
        self.btn_fnea.setGeometry(QRect(70, 30, 100, 40))
        self.btn_fnea.setMinimumSize(QSize(100, 40))
        self.btn_fnea.setMaximumSize(QSize(80, 30))
        font2 = QFont()
        font2.setFamilies([u"Reem Kufi"])
        font2.setBold(False)
        self.btn_fnea.setFont(font2)
        self.btn_fnea.setStyleSheet(u"QPushButton#btn_fnea{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_fnea:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_fnea:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Imagem/dashboard (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fnea.setIcon(icon)
        self.btn_fnea.setIconSize(QSize(24, 24))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 270, 251, 80))
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.btn_rnc = QPushButton(self.groupBox_3)
        self.btn_rnc.setObjectName(u"btn_rnc")
        self.btn_rnc.setGeometry(QRect(73, 26, 100, 40))
        self.btn_rnc.setMinimumSize(QSize(100, 40))
        self.btn_rnc.setMaximumSize(QSize(80, 30))
        font3 = QFont()
        font3.setFamilies([u"Reem Kufi"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.btn_rnc.setFont(font3)
        self.btn_rnc.setStyleSheet(u"QPushButton#btn_rnc{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_rnc:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_rnc:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Imagem/prancheta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rnc.setIcon(icon1)
        self.btn_rnc.setIconSize(QSize(24, 24))

        self.gridLayout_6.addWidget(self.groupBox, 1, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(324, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(324, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Reem Kufi"])
        font4.setPointSize(10)
        self.label_5.setFont(font4)

        self.gridLayout_6.addWidget(self.label_5, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.btn_voltar_rnc = QPushButton(self.page_2)
        self.btn_voltar_rnc.setObjectName(u"btn_voltar_rnc")
        self.btn_voltar_rnc.setMinimumSize(QSize(202, 40))
        self.btn_voltar_rnc.setMaximumSize(QSize(150, 40))
        font5 = QFont()
        font5.setFamilies([u"Reem Kufi"])
        font5.setBold(True)
        font5.setItalic(False)
        self.btn_voltar_rnc.setFont(font5)
        self.btn_voltar_rnc.setStyleSheet(u"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Imagens/vire-a-esquerda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voltar_rnc.setIcon(icon2)
        self.btn_voltar_rnc.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_voltar_rnc, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(272, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 4, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(771, 541))
        self.groupBox_4.setStyleSheet(u"border-top-left-radius:50px;")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setFamilies([u"Reem Kufi"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_7, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.groupBox_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(510, 410))
        self.widget_2.setMaximumSize(QSize(510, 410))
        self.widget_2.setStyleSheet(u"")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 201, 411))
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"border-top-left-radius:50px;")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 10, 221, 411))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(241, 200, 250, 30))
        self.lineEdit.setMinimumSize(QSize(250, 30))
        font7 = QFont()
        font7.setFamilies([u"Reem Kufi"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.lineEdit.setFont(font7)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(241, 240, 250, 30))
        self.lineEdit_2.setMinimumSize(QSize(250, 30))
        self.lineEdit_2.setFont(font7)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(282, 27, 151, 151))
        self.label_9.setMinimumSize(QSize(151, 151))
        self.label_9.setStyleSheet(u"image: url(:/Imagem/user.png);")
        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(239, 290, 251, 22))
        self.comboBox_2.setFont(font2)
        self.layoutWidget_5 = QWidget(self.widget_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(240, 320, 252, 88))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton(self.layoutWidget_5)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(250, 40))
        self.btn_login.setFont(font7)
        self.btn_login.setStyleSheet(u"QPushButton#btn_login{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Imagem/user (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon3)
        self.btn_login.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.btn_login)

        self.btn_notificaSlogin = QPushButton(self.layoutWidget_5)
        self.btn_notificaSlogin.setObjectName(u"btn_notificaSlogin")
        self.btn_notificaSlogin.setMinimumSize(QSize(250, 40))
        self.btn_notificaSlogin.setFont(font7)
        self.btn_notificaSlogin.setStyleSheet(u"QPushButton#btn_notificaSlogin{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(110, 1, 0, 255), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notificaSlogin:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notificaSlogin:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Imagem/investigacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notificaSlogin.setIcon(icon4)
        self.btn_notificaSlogin.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.btn_notificaSlogin)


        self.gridLayout_7.addWidget(self.widget_2, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 72, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 1, 1, 2, 5)

        self.horizontalSpacer_9 = QSpacerItem(58, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 1, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(108, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 5, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_11 = QGridLayout(self.page_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_20)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_5 = QGroupBox(self.page_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(81, 51))
        self.groupBox_5.setMaximumSize(QSize(81, 51))
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.btn_dashboard = QPushButton(self.groupBox_5)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setGeometry(QRect(9, 16, 60, 30))
        self.btn_dashboard.setMinimumSize(QSize(60, 30))
        self.btn_dashboard.setMaximumSize(QSize(60, 30))
        self.btn_dashboard.setFont(font2)
        self.btn_dashboard.setStyleSheet(u"QPushButton#btn_dashboard{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_dashboard:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_dashboard:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(271, 51))
        self.groupBox_6.setMaximumSize(QSize(271, 51))
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.layoutWidget_3 = QWidget(self.groupBox_6)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(6, 14, 260, 32))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.btn_notifica = QPushButton(self.layoutWidget_3)
        self.btn_notifica.setObjectName(u"btn_notifica")
        self.btn_notifica.setMinimumSize(QSize(60, 30))
        self.btn_notifica.setMaximumSize(QSize(60, 30))
        self.btn_notifica.setFont(font3)
        self.btn_notifica.setStyleSheet(u"QPushButton#btn_notifica{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_notifica.setIcon(icon1)
        self.btn_notifica.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.btn_notifica)

        self.btn_usuarios = QPushButton(self.layoutWidget_3)
        self.btn_usuarios.setObjectName(u"btn_usuarios")
        self.btn_usuarios.setMinimumSize(QSize(60, 30))
        self.btn_usuarios.setMaximumSize(QSize(60, 30))
        self.btn_usuarios.setFont(font3)
        self.btn_usuarios.setStyleSheet(u"QPushButton#btn_usuarios{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_usuarios:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_usuarios:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Imagem/password.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usuarios.setIcon(icon5)
        self.btn_usuarios.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.btn_usuarios)

        self.btn_setor = QPushButton(self.layoutWidget_3)
        self.btn_setor.setObjectName(u"btn_setor")
        self.btn_setor.setMinimumSize(QSize(60, 30))
        self.btn_setor.setMaximumSize(QSize(60, 30))
        self.btn_setor.setFont(font3)
        self.btn_setor.setStyleSheet(u"QPushButton#btn_setor{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_setor:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_setor:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Imagem/grafico-de-setores.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setor.setIcon(icon6)
        self.btn_setor.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.btn_setor)

        self.btn_email = QPushButton(self.layoutWidget_3)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setMinimumSize(QSize(60, 30))
        self.btn_email.setMaximumSize(QSize(60, 30))
        self.btn_email.setFont(font3)
        self.btn_email.setStyleSheet(u"QPushButton#btn_email{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_email:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_email:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Imagem/marketing-de-email (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_email.setIcon(icon7)
        self.btn_email.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.btn_email)


        self.horizontalLayout_7.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.page_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(81, 51))
        self.groupBox_7.setMaximumSize(QSize(81, 51))
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.btn_investigar = QPushButton(self.groupBox_7)
        self.btn_investigar.setObjectName(u"btn_investigar")
        self.btn_investigar.setEnabled(True)
        self.btn_investigar.setGeometry(QRect(9, 17, 60, 30))
        self.btn_investigar.setMinimumSize(QSize(60, 30))
        self.btn_investigar.setMaximumSize(QSize(60, 30))
        self.btn_investigar.setFont(font3)
        self.btn_investigar.setStyleSheet(u"QPushButton#btn_investigar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_investigar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_investigar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_investigar.setIcon(icon4)
        self.btn_investigar.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.page_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(81, 51))
        self.groupBox_8.setMaximumSize(QSize(81, 51))
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.btn_consultar = QPushButton(self.groupBox_8)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setGeometry(QRect(10, 17, 60, 30))
        self.btn_consultar.setMinimumSize(QSize(60, 30))
        self.btn_consultar.setMaximumSize(QSize(60, 30))
        self.btn_consultar.setFont(font3)
        self.btn_consultar.setStyleSheet(u"QPushButton#btn_consultar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Imagem/pesquisa-de-dados (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consultar.setIcon(icon8)
        self.btn_consultar.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.page_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(81, 51))
        self.groupBox_9.setMaximumSize(QSize(81, 51))
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.btn_relatorio_2 = QPushButton(self.groupBox_9)
        self.btn_relatorio_2.setObjectName(u"btn_relatorio_2")
        self.btn_relatorio_2.setEnabled(True)
        self.btn_relatorio_2.setGeometry(QRect(10, 16, 60, 30))
        self.btn_relatorio_2.setMinimumSize(QSize(60, 30))
        self.btn_relatorio_2.setMaximumSize(QSize(60, 30))
        self.btn_relatorio_2.setFont(font3)
        self.btn_relatorio_2.setStyleSheet(u"QPushButton#btn_relatorio_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_relatorio_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_relatorio_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Imagem/relatorio-de-negocios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_2.setIcon(icon9)
        self.btn_relatorio_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.groupBox_9)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.groupBox_10 = QGroupBox(self.page_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(81, 51))
        self.groupBox_10.setMaximumSize(QSize(81, 51))
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.btn_logoff = QPushButton(self.groupBox_10)
        self.btn_logoff.setObjectName(u"btn_logoff")
        self.btn_logoff.setGeometry(QRect(6, 16, 60, 30))
        self.btn_logoff.setMinimumSize(QSize(60, 30))
        self.btn_logoff.setMaximumSize(QSize(60, 30))
        self.btn_logoff.setFont(font3)
        self.btn_logoff.setStyleSheet(u"QPushButton#btn_logoff{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_logoff:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_logoff:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Imagem/check-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logoff.setIcon(icon10)
        self.btn_logoff.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.page_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(81, 51))
        self.groupBox_11.setMaximumSize(QSize(81, 51))
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.btn_sairApp = QPushButton(self.groupBox_11)
        self.btn_sairApp.setObjectName(u"btn_sairApp")
        self.btn_sairApp.setGeometry(QRect(9, 16, 60, 30))
        self.btn_sairApp.setMinimumSize(QSize(60, 30))
        self.btn_sairApp.setMaximumSize(QSize(60, 30))
        self.btn_sairApp.setFont(font3)
        self.btn_sairApp.setStyleSheet(u"QPushButton#btn_sairApp{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sairApp:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sairApp:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Imagem/remover (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sairApp.setIcon(icon11)
        self.btn_sairApp.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.groupBox_11)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)

        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(780, 490))
        self.label_2.setStyleSheet(u"image: url(:/Imagem/FNEA.jpg);")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.gridLayout_11.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_30 = QGroupBox(self.page_3)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setMinimumSize(QSize(181, 61))
        self.groupBox_30.setMaximumSize(QSize(16777215, 61))
        self.groupBox_30.setAlignment(Qt.AlignCenter)
        self.btn_notificar = QPushButton(self.groupBox_30)
        self.btn_notificar.setObjectName(u"btn_notificar")
        self.btn_notificar.setGeometry(QRect(15, 19, 30, 30))
        self.btn_notificar.setMinimumSize(QSize(30, 30))
        self.btn_notificar.setMaximumSize(QSize(30, 30))
        self.btn_notificar.setFont(font3)
        self.btn_notificar.setStyleSheet(u"QPushButton#btn_notificar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notificar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notificar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Imagem/registro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notificar.setIcon(icon12)
        self.btn_notificar.setIconSize(QSize(24, 24))
        self.btn_editarNoti = QPushButton(self.groupBox_30)
        self.btn_editarNoti.setObjectName(u"btn_editarNoti")
        self.btn_editarNoti.setGeometry(QRect(75, 19, 30, 30))
        self.btn_editarNoti.setMinimumSize(QSize(30, 30))
        self.btn_editarNoti.setMaximumSize(QSize(30, 30))
        self.btn_editarNoti.setFont(font3)
        self.btn_editarNoti.setStyleSheet(u"QPushButton#btn_editarNoti{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editarNoti:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editarNoti:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Imagem/registro (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editarNoti.setIcon(icon13)
        self.btn_editarNoti.setIconSize(QSize(24, 24))
        self.btn_buscarMv = QPushButton(self.groupBox_30)
        self.btn_buscarMv.setObjectName(u"btn_buscarMv")
        self.btn_buscarMv.setEnabled(True)
        self.btn_buscarMv.setGeometry(QRect(132, 18, 30, 30))
        self.btn_buscarMv.setMinimumSize(QSize(30, 30))
        self.btn_buscarMv.setMaximumSize(QSize(30, 30))
        self.btn_buscarMv.setFont(font2)
        self.btn_buscarMv.setStyleSheet(u"QPushButton#btn_buscarMv{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_buscarMv:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_buscarMv:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_buscarMv.setIcon(icon8)
        self.btn_buscarMv.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_30)

        self.groupBox_33 = QGroupBox(self.page_3)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(180, 61))
        self.groupBox_33.setMaximumSize(QSize(16777215, 61))
        self.groupBox_33.setAlignment(Qt.AlignCenter)
        self.txt_consultaNoti = QLineEdit(self.groupBox_33)
        self.txt_consultaNoti.setObjectName(u"txt_consultaNoti")
        self.txt_consultaNoti.setGeometry(QRect(10, 30, 121, 20))
        self.txt_consultaNoti.setMinimumSize(QSize(100, 20))
        self.txt_consultaNoti.setMaximumSize(QSize(167777, 20))
        self.txt_consultaNoti.setFont(font1)
        self.txt_consultaNoti.setStyleSheet(u"\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")
        self.txt_consultaNoti.setAlignment(Qt.AlignCenter)
        self.btn_pesquisarNoti = QPushButton(self.groupBox_33)
        self.btn_pesquisarNoti.setObjectName(u"btn_pesquisarNoti")
        self.btn_pesquisarNoti.setGeometry(QRect(140, 20, 30, 30))
        self.btn_pesquisarNoti.setMinimumSize(QSize(30, 30))
        self.btn_pesquisarNoti.setMaximumSize(QSize(30, 30))
        self.btn_pesquisarNoti.setFont(font3)
        self.btn_pesquisarNoti.setStyleSheet(u"QPushButton#btn_pesquisarNoti{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisarNoti:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisarNoti:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Imagem/historia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisarNoti.setIcon(icon14)
        self.btn_pesquisarNoti.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_33)

        self.groupBox_31 = QGroupBox(self.page_3)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setMinimumSize(QSize(80, 61))
        self.groupBox_31.setMaximumSize(QSize(16777215, 61))
        self.groupBox_31.setAlignment(Qt.AlignCenter)
        self.btn_relatorio = QPushButton(self.groupBox_31)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setEnabled(True)
        self.btn_relatorio.setGeometry(QRect(30, 20, 30, 30))
        self.btn_relatorio.setMinimumSize(QSize(30, 30))
        self.btn_relatorio.setMaximumSize(QSize(30, 30))
        self.btn_relatorio.setFont(font3)
        self.btn_relatorio.setStyleSheet(u"QPushButton#btn_relatorio{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_relatorio:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_relatorio:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Imagem/pdf (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio.setIcon(icon15)
        self.btn_relatorio.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_31)

        self.groupBox_32 = QGroupBox(self.page_3)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setMinimumSize(QSize(105, 61))
        self.groupBox_32.setMaximumSize(QSize(16777215, 61))
        self.groupBox_32.setAlignment(Qt.AlignCenter)
        self.btn_salva_noti = QPushButton(self.groupBox_32)
        self.btn_salva_noti.setObjectName(u"btn_salva_noti")
        self.btn_salva_noti.setEnabled(False)
        self.btn_salva_noti.setGeometry(QRect(6, 21, 30, 30))
        self.btn_salva_noti.setMinimumSize(QSize(30, 30))
        self.btn_salva_noti.setMaximumSize(QSize(30, 30))
        self.btn_salva_noti.setFont(font1)
        self.btn_salva_noti.setStyleSheet(u"QPushButton#btn_salva_noti{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salva_noti:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salva_noti:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/Imagem/salve-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salva_noti.setIcon(icon16)
        self.btn_salva_noti.setIconSize(QSize(24, 24))
        self.btn_cancela_noti = QPushButton(self.groupBox_32)
        self.btn_cancela_noti.setObjectName(u"btn_cancela_noti")
        self.btn_cancela_noti.setEnabled(False)
        self.btn_cancela_noti.setGeometry(QRect(58, 21, 30, 30))
        self.btn_cancela_noti.setMinimumSize(QSize(30, 30))
        self.btn_cancela_noti.setMaximumSize(QSize(30, 30))
        self.btn_cancela_noti.setFont(font1)
        self.btn_cancela_noti.setStyleSheet(u"QPushButton#btn_cancela_noti{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_noti:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_noti:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/Imagem/cancelar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancela_noti.setIcon(icon17)
        self.btn_cancela_noti.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_32)

        self.groupBox_34 = QGroupBox(self.page_3)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMinimumSize(QSize(101, 61))
        self.groupBox_34.setMaximumSize(QSize(101, 61))
        self.btn_alterar = QPushButton(self.groupBox_34)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setEnabled(False)
        self.btn_alterar.setGeometry(QRect(33, 20, 30, 30))
        self.btn_alterar.setMinimumSize(QSize(30, 30))
        self.btn_alterar.setMaximumSize(QSize(30, 30))
        self.btn_alterar.setFont(font1)
        self.btn_alterar.setStyleSheet(u"QPushButton#btn_alterar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterar.setIcon(icon13)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_34)

        self.groupBox_35 = QGroupBox(self.page_3)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setMinimumSize(QSize(131, 61))
        self.groupBox_35.setMaximumSize(QSize(131, 61))
        self.btn_resumoInvest = QPushButton(self.groupBox_35)
        self.btn_resumoInvest.setObjectName(u"btn_resumoInvest")
        self.btn_resumoInvest.setEnabled(True)
        self.btn_resumoInvest.setGeometry(QRect(45, 21, 30, 30))
        self.btn_resumoInvest.setMinimumSize(QSize(30, 30))
        self.btn_resumoInvest.setMaximumSize(QSize(30, 30))
        self.btn_resumoInvest.setFont(font1)
        self.btn_resumoInvest.setStyleSheet(u"QPushButton#btn_resumoInvest{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumoInvest:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumoInvest:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/Imagem/resumo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resumoInvest.setIcon(icon18)
        self.btn_resumoInvest.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_35)

        self.groupBox_36 = QGroupBox(self.page_3)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setMinimumSize(QSize(61, 61))
        self.groupBox_36.setMaximumSize(QSize(61, 61))
        self.groupBox_36.setAlignment(Qt.AlignCenter)
        self.btn_voltar = QPushButton(self.groupBox_36)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setEnabled(True)
        self.btn_voltar.setGeometry(QRect(15, 20, 30, 30))
        self.btn_voltar.setMinimumSize(QSize(30, 30))
        self.btn_voltar.setMaximumSize(QSize(30, 30))
        self.btn_voltar.setFont(font1)
        self.btn_voltar.setStyleSheet(u"QPushButton#btn_voltar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/Imagem/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voltar.setIcon(icon19)
        self.btn_voltar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.groupBox_36)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_21 = QFrame(self.page_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(901, 91))
        self.frame_21.setMaximumSize(QSize(901, 91))
        self.frame_21.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.frame_21.setFrameShape(QFrame.Box)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(1)
        self.frame_21.setMidLineWidth(0)
        self.layoutWidget_6 = QWidget(self.frame_21)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(22, 49, 793, 38))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.layoutWidget_6)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font1)
        self.label_70.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_70)

        self.cb_sex = QComboBox(self.layoutWidget_6)
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.setObjectName(u"cb_sex")
        self.cb_sex.setEnabled(False)
        self.cb_sex.setMaximumSize(QSize(85, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        self.cb_sex.setFont(font8)
        self.cb_sex.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_4.addWidget(self.cb_sex)

        self.label_71 = QLabel(self.layoutWidget_6)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font1)
        self.label_71.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_71)

        self.cb_seto = QComboBox(self.layoutWidget_6)
        self.cb_seto.setObjectName(u"cb_seto")
        self.cb_seto.setEnabled(False)
        self.cb_seto.setMinimumSize(QSize(150, 0))
        self.cb_seto.setMaximumSize(QSize(150, 16777215))
        self.cb_seto.setFont(font8)
        self.cb_seto.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_4.addWidget(self.cb_seto)

        self.label_72 = QLabel(self.layoutWidget_6)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(90, 16777215))
        self.label_72.setFont(font1)
        self.label_72.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_72)

        self.txt_leit = QLineEdit(self.layoutWidget_6)
        self.txt_leit.setObjectName(u"txt_leit")
        self.txt_leit.setEnabled(False)
        self.txt_leit.setMaximumSize(QSize(90, 16777215))
        self.txt_leit.setFont(font8)
        self.txt_leit.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_4.addWidget(self.txt_leit)

        self.label_73 = QLabel(self.layoutWidget_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font1)
        self.label_73.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_73)

        self.dt_internacao = QDateEdit(self.layoutWidget_6)
        self.dt_internacao.setObjectName(u"dt_internacao")
        self.dt_internacao.setEnabled(False)
        self.dt_internacao.setMinimumSize(QSize(101, 0))
        self.dt_internacao.setFont(font8)
        self.dt_internacao.setDateTime(QDateTime(QDate(2022, 1, 2), QTime(3, 0, 0)))
        self.dt_internacao.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dt_internacao)

        self.label_66 = QLabel(self.layoutWidget_6)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_66)

        self.cb_rac = QComboBox(self.layoutWidget_6)
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.setObjectName(u"cb_rac")
        self.cb_rac.setEnabled(False)
        self.cb_rac.setMaximumSize(QSize(90, 16777215))
        self.cb_rac.setFont(font8)
        self.cb_rac.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_4.addWidget(self.cb_rac)

        self.layoutWidget_7 = QWidget(self.frame_21)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(22, 9, 861, 40))
        self.horizontalLayout_22 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.layoutWidget_7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font1)
        self.label_67.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_67)

        self.txt_codPacient = QLineEdit(self.layoutWidget_7)
        self.txt_codPacient.setObjectName(u"txt_codPacient")
        self.txt_codPacient.setEnabled(False)
        self.txt_codPacient.setMinimumSize(QSize(60, 0))
        self.txt_codPacient.setMaximumSize(QSize(90, 16777215))
        self.txt_codPacient.setFont(font8)
        self.txt_codPacient.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_22.addWidget(self.txt_codPacient)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_68 = QLabel(self.layoutWidget_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font1)
        self.label_68.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_68)

        self.txt_nmPacient = QLineEdit(self.layoutWidget_7)
        self.txt_nmPacient.setObjectName(u"txt_nmPacient")
        self.txt_nmPacient.setEnabled(False)
        self.txt_nmPacient.setMinimumSize(QSize(250, 0))
        self.txt_nmPacient.setMaximumSize(QSize(400, 16777215))
        self.txt_nmPacient.setFont(font8)
        self.txt_nmPacient.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_21.addWidget(self.txt_nmPacient)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)

        self.label_82 = QLabel(self.layoutWidget_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font1)
        self.label_82.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_82)

        self.txt_social = QLineEdit(self.layoutWidget_7)
        self.txt_social.setObjectName(u"txt_social")
        self.txt_social.setEnabled(False)
        self.txt_social.setMinimumSize(QSize(60, 0))
        self.txt_social.setMaximumSize(QSize(90, 16777215))
        self.txt_social.setFont(font8)
        self.txt_social.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_22.addWidget(self.txt_social)

        self.label_69 = QLabel(self.layoutWidget_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font1)
        self.label_69.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_69)

        self.dt_nascimento = QDateEdit(self.layoutWidget_7)
        self.dt_nascimento.setObjectName(u"dt_nascimento")
        self.dt_nascimento.setEnabled(False)
        self.dt_nascimento.setMinimumSize(QSize(101, 0))
        self.dt_nascimento.setFont(font8)
        self.dt_nascimento.setDateTime(QDateTime(QDate(2022, 1, 2), QTime(3, 0, 0)))
        self.dt_nascimento.setCalendarPopup(True)

        self.horizontalLayout_22.addWidget(self.dt_nascimento)


        self.verticalLayout_6.addWidget(self.frame_21)

        self.frame_19 = QFrame(self.page_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(901, 91))
        self.frame_19.setMaximumSize(QSize(901, 91))
        self.frame_19.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.layoutWidget_8 = QWidget(self.frame_19)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(21, 6, 856, 77))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_62 = QLabel(self.layoutWidget_8)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)
        self.label_62.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_62)

        self.txt_diagnostic = QLineEdit(self.layoutWidget_8)
        self.txt_diagnostic.setObjectName(u"txt_diagnostic")
        self.txt_diagnostic.setEnabled(False)
        self.txt_diagnostic.setMinimumSize(QSize(301, 0))
        self.txt_diagnostic.setFont(font8)
        self.txt_diagnostic.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_25.addWidget(self.txt_diagnostic)

        self.label_63 = QLabel(self.layoutWidget_8)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)
        self.label_63.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_63)

        self.txt_tratamento = QLineEdit(self.layoutWidget_8)
        self.txt_tratamento.setObjectName(u"txt_tratamento")
        self.txt_tratamento.setEnabled(False)
        self.txt_tratamento.setMinimumSize(QSize(401, 0))
        self.txt_tratamento.setFont(font8)
        self.txt_tratamento.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_25.addWidget(self.txt_tratamento)


        self.verticalLayout_20.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_64 = QLabel(self.layoutWidget_8)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font1)
        self.label_64.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_64)

        self.dt_evento = QDateEdit(self.layoutWidget_8)
        self.dt_evento.setObjectName(u"dt_evento")
        self.dt_evento.setEnabled(False)
        self.dt_evento.setMinimumSize(QSize(101, 0))
        self.dt_evento.setMaximumSize(QSize(101, 16777215))
        self.dt_evento.setFont(font8)
        self.dt_evento.setDateTime(QDateTime(QDate(2022, 1, 2), QTime(3, 0, 0)))
        self.dt_evento.setCalendarPopup(True)

        self.horizontalLayout_23.addWidget(self.dt_evento)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.rb_mt = QRadioButton(self.layoutWidget_8)
        self.rb_mt.setObjectName(u"rb_mt")
        self.rb_mt.setEnabled(False)
        self.rb_mt.setFont(font1)

        self.horizontalLayout_24.addWidget(self.rb_mt)

        self.rb_sn = QRadioButton(self.layoutWidget_8)
        self.rb_sn.setObjectName(u"rb_sn")
        self.rb_sn.setEnabled(False)
        self.rb_sn.setFont(font1)

        self.horizontalLayout_24.addWidget(self.rb_sn)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_65 = QLabel(self.layoutWidget_8)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_65)

        self.dt_notificacao = QDateEdit(self.layoutWidget_8)
        self.dt_notificacao.setObjectName(u"dt_notificacao")
        self.dt_notificacao.setEnabled(False)
        self.dt_notificacao.setMinimumSize(QSize(101, 0))
        self.dt_notificacao.setFont(font8)
        self.dt_notificacao.setDateTime(QDateTime(QDate(2022, 1, 2), QTime(3, 0, 0)))
        self.dt_notificacao.setCalendarPopup(True)

        self.horizontalLayout_17.addWidget(self.dt_notificacao)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_17)

        self.chk_nsp = QCheckBox(self.layoutWidget_8)
        self.chk_nsp.setObjectName(u"chk_nsp")
        self.chk_nsp.setEnabled(False)
        self.chk_nsp.setFont(font1)

        self.horizontalLayout_26.addWidget(self.chk_nsp)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)


        self.verticalLayout_6.addWidget(self.frame_19)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.tabWidget_2 = QTabWidget(self.page_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(901, 361))
        self.tabWidget_2.setMaximumSize(QSize(901, 361))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 13, 870, 307))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ck_falha_id = QCheckBox(self.layoutWidget)
        self.ck_falha_id.setObjectName(u"ck_falha_id")
        self.ck_falha_id.setEnabled(False)
        self.ck_falha_id.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_id)

        self.ck_falha_comu = QCheckBox(self.layoutWidget)
        self.ck_falha_comu.setObjectName(u"ck_falha_comu")
        self.ck_falha_comu.setEnabled(False)
        self.ck_falha_comu.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_comu)

        self.ck_falha_oxi = QCheckBox(self.layoutWidget)
        self.ck_falha_oxi.setObjectName(u"ck_falha_oxi")
        self.ck_falha_oxi.setEnabled(False)
        self.ck_falha_oxi.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_oxi)

        self.ck_falha_sonda = QCheckBox(self.layoutWidget)
        self.ck_falha_sonda.setObjectName(u"ck_falha_sonda")
        self.ck_falha_sonda.setEnabled(False)
        self.ck_falha_sonda.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_sonda)

        self.ck_falha_nutri = QCheckBox(self.layoutWidget)
        self.ck_falha_nutri.setObjectName(u"ck_falha_nutri")
        self.ck_falha_nutri.setEnabled(False)
        self.ck_falha_nutri.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_nutri)

        self.ck_falha_hemo = QCheckBox(self.layoutWidget)
        self.ck_falha_hemo.setObjectName(u"ck_falha_hemo")
        self.ck_falha_hemo.setEnabled(False)
        self.ck_falha_hemo.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_hemo)

        self.ck_falha_med = QCheckBox(self.layoutWidget)
        self.ck_falha_med.setObjectName(u"ck_falha_med")
        self.ck_falha_med.setEnabled(False)
        self.ck_falha_med.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_med)

        self.ck_falha_usu = QCheckBox(self.layoutWidget)
        self.ck_falha_usu.setObjectName(u"ck_falha_usu")
        self.ck_falha_usu.setEnabled(False)
        self.ck_falha_usu.setFont(font1)

        self.verticalLayout_2.addWidget(self.ck_falha_usu)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ck_falha_anest_2 = QCheckBox(self.layoutWidget)
        self.ck_falha_anest_2.setObjectName(u"ck_falha_anest_2")
        self.ck_falha_anest_2.setEnabled(False)
        self.ck_falha_anest_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_falha_anest_2)

        self.ck_falha_dispo_2 = QCheckBox(self.layoutWidget)
        self.ck_falha_dispo_2.setObjectName(u"ck_falha_dispo_2")
        self.ck_falha_dispo_2.setEnabled(False)
        self.ck_falha_dispo_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_falha_dispo_2)

        self.ck_queda_hosp_2 = QCheckBox(self.layoutWidget)
        self.ck_queda_hosp_2.setObjectName(u"ck_queda_hosp_2")
        self.ck_queda_hosp_2.setEnabled(False)
        self.ck_queda_hosp_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_queda_hosp_2)

        self.ck_falha_cirurg_2 = QCheckBox(self.layoutWidget)
        self.ck_falha_cirurg_2.setObjectName(u"ck_falha_cirurg_2")
        self.ck_falha_cirurg_2.setEnabled(False)
        self.ck_falha_cirurg_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_falha_cirurg_2)

        self.ck_ulcera_2 = QCheckBox(self.layoutWidget)
        self.ck_ulcera_2.setObjectName(u"ck_ulcera_2")
        self.ck_ulcera_2.setEnabled(False)
        self.ck_ulcera_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_ulcera_2)

        self.ck_infeccao_2 = QCheckBox(self.layoutWidget)
        self.ck_infeccao_2.setObjectName(u"ck_infeccao_2")
        self.ck_infeccao_2.setEnabled(False)
        self.ck_infeccao_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_infeccao_2)

        self.ck_inadequada_2 = QCheckBox(self.layoutWidget)
        self.ck_inadequada_2.setObjectName(u"ck_inadequada_2")
        self.ck_inadequada_2.setEnabled(False)
        self.ck_inadequada_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_inadequada_2)

        self.ck_higiene_paciente_2 = QCheckBox(self.layoutWidget)
        self.ck_higiene_paciente_2.setObjectName(u"ck_higiene_paciente_2")
        self.ck_higiene_paciente_2.setEnabled(False)
        self.ck_higiene_paciente_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.ck_higiene_paciente_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ck_neonato_2 = QCheckBox(self.layoutWidget)
        self.ck_neonato_2.setObjectName(u"ck_neonato_2")
        self.ck_neonato_2.setEnabled(False)
        self.ck_neonato_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_neonato_2)

        self.ck_vaginal_2 = QCheckBox(self.layoutWidget)
        self.ck_vaginal_2.setObjectName(u"ck_vaginal_2")
        self.ck_vaginal_2.setEnabled(False)
        self.ck_vaginal_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_vaginal_2)

        self.ck_cesariana_2 = QCheckBox(self.layoutWidget)
        self.ck_cesariana_2.setObjectName(u"ck_cesariana_2")
        self.ck_cesariana_2.setEnabled(False)
        self.ck_cesariana_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_cesariana_2)

        self.ck_atendimento_2 = QCheckBox(self.layoutWidget)
        self.ck_atendimento_2.setObjectName(u"ck_atendimento_2")
        self.ck_atendimento_2.setEnabled(False)
        self.ck_atendimento_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_atendimento_2)

        self.ck_conflito_2 = QCheckBox(self.layoutWidget)
        self.ck_conflito_2.setObjectName(u"ck_conflito_2")
        self.ck_conflito_2.setEnabled(False)
        self.ck_conflito_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_conflito_2)

        self.ck_evasao_2 = QCheckBox(self.layoutWidget)
        self.ck_evasao_2.setObjectName(u"ck_evasao_2")
        self.ck_evasao_2.setEnabled(False)
        self.ck_evasao_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_evasao_2)

        self.ck_sentinela_2 = QCheckBox(self.layoutWidget)
        self.ck_sentinela_2.setObjectName(u"ck_sentinela_2")
        self.ck_sentinela_2.setEnabled(False)
        self.ck_sentinela_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_sentinela_2)

        self.ck_queimadura_2 = QCheckBox(self.layoutWidget)
        self.ck_queimadura_2.setObjectName(u"ck_queimadura_2")
        self.ck_queimadura_2.setEnabled(False)
        self.ck_queimadura_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.ck_queimadura_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ck_outros_2 = QCheckBox(self.layoutWidget)
        self.ck_outros_2.setObjectName(u"ck_outros_2")
        self.ck_outros_2.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.ck_outros_2)

        self.ds_outros = QLineEdit(self.layoutWidget)
        self.ds_outros.setObjectName(u"ds_outros")
        self.ds_outros.setEnabled(True)
        self.ds_outros.setMinimumSize(QSize(800, 31))
        self.ds_outros.setMaximumSize(QSize(800, 31))
        self.ds_outros.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_14.addWidget(self.ds_outros)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_74 = QLabel(self.tab_4)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(342, 24, 171, 16))
        font9 = QFont()
        font9.setFamilies([u"Reem Kufi"])
        font9.setPointSize(7)
        font9.setBold(True)
        self.label_74.setFont(font9)
        self.label_74.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_74.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.tab_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(37, 42, 826, 283))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.txt_ocorrencia = QTextEdit(self.layoutWidget1)
        self.txt_ocorrencia.setObjectName(u"txt_ocorrencia")
        self.txt_ocorrencia.setEnabled(False)
        self.txt_ocorrencia.setMinimumSize(QSize(400, 211))
        self.txt_ocorrencia.setFont(font8)
        self.txt_ocorrencia.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_17.addWidget(self.txt_ocorrencia)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_75 = QLabel(self.layoutWidget1)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font9)
        self.label_75.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_75)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.rb_dano_sim = QRadioButton(self.layoutWidget1)
        self.rb_dano_sim.setObjectName(u"rb_dano_sim")
        self.rb_dano_sim.setEnabled(False)
        self.rb_dano_sim.setFont(font1)

        self.horizontalLayout_29.addWidget(self.rb_dano_sim)

        self.rb_dano_nao = QRadioButton(self.layoutWidget1)
        self.rb_dano_nao.setObjectName(u"rb_dano_nao")
        self.rb_dano_nao.setEnabled(False)
        self.rb_dano_nao.setFont(font1)

        self.horizontalLayout_29.addWidget(self.rb_dano_nao)

        self.rb_dano_SI = QRadioButton(self.layoutWidget1)
        self.rb_dano_SI.setObjectName(u"rb_dano_SI")
        self.rb_dano_SI.setEnabled(False)
        self.rb_dano_SI.setFont(font1)

        self.horizontalLayout_29.addWidget(self.rb_dano_SI)


        self.verticalLayout_16.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_16.addLayout(self.verticalLayout_16)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_76 = QLabel(self.layoutWidget1)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(343, 0))
        self.label_76.setMaximumSize(QSize(343, 16777215))
        self.label_76.setFont(font9)
        self.label_76.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_76)

        self.cb_dan = QComboBox(self.layoutWidget1)
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.setObjectName(u"cb_dan")
        self.cb_dan.setEnabled(False)
        self.cb_dan.setMinimumSize(QSize(661, 0))
        self.cb_dan.setMaximumSize(QSize(661, 16777215))
        self.cb_dan.setFont(font1)
        self.cb_dan.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_5.addWidget(self.cb_dan)


        self.horizontalLayout_16.addLayout(self.verticalLayout_5)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.layoutWidget2 = QWidget(self.tab_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(39, 3, 814, 325))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_77 = QLabel(self.layoutWidget2)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font9)
        self.label_77.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_77)

        self.txt_como = QTextEdit(self.layoutWidget2)
        self.txt_como.setObjectName(u"txt_como")
        self.txt_como.setEnabled(False)
        self.txt_como.setMinimumSize(QSize(400, 211))
        self.txt_como.setMaximumSize(QSize(400, 211))
        self.txt_como.setFont(font8)
        self.txt_como.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_22.addWidget(self.txt_como)


        self.horizontalLayout_20.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_78 = QLabel(self.layoutWidget2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font9)
        self.label_78.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_78)

        self.txt_acao = QTextEdit(self.layoutWidget2)
        self.txt_acao.setObjectName(u"txt_acao")
        self.txt_acao.setEnabled(False)
        self.txt_acao.setMinimumSize(QSize(400, 211))
        self.txt_acao.setMaximumSize(QSize(400, 211))
        self.txt_acao.setFont(font8)
        self.txt_acao.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_23.addWidget(self.txt_acao)


        self.horizontalLayout_20.addLayout(self.verticalLayout_23)


        self.verticalLayout_24.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_79 = QLabel(self.layoutWidget2)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font9)
        self.label_79.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_79)

        self.txt_quem = QTextEdit(self.layoutWidget2)
        self.txt_quem.setObjectName(u"txt_quem")
        self.txt_quem.setEnabled(False)
        self.txt_quem.setMinimumSize(QSize(400, 50))
        self.txt_quem.setMaximumSize(QSize(400, 50))
        self.txt_quem.setFont(font8)
        self.txt_quem.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_18.addWidget(self.txt_quem)


        self.horizontalLayout_18.addLayout(self.verticalLayout_18)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_80 = QLabel(self.layoutWidget2)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font9)
        self.label_80.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_80)

        self.txt_identificacao = QTextEdit(self.layoutWidget2)
        self.txt_identificacao.setObjectName(u"txt_identificacao")
        self.txt_identificacao.setEnabled(False)
        self.txt_identificacao.setMinimumSize(QSize(400, 50))
        self.txt_identificacao.setMaximumSize(QSize(400, 50))
        self.txt_identificacao.setFont(font8)
        self.txt_identificacao.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_21.addWidget(self.txt_identificacao)


        self.horizontalLayout_18.addLayout(self.verticalLayout_21)


        self.verticalLayout_24.addLayout(self.horizontalLayout_18)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_8.addWidget(self.tabWidget_2)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_6 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")
        font10 = QFont()
        font10.setFamilies([u"Reem Kufi"])
        font10.setPointSize(9)
        font10.setBold(False)
        self.label_17.setFont(font10)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(258, 40, 441, 101))
        self.label_3.setStyleSheet(u"image: url(:/Imagem/Peixe.jpg);")
        self.label_98 = QLabel(self.page_4)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(160, 10, 691, 20))
        self.label_98.setFont(font7)
        self.label_98.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_98.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.page_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(52, 250, 911, 401))
        self.tabWidget.setMinimumSize(QSize(911, 361))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget3 = QWidget(self.tab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(11, 11, 882, 357))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_16 = QGroupBox(self.layoutWidget3)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(871, 51))
        self.txt_paciente = QLineEdit(self.groupBox_16)
        self.txt_paciente.setObjectName(u"txt_paciente")
        self.txt_paciente.setEnabled(False)
        self.txt_paciente.setGeometry(QRect(5, 21, 871, 21))
        self.txt_paciente.setMinimumSize(QSize(200, 21))
        self.txt_paciente.setFont(font8)
        self.txt_paciente.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_11.addWidget(self.groupBox_16)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_17 = QGroupBox(self.layoutWidget3)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(435, 51))
        self.groupBox_17.setMaximumSize(QSize(435, 51))
        self.txt_pessoas = QLineEdit(self.groupBox_17)
        self.txt_pessoas.setObjectName(u"txt_pessoas")
        self.txt_pessoas.setEnabled(False)
        self.txt_pessoas.setGeometry(QRect(7, 15, 421, 31))
        self.txt_pessoas.setMinimumSize(QSize(390, 0))
        self.txt_pessoas.setFont(font8)
        self.txt_pessoas.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_8.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.layoutWidget3)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMinimumSize(QSize(435, 51))
        self.groupBox_18.setMaximumSize(QSize(435, 51))
        self.txt_processos = QLineEdit(self.groupBox_18)
        self.txt_processos.setObjectName(u"txt_processos")
        self.txt_processos.setEnabled(False)
        self.txt_processos.setGeometry(QRect(9, 15, 421, 31))
        self.txt_processos.setMinimumSize(QSize(390, 0))
        self.txt_processos.setFont(font8)
        self.txt_processos.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_8.addWidget(self.groupBox_18)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.groupBox_19 = QGroupBox(self.layoutWidget3)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(871, 51))
        self.groupBox_19.setMaximumSize(QSize(16777215, 16777215))
        self.txt_equipamentos = QLineEdit(self.groupBox_19)
        self.txt_equipamentos.setObjectName(u"txt_equipamentos")
        self.txt_equipamentos.setEnabled(False)
        self.txt_equipamentos.setGeometry(QRect(10, 16, 861, 31))
        self.txt_equipamentos.setMinimumSize(QSize(390, 0))
        self.txt_equipamentos.setFont(font8)
        self.txt_equipamentos.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_11.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.layoutWidget3)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMinimumSize(QSize(871, 51))
        self.groupBox_20.setMaximumSize(QSize(16777215, 16777215))
        self.txt_ambiente = QLineEdit(self.groupBox_20)
        self.txt_ambiente.setObjectName(u"txt_ambiente")
        self.txt_ambiente.setEnabled(False)
        self.txt_ambiente.setGeometry(QRect(10, 15, 861, 31))
        self.txt_ambiente.setMinimumSize(QSize(390, 0))
        self.txt_ambiente.setFont(font8)
        self.txt_ambiente.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_11.addWidget(self.groupBox_20)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_21 = QGroupBox(self.layoutWidget3)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(435, 121))
        self.txt_observacao_2 = QTextEdit(self.groupBox_21)
        self.txt_observacao_2.setObjectName(u"txt_observacao_2")
        self.txt_observacao_2.setEnabled(False)
        self.txt_observacao_2.setGeometry(QRect(7, 16, 420, 100))
        self.txt_observacao_2.setMinimumSize(QSize(355, 100))
        self.txt_observacao_2.setMaximumSize(QSize(420, 100))
        self.txt_observacao_2.setFont(font8)
        self.txt_observacao_2.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_3.addWidget(self.groupBox_21)

        self.groupBox_22 = QGroupBox(self.layoutWidget3)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(435, 121))
        self.txt_recomendacao_4 = QTextEdit(self.groupBox_22)
        self.txt_recomendacao_4.setObjectName(u"txt_recomendacao_4")
        self.txt_recomendacao_4.setEnabled(False)
        self.txt_recomendacao_4.setGeometry(QRect(14, 16, 410, 100))
        self.txt_recomendacao_4.setMinimumSize(QSize(355, 100))
        self.txt_recomendacao_4.setMaximumSize(QSize(410, 100))
        self.txt_recomendacao_4.setFont(font8)
        self.txt_recomendacao_4.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_3.addWidget(self.groupBox_22)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_28 = QGroupBox(self.tab_2)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setGeometry(QRect(20, 129, 435, 51))
        self.groupBox_28.setMinimumSize(QSize(435, 51))
        self.txt_pessoas_12 = QLineEdit(self.groupBox_28)
        self.txt_pessoas_12.setObjectName(u"txt_pessoas_12")
        self.txt_pessoas_12.setEnabled(False)
        self.txt_pessoas_12.setGeometry(QRect(10, 16, 411, 31))
        self.txt_pessoas_12.setMinimumSize(QSize(411, 0))
        self.txt_pessoas_12.setFont(font8)
        self.txt_pessoas_12.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.groupBox_29 = QGroupBox(self.tab_2)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(20, 182, 881, 91))
        self.groupBox_29.setMinimumSize(QSize(435, 51))
        self.txt_recomendacao_3 = QTextEdit(self.groupBox_29)
        self.txt_recomendacao_3.setObjectName(u"txt_recomendacao_3")
        self.txt_recomendacao_3.setEnabled(False)
        self.txt_recomendacao_3.setGeometry(QRect(6, 27, 871, 57))
        self.txt_recomendacao_3.setMinimumSize(QSize(871, 51))
        self.txt_recomendacao_3.setFont(font8)
        self.txt_recomendacao_3.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.layoutWidget4 = QWidget(self.tab_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 10, 880, 114))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_24 = QGroupBox(self.layoutWidget4)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(435, 51))
        self.txt_pessoas_8 = QLineEdit(self.groupBox_24)
        self.txt_pessoas_8.setObjectName(u"txt_pessoas_8")
        self.txt_pessoas_8.setEnabled(False)
        self.txt_pessoas_8.setGeometry(QRect(10, 17, 411, 31))
        self.txt_pessoas_8.setMinimumSize(QSize(411, 0))
        self.txt_pessoas_8.setFont(font8)
        self.txt_pessoas_8.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_9.addWidget(self.groupBox_24)

        self.groupBox_25 = QGroupBox(self.layoutWidget4)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(435, 51))
        self.txt_pessoas_9 = QLineEdit(self.groupBox_25)
        self.txt_pessoas_9.setObjectName(u"txt_pessoas_9")
        self.txt_pessoas_9.setEnabled(False)
        self.txt_pessoas_9.setGeometry(QRect(10, 18, 411, 31))
        self.txt_pessoas_9.setMinimumSize(QSize(411, 0))
        self.txt_pessoas_9.setFont(font8)
        self.txt_pessoas_9.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_9.addWidget(self.groupBox_25)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_26 = QGroupBox(self.layoutWidget4)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setMinimumSize(QSize(435, 51))
        self.txt_pessoas_11 = QLineEdit(self.groupBox_26)
        self.txt_pessoas_11.setObjectName(u"txt_pessoas_11")
        self.txt_pessoas_11.setEnabled(False)
        self.txt_pessoas_11.setGeometry(QRect(10, 16, 411, 31))
        self.txt_pessoas_11.setMinimumSize(QSize(411, 0))
        self.txt_pessoas_11.setFont(font8)
        self.txt_pessoas_11.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_13.addWidget(self.groupBox_26)

        self.groupBox_27 = QGroupBox(self.layoutWidget4)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(435, 51))
        self.txt_pessoas_10 = QLineEdit(self.groupBox_27)
        self.txt_pessoas_10.setObjectName(u"txt_pessoas_10")
        self.txt_pessoas_10.setEnabled(False)
        self.txt_pessoas_10.setGeometry(QRect(12, 16, 411, 31))
        self.txt_pessoas_10.setMinimumSize(QSize(411, 0))
        self.txt_pessoas_10.setFont(font8)
        self.txt_pessoas_10.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_13.addWidget(self.groupBox_27)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab_2, "")
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 656, 551, 20))
        self.label_16.setFont(font10)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.btn_voltar_2 = QPushButton(self.page_4)
        self.btn_voltar_2.setObjectName(u"btn_voltar_2")
        self.btn_voltar_2.setEnabled(True)
        self.btn_voltar_2.setGeometry(QRect(870, 80, 30, 30))
        self.btn_voltar_2.setMinimumSize(QSize(30, 30))
        self.btn_voltar_2.setMaximumSize(QSize(30, 30))
        self.btn_voltar_2.setFont(font1)
        self.btn_voltar_2.setStyleSheet(u"QPushButton#btn_voltar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_2.setIcon(icon19)
        self.btn_voltar_2.setIconSize(QSize(24, 24))
        self.layoutWidget5 = QWidget(self.page_4)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(91, 175, 846, 63))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_12 = QGroupBox(self.layoutWidget5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(210, 61))
        self.groupBox_12.setMaximumSize(QSize(210, 61))
        self.groupBox_12.setAlignment(Qt.AlignCenter)
        self.btn_buscarInv = QPushButton(self.groupBox_12)
        self.btn_buscarInv.setObjectName(u"btn_buscarInv")
        self.btn_buscarInv.setGeometry(QRect(40, 20, 30, 30))
        self.btn_buscarInv.setMinimumSize(QSize(30, 30))
        font11 = QFont()
        font11.setFamilies([u"Reem Kufi"])
        font11.setPointSize(8)
        font11.setBold(True)
        self.btn_buscarInv.setFont(font11)
        self.btn_buscarInv.setStyleSheet(u"QPushButton#btn_buscarInv{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_buscarInv:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_buscarInv:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_buscarInv.setIcon(icon14)
        self.btn_buscarInv.setIconSize(QSize(24, 24))
        self.txt_paciente_4 = QLineEdit(self.groupBox_12)
        self.txt_paciente_4.setObjectName(u"txt_paciente_4")
        self.txt_paciente_4.setEnabled(True)
        self.txt_paciente_4.setGeometry(QRect(80, 20, 110, 31))
        self.txt_paciente_4.setMinimumSize(QSize(100, 21))
        self.txt_paciente_4.setFont(font1)
        self.txt_paciente_4.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_paciente_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.layoutWidget5)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 61))
        self.groupBox_13.setMaximumSize(QSize(16777215, 61))
        self.btn_conclusao_2 = QPushButton(self.groupBox_13)
        self.btn_conclusao_2.setObjectName(u"btn_conclusao_2")
        self.btn_conclusao_2.setEnabled(False)
        self.btn_conclusao_2.setGeometry(QRect(20, 17, 30, 30))
        self.btn_conclusao_2.setMinimumSize(QSize(30, 30))
        self.btn_conclusao_2.setMaximumSize(QSize(30, 30))
        self.btn_conclusao_2.setFont(font11)
        self.btn_conclusao_2.setStyleSheet(u"QPushButton#btn_conclusao_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_conclusao_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_conclusao_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_conclusao_2.setIcon(icon16)
        self.btn_conclusao_2.setIconSize(QSize(24, 24))
        self.btn_cancela_investiga_2 = QPushButton(self.groupBox_13)
        self.btn_cancela_investiga_2.setObjectName(u"btn_cancela_investiga_2")
        self.btn_cancela_investiga_2.setGeometry(QRect(78, 18, 30, 30))
        self.btn_cancela_investiga_2.setMinimumSize(QSize(30, 30))
        self.btn_cancela_investiga_2.setMaximumSize(QSize(30, 30))
        self.btn_cancela_investiga_2.setFont(font11)
        self.btn_cancela_investiga_2.setStyleSheet(u"QPushButton#btn_cancela_investiga_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_investiga_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_investiga_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_investiga_2.setIcon(icon17)
        self.btn_cancela_investiga_2.setIconSize(QSize(24, 24))
        self.btn_alterarInv_2 = QPushButton(self.groupBox_13)
        self.btn_alterarInv_2.setObjectName(u"btn_alterarInv_2")
        self.btn_alterarInv_2.setEnabled(False)
        self.btn_alterarInv_2.setGeometry(QRect(137, 18, 30, 30))
        self.btn_alterarInv_2.setMinimumSize(QSize(30, 30))
        self.btn_alterarInv_2.setMaximumSize(QSize(30, 30))
        self.btn_alterarInv_2.setFont(font11)
        self.btn_alterarInv_2.setStyleSheet(u"QPushButton#btn_alterarInv_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarInv_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarInv_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterarInv_2.setIcon(icon13)
        self.btn_alterarInv_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.groupBox_13)

        self.groupBox_14 = QGroupBox(self.layoutWidget5)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(0, 61))
        self.groupBox_14.setMaximumSize(QSize(16777215, 61))
        self.groupBox_14.setAlignment(Qt.AlignCenter)
        self.btn_resumo = QPushButton(self.groupBox_14)
        self.btn_resumo.setObjectName(u"btn_resumo")
        self.btn_resumo.setGeometry(QRect(40, 20, 30, 30))
        self.btn_resumo.setMinimumSize(QSize(30, 30))
        self.btn_resumo.setMaximumSize(QSize(30, 30))
        self.btn_resumo.setFont(font3)
        self.btn_resumo.setStyleSheet(u"QPushButton#btn_resumo{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumo:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumo:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_resumo.setIcon(icon18)
        self.btn_resumo.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.layoutWidget5)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(0, 61))
        self.groupBox_15.setMaximumSize(QSize(16777215, 61))
        self.groupBox_15.setAlignment(Qt.AlignCenter)
        self.btn_editarInv = QPushButton(self.groupBox_15)
        self.btn_editarInv.setObjectName(u"btn_editarInv")
        self.btn_editarInv.setGeometry(QRect(32, 18, 30, 30))
        self.btn_editarInv.setMinimumSize(QSize(30, 30))
        self.btn_editarInv.setMaximumSize(QSize(30, 30))
        self.btn_editarInv.setFont(font11)
        self.btn_editarInv.setStyleSheet(u"QPushButton#btn_editarInv{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_btn_editarInv:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editarInv:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/Imagem/editar-codigo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editarInv.setIcon(icon20)
        self.btn_editarInv.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.groupBox_15)

        self.groupBox_23 = QGroupBox(self.layoutWidget5)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(201, 61))
        self.groupBox_23.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.groupBox_23)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QRect(10, 30, 181, 22))
        self.comboBox.setFont(font1)

        self.horizontalLayout_5.addWidget(self.groupBox_23)

        self.stackedWidget.addWidget(self.page_4)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.btn_Spdf_2 = QPushButton(self.page_12)
        self.btn_Spdf_2.setObjectName(u"btn_Spdf_2")
        self.btn_Spdf_2.setEnabled(False)
        self.btn_Spdf_2.setGeometry(QRect(950, 620, 30, 30))
        self.btn_Spdf_2.setMinimumSize(QSize(30, 30))
        self.btn_Spdf_2.setMaximumSize(QSize(30, 30))
        self.btn_Spdf_2.setStyleSheet(u"QPushButton#btn_Spdf{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_Spdf:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_Spdf:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_Spdf_2.setIcon(icon15)
        self.btn_Spdf_2.setIconSize(QSize(24, 24))
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(350, 660, 331, 20))
        self.label_18.setFont(font10)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.layoutWidget6 = QWidget(self.page_12)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 60, 993, 550))
        self.verticalLayout_25 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.groupBox_61 = QGroupBox(self.layoutWidget6)
        self.groupBox_61.setObjectName(u"groupBox_61")
        self.groupBox_61.setMinimumSize(QSize(991, 121))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.groupBox_61.setFont(font12)
        self.groupBox_61.setAlignment(Qt.AlignCenter)
        self.btn_voltar_3 = QPushButton(self.groupBox_61)
        self.btn_voltar_3.setObjectName(u"btn_voltar_3")
        self.btn_voltar_3.setEnabled(True)
        self.btn_voltar_3.setGeometry(QRect(930, 50, 30, 30))
        self.btn_voltar_3.setMinimumSize(QSize(30, 30))
        self.btn_voltar_3.setMaximumSize(QSize(30, 30))
        self.btn_voltar_3.setFont(font1)
        self.btn_voltar_3.setStyleSheet(u"QPushButton#btn_voltar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_3.setIcon(icon19)
        self.btn_voltar_3.setIconSize(QSize(24, 24))
        self.layoutWidget7 = QWidget(self.groupBox_61)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(84, 20, 822, 93))
        self.horizontalLayout_28 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_136 = QLabel(self.layoutWidget7)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font1)
        self.label_136.setStyleSheet(u"color:rgb(0,0,0);")

        self.horizontalLayout_19.addWidget(self.label_136)

        self.lineEdit_6 = QLineEdit(self.layoutWidget7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(441, 0))
        self.lineEdit_6.setFont(font1)
        self.lineEdit_6.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_19.addWidget(self.lineEdit_6)

        self.btn_consultarNoti_2 = QPushButton(self.layoutWidget7)
        self.btn_consultarNoti_2.setObjectName(u"btn_consultarNoti_2")
        self.btn_consultarNoti_2.setMinimumSize(QSize(30, 30))
        self.btn_consultarNoti_2.setMaximumSize(QSize(30, 30))
        self.btn_consultarNoti_2.setFont(font1)
        self.btn_consultarNoti_2.setStyleSheet(u"QPushButton#btn_consultarNoti_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultarNoti_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultarNoti_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultarNoti_2.setIcon(icon14)
        self.btn_consultarNoti_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.btn_consultarNoti_2)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_19)

        self.groupBox_37 = QGroupBox(self.layoutWidget7)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setMinimumSize(QSize(281, 91))
        self.groupBox_37.setAlignment(Qt.AlignCenter)
        self.layoutWidget_4 = QWidget(self.groupBox_37)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 20, 108, 62))
        self.verticalLayout_35 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.radioButton_10 = QRadioButton(self.layoutWidget_4)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setEnabled(True)
        self.radioButton_10.setFont(font1)

        self.verticalLayout_35.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.layoutWidget_4)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setEnabled(True)
        self.radioButton_11.setFont(font1)

        self.verticalLayout_35.addWidget(self.radioButton_11)

        self.layoutWidget_42 = QWidget(self.groupBox_37)
        self.layoutWidget_42.setObjectName(u"layoutWidget_42")
        self.layoutWidget_42.setGeometry(QRect(140, 20, 113, 62))
        self.verticalLayout_36 = QVBoxLayout(self.layoutWidget_42)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.radioButton_12 = QRadioButton(self.layoutWidget_42)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setEnabled(True)
        self.radioButton_12.setFont(font1)

        self.verticalLayout_36.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.layoutWidget_42)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setEnabled(True)
        self.radioButton_13.setFont(font1)

        self.verticalLayout_36.addWidget(self.radioButton_13)


        self.horizontalLayout_28.addWidget(self.groupBox_37)


        self.verticalLayout_25.addWidget(self.groupBox_61)

        self.tb_consulta_4 = QTableWidget(self.layoutWidget6)
        if (self.tb_consulta_4.columnCount() < 8):
            self.tb_consulta_4.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tb_consulta_4.setObjectName(u"tb_consulta_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_consulta_4.sizePolicy().hasHeightForWidth())
        self.tb_consulta_4.setSizePolicy(sizePolicy)
        self.tb_consulta_4.setMinimumSize(QSize(991, 421))
        font13 = QFont()
        font13.setFamilies([u"Reem Kufi"])
        font13.setBold(True)
        self.tb_consulta_4.setFont(font13)
        self.tb_consulta_4.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"\n"
"\n"
"\n"
"")
        self.tb_consulta_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_consulta_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tb_consulta_4.setAutoScrollMargin(21)
        self.tb_consulta_4.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tb_consulta_4.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tb_consulta_4.setGridStyle(Qt.NoPen)
        self.tb_consulta_4.horizontalHeader().setVisible(True)
        self.tb_consulta_4.horizontalHeader().setDefaultSectionSize(125)

        self.verticalLayout_25.addWidget(self.tb_consulta_4)

        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.groupBox_38 = QGroupBox(self.page_13)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setGeometry(QRect(90, 0, 821, 681))
        self.groupBox_38.setMinimumSize(QSize(821, 681))
        self.groupBox_38.setAlignment(Qt.AlignCenter)
        self.btn_voltar_4 = QPushButton(self.groupBox_38)
        self.btn_voltar_4.setObjectName(u"btn_voltar_4")
        self.btn_voltar_4.setEnabled(True)
        self.btn_voltar_4.setGeometry(QRect(770, 50, 30, 30))
        self.btn_voltar_4.setMinimumSize(QSize(30, 30))
        self.btn_voltar_4.setMaximumSize(QSize(30, 30))
        self.btn_voltar_4.setFont(font1)
        self.btn_voltar_4.setStyleSheet(u"QPushButton#btn_voltar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_4.setIcon(icon19)
        self.btn_voltar_4.setIconSize(QSize(24, 24))
        self.layoutWidget8 = QWidget(self.groupBox_38)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(201, 93, 445, 569))
        self.verticalLayout_39 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.groupBox_39 = QGroupBox(self.layoutWidget8)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setMinimumSize(QSize(441, 80))
        self.txt_cadnome_4 = QLineEdit(self.groupBox_39)
        self.txt_cadnome_4.setObjectName(u"txt_cadnome_4")
        self.txt_cadnome_4.setEnabled(False)
        self.txt_cadnome_4.setGeometry(QRect(10, 30, 421, 31))
        self.txt_cadnome_4.setMinimumSize(QSize(421, 0))
        self.txt_cadnome_4.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")

        self.verticalLayout_38.addWidget(self.groupBox_39)

        self.groupBox_40 = QGroupBox(self.layoutWidget8)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setMinimumSize(QSize(441, 80))
        self.txt_cadnome_5 = QLineEdit(self.groupBox_40)
        self.txt_cadnome_5.setObjectName(u"txt_cadnome_5")
        self.txt_cadnome_5.setEnabled(False)
        self.txt_cadnome_5.setGeometry(QRect(10, 30, 421, 31))
        self.txt_cadnome_5.setMinimumSize(QSize(421, 0))
        self.txt_cadnome_5.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")

        self.verticalLayout_38.addWidget(self.groupBox_40)

        self.groupBox_42 = QGroupBox(self.layoutWidget8)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setMinimumSize(QSize(441, 80))
        self.txt_cadnome_6 = QLineEdit(self.groupBox_42)
        self.txt_cadnome_6.setObjectName(u"txt_cadnome_6")
        self.txt_cadnome_6.setEnabled(False)
        self.txt_cadnome_6.setGeometry(QRect(10, 30, 421, 31))
        self.txt_cadnome_6.setMinimumSize(QSize(421, 0))
        self.txt_cadnome_6.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")
        self.txt_cadnome_6.setEchoMode(QLineEdit.Password)

        self.verticalLayout_38.addWidget(self.groupBox_42)

        self.groupBox_41 = QGroupBox(self.layoutWidget8)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setMinimumSize(QSize(441, 80))
        self.cb_outros_4 = QComboBox(self.groupBox_41)
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.setObjectName(u"cb_outros_4")
        self.cb_outros_4.setEnabled(True)
        self.cb_outros_4.setGeometry(QRect(80, 40, 300, 29))
        self.cb_outros_4.setMinimumSize(QSize(300, 0))
        self.cb_outros_4.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_38.addWidget(self.groupBox_41)


        self.verticalLayout_39.addLayout(self.verticalLayout_38)

        self.groupBox_43 = QGroupBox(self.layoutWidget8)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setMinimumSize(QSize(0, 221))
        self.groupBox_43.setAlignment(Qt.AlignCenter)
        self.groupBox_44 = QGroupBox(self.groupBox_43)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setGeometry(QRect(10, 20, 420, 80))
        self.groupBox_44.setMinimumSize(QSize(420, 80))
        self.groupBox_44.setMaximumSize(QSize(420, 16777215))
        self.layoutWidget9 = QWidget(self.groupBox_44)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(20, 30, 389, 32))
        self.horizontalLayout_59 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.txt_consultaUser_2 = QLineEdit(self.layoutWidget9)
        self.txt_consultaUser_2.setObjectName(u"txt_consultaUser_2")
        self.txt_consultaUser_2.setMinimumSize(QSize(351, 22))
        self.txt_consultaUser_2.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")

        self.horizontalLayout_59.addWidget(self.txt_consultaUser_2)

        self.btn_consultaUser_2 = QPushButton(self.layoutWidget9)
        self.btn_consultaUser_2.setObjectName(u"btn_consultaUser_2")
        self.btn_consultaUser_2.setMinimumSize(QSize(30, 30))
        self.btn_consultaUser_2.setMaximumSize(QSize(30, 30))
        self.btn_consultaUser_2.setStyleSheet(u"QPushButton#btn_consultaUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultaUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultaUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultaUser_2.setIcon(icon14)
        self.btn_consultaUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_59.addWidget(self.btn_consultaUser_2)

        self.tableWidget_2 = QTableWidget(self.groupBox_43)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(1, 110, 441, 101))
        self.tableWidget_2.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"\n"
"padding-bottom: 7px")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(146)

        self.verticalLayout_39.addWidget(self.groupBox_43)

        self.layoutWidget10 = QWidget(self.groupBox_38)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(521, 25, 124, 63))
        self.horizontalLayout_60 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.groupBox_48 = QGroupBox(self.layoutWidget10)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.groupBox_48.setMinimumSize(QSize(51, 61))
        self.groupBox_48.setMaximumSize(QSize(16777215, 61))
        self.groupBox_48.setAlignment(Qt.AlignCenter)
        self.btn_salvaUser_2 = QPushButton(self.groupBox_48)
        self.btn_salvaUser_2.setObjectName(u"btn_salvaUser_2")
        self.btn_salvaUser_2.setEnabled(False)
        self.btn_salvaUser_2.setGeometry(QRect(10, 20, 30, 30))
        self.btn_salvaUser_2.setMinimumSize(QSize(30, 30))
        self.btn_salvaUser_2.setMaximumSize(QSize(30, 30))
        font14 = QFont()
        font14.setPointSize(8)
        font14.setBold(True)
        self.btn_salvaUser_2.setFont(font14)
        self.btn_salvaUser_2.setStyleSheet(u"QPushButton#btn_salvaUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salvaUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salvaUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salvaUser_2.setIcon(icon16)
        self.btn_salvaUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.groupBox_48)

        self.groupBox_49 = QGroupBox(self.layoutWidget10)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.groupBox_49.setMinimumSize(QSize(51, 61))
        self.groupBox_49.setMaximumSize(QSize(16777215, 61))
        self.groupBox_49.setAlignment(Qt.AlignCenter)
        self.btn_cancelaUser_2 = QPushButton(self.groupBox_49)
        self.btn_cancelaUser_2.setObjectName(u"btn_cancelaUser_2")
        self.btn_cancelaUser_2.setEnabled(False)
        self.btn_cancelaUser_2.setGeometry(QRect(17, 20, 30, 30))
        self.btn_cancelaUser_2.setMinimumSize(QSize(30, 30))
        self.btn_cancelaUser_2.setMaximumSize(QSize(30, 30))
        self.btn_cancelaUser_2.setFont(font14)
        self.btn_cancelaUser_2.setStyleSheet(u"QPushButton#btn_cancelaUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancelaUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancelaUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancelaUser_2.setIcon(icon17)
        self.btn_cancelaUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.groupBox_49)

        self.layoutWidget11 = QWidget(self.groupBox_38)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(202, 26, 170, 63))
        self.horizontalLayout_61 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.groupBox_45 = QGroupBox(self.layoutWidget11)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setMinimumSize(QSize(51, 61))
        self.groupBox_45.setMaximumSize(QSize(16777215, 61))
        self.groupBox_45.setAlignment(Qt.AlignCenter)
        self.btn_novoUser_2 = QPushButton(self.groupBox_45)
        self.btn_novoUser_2.setObjectName(u"btn_novoUser_2")
        self.btn_novoUser_2.setGeometry(QRect(10, 20, 30, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.btn_novoUser_2.sizePolicy().hasHeightForWidth())
        self.btn_novoUser_2.setSizePolicy(sizePolicy1)
        self.btn_novoUser_2.setMinimumSize(QSize(30, 30))
        self.btn_novoUser_2.setFont(font14)
        self.btn_novoUser_2.setStyleSheet(u"QPushButton#btn_novoUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novoUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novoUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/Imagem/adicionar-usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_novoUser_2.setIcon(icon21)
        self.btn_novoUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_61.addWidget(self.groupBox_45)

        self.groupBox_46 = QGroupBox(self.layoutWidget11)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.groupBox_46.setMinimumSize(QSize(51, 61))
        self.groupBox_46.setMaximumSize(QSize(16777215, 61))
        self.groupBox_46.setAlignment(Qt.AlignCenter)
        self.btn_editaUser_2 = QPushButton(self.groupBox_46)
        self.btn_editaUser_2.setObjectName(u"btn_editaUser_2")
        self.btn_editaUser_2.setEnabled(False)
        self.btn_editaUser_2.setGeometry(QRect(10, 20, 30, 30))
        self.btn_editaUser_2.setMinimumSize(QSize(30, 30))
        self.btn_editaUser_2.setMaximumSize(QSize(30, 30))
        self.btn_editaUser_2.setFont(font14)
        self.btn_editaUser_2.setStyleSheet(u"QPushButton#btn_editaUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editaUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editaUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/Imagem/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editaUser_2.setIcon(icon22)
        self.btn_editaUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_61.addWidget(self.groupBox_46)

        self.groupBox_47 = QGroupBox(self.layoutWidget11)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.groupBox_47.setMinimumSize(QSize(51, 61))
        self.groupBox_47.setMaximumSize(QSize(16777215, 61))
        self.groupBox_47.setAlignment(Qt.AlignCenter)
        self.btn_alterarUser_2 = QPushButton(self.groupBox_47)
        self.btn_alterarUser_2.setObjectName(u"btn_alterarUser_2")
        self.btn_alterarUser_2.setEnabled(False)
        self.btn_alterarUser_2.setGeometry(QRect(10, 20, 30, 30))
        self.btn_alterarUser_2.setMinimumSize(QSize(30, 30))
        self.btn_alterarUser_2.setMaximumSize(QSize(30, 30))
        self.btn_alterarUser_2.setFont(font14)
        self.btn_alterarUser_2.setStyleSheet(u"QPushButton#btn_alterarUser_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarUser_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarUser_2:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterarUser_2.setIcon(icon13)
        self.btn_alterarUser_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_61.addWidget(self.groupBox_47)

        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.groupBox_50 = QGroupBox(self.page_14)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.groupBox_50.setGeometry(QRect(241, 138, 511, 321))
        self.groupBox_50.setMinimumSize(QSize(511, 241))
        self.groupBox_50.setAlignment(Qt.AlignCenter)
        self.layoutWidget12 = QWidget(self.groupBox_50)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(60, 100, 397, 201))
        self.verticalLayout_40 = QVBoxLayout(self.layoutWidget12)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_19 = QLabel(self.layoutWidget12)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_62.addWidget(self.label_19)

        self.lineEdit_7 = QLineEdit(self.layoutWidget12)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(351, 0))

        self.horizontalLayout_62.addWidget(self.lineEdit_7)


        self.verticalLayout_40.addLayout(self.horizontalLayout_62)

        self.tableWidget_3 = QTableWidget(self.layoutWidget12)
        if (self.tableWidget_3.columnCount() < 1):
            self.tableWidget_3.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(391, 151))
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(391)

        self.verticalLayout_40.addWidget(self.tableWidget_3)

        self.layoutWidget13 = QWidget(self.groupBox_50)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(50, 20, 167, 63))
        self.horizontalLayout_63 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.groupBox_51 = QGroupBox(self.layoutWidget13)
        self.groupBox_51.setObjectName(u"groupBox_51")
        self.groupBox_51.setMinimumSize(QSize(51, 61))
        self.groupBox_51.setMaximumSize(QSize(51, 61))
        self.groupBox_51.setAlignment(Qt.AlignCenter)
        self.btn_novo_setor = QPushButton(self.groupBox_51)
        self.btn_novo_setor.setObjectName(u"btn_novo_setor")
        self.btn_novo_setor.setGeometry(QRect(10, 20, 30, 30))
        self.btn_novo_setor.setMinimumSize(QSize(30, 30))
        self.btn_novo_setor.setMaximumSize(QSize(30, 30))
        self.btn_novo_setor.setStyleSheet(u"QPushButton#btn_novo_setor{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novo_setor:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novo_setor:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/Imagem/grafico-de-setores (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_novo_setor.setIcon(icon23)
        self.btn_novo_setor.setIconSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.groupBox_51)

        self.groupBox_52 = QGroupBox(self.layoutWidget13)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setMinimumSize(QSize(51, 61))
        self.groupBox_52.setMaximumSize(QSize(51, 61))
        self.groupBox_52.setAlignment(Qt.AlignCenter)
        self.btn_edita_setor = QPushButton(self.groupBox_52)
        self.btn_edita_setor.setObjectName(u"btn_edita_setor")
        self.btn_edita_setor.setGeometry(QRect(10, 20, 30, 30))
        self.btn_edita_setor.setMinimumSize(QSize(30, 30))
        self.btn_edita_setor.setMaximumSize(QSize(30, 30))
        self.btn_edita_setor.setStyleSheet(u"QPushButton#btn_edita_setor{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_edita_setor:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_edita_setor:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_edita_setor.setIcon(icon20)
        self.btn_edita_setor.setIconSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.groupBox_52)

        self.groupBox_55 = QGroupBox(self.layoutWidget13)
        self.groupBox_55.setObjectName(u"groupBox_55")
        self.groupBox_55.setMinimumSize(QSize(51, 61))
        self.groupBox_55.setMaximumSize(QSize(51, 61))
        self.groupBox_55.setAlignment(Qt.AlignCenter)
        self.btn_conf_alterar = QPushButton(self.groupBox_55)
        self.btn_conf_alterar.setObjectName(u"btn_conf_alterar")
        self.btn_conf_alterar.setGeometry(QRect(10, 20, 30, 30))
        self.btn_conf_alterar.setMinimumSize(QSize(30, 30))
        self.btn_conf_alterar.setMaximumSize(QSize(30, 30))
        self.btn_conf_alterar.setStyleSheet(u"QPushButton#btn_conf_alterar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_conf_alterar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_conf_alterar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_conf_alterar.setIcon(icon13)
        self.btn_conf_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.groupBox_55)

        self.layoutWidget14 = QWidget(self.groupBox_50)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(370, 20, 110, 63))
        self.horizontalLayout_64 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.groupBox_53 = QGroupBox(self.layoutWidget14)
        self.groupBox_53.setObjectName(u"groupBox_53")
        self.groupBox_53.setMinimumSize(QSize(51, 61))
        self.groupBox_53.setMaximumSize(QSize(51, 61))
        self.groupBox_53.setAlignment(Qt.AlignCenter)
        self.btn_salvar_setor = QPushButton(self.groupBox_53)
        self.btn_salvar_setor.setObjectName(u"btn_salvar_setor")
        self.btn_salvar_setor.setGeometry(QRect(10, 20, 30, 30))
        self.btn_salvar_setor.setMinimumSize(QSize(30, 30))
        self.btn_salvar_setor.setMaximumSize(QSize(30, 30))
        self.btn_salvar_setor.setStyleSheet(u"QPushButton#btn_salvar_setor{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salvar_setor:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salvar_setor:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salvar_setor.setIcon(icon16)
        self.btn_salvar_setor.setIconSize(QSize(24, 24))

        self.horizontalLayout_64.addWidget(self.groupBox_53)

        self.groupBox_54 = QGroupBox(self.layoutWidget14)
        self.groupBox_54.setObjectName(u"groupBox_54")
        self.groupBox_54.setMinimumSize(QSize(51, 61))
        self.groupBox_54.setMaximumSize(QSize(51, 61))
        self.groupBox_54.setAlignment(Qt.AlignCenter)
        self.btn_cancela_setor = QPushButton(self.groupBox_54)
        self.btn_cancela_setor.setObjectName(u"btn_cancela_setor")
        self.btn_cancela_setor.setGeometry(QRect(10, 20, 30, 30))
        self.btn_cancela_setor.setMinimumSize(QSize(30, 30))
        self.btn_cancela_setor.setMaximumSize(QSize(30, 30))
        self.btn_cancela_setor.setStyleSheet(u"QPushButton#btn_cancela_setor{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_setor:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_setor:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_setor.setIcon(icon17)
        self.btn_cancela_setor.setIconSize(QSize(24, 24))

        self.horizontalLayout_64.addWidget(self.groupBox_54)

        self.label_20 = QLabel(self.page_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(450, 40, 91, 81))
        self.label_20.setMinimumSize(QSize(91, 81))
        self.label_20.setStyleSheet(u"image: url(:/Imagem/composto.png);")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_21 = QLabel(self.page_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(330, 660, 331, 20))
        self.label_21.setFont(font10)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.btn_voltar_5 = QPushButton(self.page_14)
        self.btn_voltar_5.setObjectName(u"btn_voltar_5")
        self.btn_voltar_5.setEnabled(True)
        self.btn_voltar_5.setGeometry(QRect(720, 100, 30, 30))
        self.btn_voltar_5.setMinimumSize(QSize(30, 30))
        self.btn_voltar_5.setMaximumSize(QSize(30, 30))
        self.btn_voltar_5.setFont(font1)
        self.btn_voltar_5.setStyleSheet(u"QPushButton#btn_voltar_5{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar_5:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar_5:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_5.setIcon(icon19)
        self.btn_voltar_5.setIconSize(QSize(24, 24))
        self.stackedWidget.addWidget(self.page_14)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.groupBox_56 = QGroupBox(self.page_5)
        self.groupBox_56.setObjectName(u"groupBox_56")
        self.groupBox_56.setGeometry(QRect(171, 138, 651, 421))
        self.groupBox_56.setAlignment(Qt.AlignCenter)
        self.layoutWidget15 = QWidget(self.groupBox_56)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(60, 40, 124, 63))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.groupBox_58 = QGroupBox(self.layoutWidget15)
        self.groupBox_58.setObjectName(u"groupBox_58")
        self.groupBox_58.setMinimumSize(QSize(58, 61))
        self.groupBox_58.setAlignment(Qt.AlignCenter)
        self.btn_novoEmail = QPushButton(self.groupBox_58)
        self.btn_novoEmail.setObjectName(u"btn_novoEmail")
        self.btn_novoEmail.setGeometry(QRect(13, 26, 30, 30))
        self.btn_novoEmail.setMinimumSize(QSize(30, 30))
        self.btn_novoEmail.setMaximumSize(QSize(30, 30))
        self.btn_novoEmail.setStyleSheet(u"QPushButton#btn_novoEmail{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novoEmail:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novoEmail:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/Imagem/nova-mensagem (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_novoEmail.setIcon(icon24)
        self.btn_novoEmail.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.groupBox_58)

        self.groupBox_59 = QGroupBox(self.layoutWidget15)
        self.groupBox_59.setObjectName(u"groupBox_59")
        self.groupBox_59.setMinimumSize(QSize(58, 61))
        self.groupBox_59.setAlignment(Qt.AlignCenter)
        self.btn_alterar_email = QPushButton(self.groupBox_59)
        self.btn_alterar_email.setObjectName(u"btn_alterar_email")
        self.btn_alterar_email.setGeometry(QRect(10, 24, 30, 30))
        self.btn_alterar_email.setMinimumSize(QSize(30, 30))
        self.btn_alterar_email.setMaximumSize(QSize(30, 30))
        self.btn_alterar_email.setStyleSheet(u"QPushButton#btn_alterar_email{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterar_email:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterar_email:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/Imagem/papel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_email.setIcon(icon25)
        self.btn_alterar_email.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.groupBox_59)

        self.groupBox_60 = QGroupBox(self.groupBox_56)
        self.groupBox_60.setObjectName(u"groupBox_60")
        self.groupBox_60.setGeometry(QRect(534, 37, 58, 71))
        self.groupBox_60.setMinimumSize(QSize(58, 61))
        self.groupBox_60.setAlignment(Qt.AlignCenter)
        self.btn_pesquisa_email = QPushButton(self.groupBox_60)
        self.btn_pesquisa_email.setObjectName(u"btn_pesquisa_email")
        self.btn_pesquisa_email.setGeometry(QRect(11, 25, 30, 30))
        self.btn_pesquisa_email.setMinimumSize(QSize(30, 30))
        self.btn_pesquisa_email.setMaximumSize(QSize(30, 30))
        self.btn_pesquisa_email.setStyleSheet(u"QPushButton#btn_pesquisa_email{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisa_email:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisa_email:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisa_email.setIcon(icon14)
        self.btn_pesquisa_email.setIconSize(QSize(24, 24))
        self.layoutWidget16 = QWidget(self.groupBox_56)
        self.layoutWidget16.setObjectName(u"layoutWidget16")
        self.layoutWidget16.setGeometry(QRect(60, 110, 533, 263))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.layoutWidget16)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.layoutWidget16)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(431, 22))

        self.horizontalLayout_10.addWidget(self.lineEdit_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.groupBox_57 = QGroupBox(self.layoutWidget16)
        self.groupBox_57.setObjectName(u"groupBox_57")
        self.groupBox_57.setMinimumSize(QSize(531, 231))
        self.tableWidget = QTableWidget(self.groupBox_57)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 50, 481, 161))
        self.tableWidget.setMinimumSize(QSize(481, 61))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(477)

        self.verticalLayout_15.addWidget(self.groupBox_57)

        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(418, 28, 141, 101))
        self.label_11.setStyleSheet(u"image: url(:/Imagem/marketing-de-email.png);")
        self.btn_voltar_6 = QPushButton(self.page_5)
        self.btn_voltar_6.setObjectName(u"btn_voltar_6")
        self.btn_voltar_6.setEnabled(True)
        self.btn_voltar_6.setGeometry(QRect(788, 98, 30, 30))
        self.btn_voltar_6.setMinimumSize(QSize(30, 30))
        self.btn_voltar_6.setMaximumSize(QSize(30, 30))
        self.btn_voltar_6.setFont(font1)
        self.btn_voltar_6.setStyleSheet(u"QPushButton#btn_voltar_6{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar_6:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar_6:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_6.setIcon(icon19)
        self.btn_voltar_6.setIconSize(QSize(24, 24))
        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 660, 331, 20))
        self.label_22.setFont(font10)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_5)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.frame_3 = QFrame(self.page_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(239, 80, 281, 511))
        self.frame_3.setFont(font1)
        self.frame_3.setStyleSheet(u"border-top-left-radius:50px;\n"
"image: url(:/Imagens/Fundo_login.jpg);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(13, 110, 261, 351))
        self.label_12.setStyleSheet(u"image: url(:/Imagens/Dia-da-Qualidadecorte (1).png);")
        self.layoutWidget_2 = QWidget(self.frame_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(51, 28, 179, 70))
        self.verticalLayout_26 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        font15 = QFont()
        font15.setFamilies([u"Reem Kufi"])
        font15.setPointSize(12)
        font15.setBold(False)
        self.label_13.setFont(font15)
        self.label_13.setStyleSheet(u"color: rgb(108, 52, 19);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_13)

        self.label_23 = QLabel(self.layoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font15)
        self.label_23.setStyleSheet(u"color: rgb(108, 52, 19);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_23)

        self.frame_4 = QFrame(self.page_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(520, 80, 281, 531))
        self.frame_4.setStyleSheet(u"border-bottom-right-radius:50px;\n"
"background-color: rgb(244, 244, 244);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_9 = QWidget(self.frame_4)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(40, 176, 204, 105))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.txt_usuario = QLineEdit(self.layoutWidget_9)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(200, 30))
        self.txt_usuario.setFont(font1)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.txt_usuario)

        self.txt_senha = QLineEdit(self.layoutWidget_9)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(200, 30))
        self.txt_senha.setFont(font1)
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.txt_senha)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)

        self.cb_empresa = QComboBox(self.layoutWidget_9)
        self.cb_empresa.addItem("")
        self.cb_empresa.addItem("")
        self.cb_empresa.setObjectName(u"cb_empresa")
        self.cb_empresa.setMinimumSize(QSize(200, 20))
        self.cb_empresa.setFont(font1)
        self.cb_empresa.setLayoutDirection(Qt.LeftToRight)
        self.cb_empresa.setStyleSheet(u"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_empresa.setInsertPolicy(QComboBox.NoInsert)
        self.cb_empresa.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_27.addWidget(self.cb_empresa)

        self.btn_anonimo = QPushButton(self.frame_4)
        self.btn_anonimo.setObjectName(u"btn_anonimo")
        self.btn_anonimo.setGeometry(QRect(100, 390, 100, 30))
        self.btn_anonimo.setMinimumSize(QSize(100, 30))
        self.btn_anonimo.setFont(font1)
        self.btn_anonimo.setStyleSheet(u"QPushButton#btn_anonimo{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_anonimo:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_anonimo:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.layoutWidget_10 = QWidget(self.frame_4)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(90, 295, 102, 68))
        self.verticalLayout_29 = QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_login_rnc = QPushButton(self.layoutWidget_10)
        self.btn_login_rnc.setObjectName(u"btn_login_rnc")
        self.btn_login_rnc.setEnabled(False)
        self.btn_login_rnc.setMinimumSize(QSize(100, 30))
        self.btn_login_rnc.setFont(font1)
        self.btn_login_rnc.setStyleSheet(u"QPushButton#btn_login_rnc{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login_rnc:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login_rnc:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.btn_login_rnc)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 5, 141, 151))
        self.label_14.setStyleSheet(u"image: url(:/Imagens/password.png);")
        self.btn_SairApp = QPushButton(self.frame_4)
        self.btn_SairApp.setObjectName(u"btn_SairApp")
        self.btn_SairApp.setEnabled(False)
        self.btn_SairApp.setGeometry(QRect(100, 480, 100, 30))
        self.btn_SairApp.setMinimumSize(QSize(100, 30))
        self.btn_SairApp.setFont(font1)
        self.btn_SairApp.setStyleSheet(u"QPushButton#btn_SairApp{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_SairApp:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_SairApp:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.groupBox_128 = QGroupBox(self.page_8)
        self.groupBox_128.setObjectName(u"groupBox_128")
        self.groupBox_128.setGeometry(QRect(150, 179, 81, 51))
        self.groupBox_128.setMinimumSize(QSize(81, 51))
        self.groupBox_128.setMaximumSize(QSize(81, 51))
        self.groupBox_128.setAlignment(Qt.AlignCenter)
        self.btn_logoff_3 = QPushButton(self.groupBox_128)
        self.btn_logoff_3.setObjectName(u"btn_logoff_3")
        self.btn_logoff_3.setGeometry(QRect(6, 16, 60, 30))
        self.btn_logoff_3.setMinimumSize(QSize(60, 30))
        self.btn_logoff_3.setMaximumSize(QSize(60, 30))
        self.btn_logoff_3.setFont(font3)
        self.btn_logoff_3.setStyleSheet(u"QPushButton#btn_logoff{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_logoff:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_logoff:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_logoff_3.setIcon(icon10)
        self.btn_logoff_3.setIconSize(QSize(24, 24))
        self.widget1 = QWidget(self.page_8)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(150, 180, 708, 53))
        self.horizontalLayout_130 = QHBoxLayout(self.widget1)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.groupBox_129 = QGroupBox(self.widget1)
        self.groupBox_129.setObjectName(u"groupBox_129")
        self.groupBox_129.setMinimumSize(QSize(81, 51))
        self.groupBox_129.setMaximumSize(QSize(81, 51))
        self.groupBox_129.setAlignment(Qt.AlignCenter)
        self.btn_dashboard_2 = QPushButton(self.groupBox_129)
        self.btn_dashboard_2.setObjectName(u"btn_dashboard_2")
        self.btn_dashboard_2.setEnabled(False)
        self.btn_dashboard_2.setGeometry(QRect(23, 17, 30, 30))
        self.btn_dashboard_2.setMinimumSize(QSize(30, 30))
        self.btn_dashboard_2.setMaximumSize(QSize(30, 30))
        self.btn_dashboard_2.setFont(font2)
        self.btn_dashboard_2.setStyleSheet(u"QPushButton#btn_dashboard{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_dashboard:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_dashboard:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/Imagens/dashboard (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard_2.setIcon(icon26)
        self.btn_dashboard_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.groupBox_129)

        self.groupBox_123 = QGroupBox(self.widget1)
        self.groupBox_123.setObjectName(u"groupBox_123")
        self.groupBox_123.setMinimumSize(QSize(271, 51))
        self.groupBox_123.setMaximumSize(QSize(271, 51))
        self.groupBox_123.setAlignment(Qt.AlignCenter)
        self.btn_rnc_2 = QPushButton(self.groupBox_123)
        self.btn_rnc_2.setObjectName(u"btn_rnc_2")
        self.btn_rnc_2.setEnabled(False)
        self.btn_rnc_2.setGeometry(QRect(26, 15, 30, 30))
        self.btn_rnc_2.setMinimumSize(QSize(30, 30))
        self.btn_rnc_2.setMaximumSize(QSize(30, 30))
        self.btn_rnc_2.setFont(font3)
        self.btn_rnc_2.setStyleSheet(u"QPushButton#btn_rnc{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_rnc:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_rnc:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/Imagens/registro-online.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rnc_2.setIcon(icon27)
        self.btn_rnc_2.setIconSize(QSize(24, 24))
        self.btn_usuarios_2 = QPushButton(self.groupBox_123)
        self.btn_usuarios_2.setObjectName(u"btn_usuarios_2")
        self.btn_usuarios_2.setEnabled(False)
        self.btn_usuarios_2.setGeometry(QRect(76, 15, 30, 30))
        self.btn_usuarios_2.setMinimumSize(QSize(30, 30))
        self.btn_usuarios_2.setMaximumSize(QSize(30, 30))
        self.btn_usuarios_2.setFont(font3)
        self.btn_usuarios_2.setStyleSheet(u"QPushButton#btn_usuarios{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_usuarios:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_usuarios:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/Imagens/password.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_usuarios_2.setIcon(icon28)
        self.btn_usuarios_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.groupBox_123)

        self.groupBox_124 = QGroupBox(self.widget1)
        self.groupBox_124.setObjectName(u"groupBox_124")
        self.groupBox_124.setMinimumSize(QSize(81, 51))
        self.groupBox_124.setMaximumSize(QSize(81, 51))
        self.groupBox_124.setAlignment(Qt.AlignCenter)
        self.btn_tratativa = QPushButton(self.groupBox_124)
        self.btn_tratativa.setObjectName(u"btn_tratativa")
        self.btn_tratativa.setEnabled(False)
        self.btn_tratativa.setGeometry(QRect(24, 16, 30, 30))
        self.btn_tratativa.setMinimumSize(QSize(30, 30))
        self.btn_tratativa.setMaximumSize(QSize(30, 30))
        self.btn_tratativa.setFont(font3)
        self.btn_tratativa.setStyleSheet(u"QPushButton#btn_tratativa{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_tratativa:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_tratativa:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/Imagens/investigacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tratativa.setIcon(icon29)
        self.btn_tratativa.setIconSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.groupBox_124)

        self.groupBox_127 = QGroupBox(self.widget1)
        self.groupBox_127.setObjectName(u"groupBox_127")
        self.groupBox_127.setMinimumSize(QSize(81, 51))
        self.groupBox_127.setMaximumSize(QSize(81, 51))
        self.groupBox_127.setAlignment(Qt.AlignCenter)
        self.btn_consultar_2 = QPushButton(self.groupBox_127)
        self.btn_consultar_2.setObjectName(u"btn_consultar_2")
        self.btn_consultar_2.setEnabled(False)
        self.btn_consultar_2.setGeometry(QRect(26, 16, 30, 30))
        self.btn_consultar_2.setMinimumSize(QSize(30, 30))
        self.btn_consultar_2.setMaximumSize(QSize(30, 30))
        self.btn_consultar_2.setFont(font3)
        self.btn_consultar_2.setStyleSheet(u"QPushButton#btn_consultar{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultar:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultar:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/Imagens/pesquisa-de-dados (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consultar_2.setIcon(icon30)
        self.btn_consultar_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_130.addWidget(self.groupBox_127)

        self.groupBox_125 = QGroupBox(self.widget1)
        self.groupBox_125.setObjectName(u"groupBox_125")
        self.groupBox_125.setMinimumSize(QSize(81, 51))
        self.groupBox_125.setMaximumSize(QSize(81, 51))
        self.groupBox_125.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.groupBox_125)

        self.groupBox_126 = QGroupBox(self.widget1)
        self.groupBox_126.setObjectName(u"groupBox_126")
        self.groupBox_126.setMinimumSize(QSize(81, 51))
        self.groupBox_126.setMaximumSize(QSize(81, 51))
        self.groupBox_126.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.groupBox_126)

        self.stackedWidget.addWidget(self.page_8)
        self.layoutWidget17 = QWidget(self.centralwidget)
        self.layoutWidget17.setObjectName(u"layoutWidget17")
        self.layoutWidget17.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout = QVBoxLayout(self.layoutWidget17)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(10)
        self.btn_investigar.setDefault(False)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.btn_tratativa.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SELECIONE A NOTIFICA\u00c7\u00c3O QUE DESEJA ACESSAR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u" EVENTO ADVERSO", None))
#if QT_CONFIG(tooltip)
        self.btn_fnea.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMA\u00c7\u00d5ES</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_fnea.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_fnea.setText(QCoreApplication.translate("MainWindow", u"FNEA", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u" N\u00c3O CONFORMIDADE", None))
#if QT_CONFIG(tooltip)
        self.btn_rnc.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMUL\u00c1RIO DE NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rnc.setText(QCoreApplication.translate("MainWindow", u"RNC", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por: M\u00e1rcio Anderson e Leonardo Aquino", None))
        self.btn_voltar_rnc.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"NOTIFICA\u00c7\u00c3O DE EVENTO ADVERSO", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_9.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"notihomologacao", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"notiproducao", None))

#if QT_CONFIG(tooltip)
        self.btn_login.setToolTip(QCoreApplication.translate("MainWindow", u"Informe Usu\u00e1rio e Senha e efetue o login", None))
#endif // QT_CONFIG(tooltip)
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"L O G  I N", None))
        self.btn_notificaSlogin.setText(QCoreApplication.translate("MainWindow", u"A P E N A S | N O T I F I C A R", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Estrat\u00e9gico", None))
#if QT_CONFIG(tooltip)
        self.btn_dashboard.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMA\u00c7\u00d5ES</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_dashboard.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_dashboard.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Cadastros", None))
#if QT_CONFIG(tooltip)
        self.btn_notifica.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMUL\u00c1RIO DE NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_notifica.setText("")
        self.btn_usuarios.setText("")
        self.btn_setor.setText("")
        self.btn_email.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Investiga\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_investigar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMUL\u00c1RIO DE INVESTIGA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_investigar.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Consulta", None))
#if QT_CONFIG(tooltip)
        self.btn_consultar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CONSULTA DE NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_consultar.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.btn_relatorio_2.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Logoff", None))
        self.btn_logoff.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_sairApp.setText("")
        self.label_2.setText("")
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Novo-------Editar-----Integra", None))
#if QT_CONFIG(tooltip)
        self.btn_notificar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_notificar.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_notificar.setText("")
#if QT_CONFIG(tooltip)
        self.btn_editarNoti.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">EDITAR NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_editarNoti.setText("")
#if QT_CONFIG(tooltip)
        self.btn_buscarMv.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">BUSCAR PACIENTE NO MV</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_buscarMv.setText("")
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"N\u00famero da Notifica\u00e7\u00e3o", None))
        self.txt_consultaNoti.setText("")
#if QT_CONFIG(tooltip)
        self.btn_pesquisarNoti.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pesquisarNoti.setText("")
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
#if QT_CONFIG(tooltip)
        self.btn_relatorio.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERAR FICHA DE NOTIFICA\u00c7\u00c3O EM PDF</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_relatorio.setText("")
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"Salvar | Cancelar", None))
#if QT_CONFIG(tooltip)
        self.btn_salva_noti.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SALVAR NOTIFICA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salva_noti.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cancela_noti.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CANCELAR NOTIFICA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancela_noti.setText("")
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Habilitar Edi\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_alterar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ALTERAR NOTIFICA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_alterar.setText("")
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Resumo Investiga\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_resumoInvest.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_resumoInvest.setText("")
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"Menu ", None))
#if QT_CONFIG(tooltip)
        self.btn_voltar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.cb_sex.setItemText(0, "")
        self.cb_sex.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cb_sex.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.cb_sex.setItemText(3, QCoreApplication.translate("MainWindow", u"Transg\u00eanero", None))
        self.cb_sex.setItemText(4, QCoreApplication.translate("MainWindow", u"Cisg\u00eanero", None))
        self.cb_sex.setItemText(5, QCoreApplication.translate("MainWindow", u"N\u00e3o-bin\u00e1rio", None))

        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Setor:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Leito:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Data Interna\u00e7\u00e3o", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Ra\u00e7a | Cor:", None))
        self.cb_rac.setItemText(0, "")
        self.cb_rac.setItemText(1, QCoreApplication.translate("MainWindow", u"Amarelo", None))
        self.cb_rac.setItemText(2, QCoreApplication.translate("MainWindow", u"Branco", None))
        self.cb_rac.setItemText(3, QCoreApplication.translate("MainWindow", u"Indigena", None))
        self.cb_rac.setItemText(4, QCoreApplication.translate("MainWindow", u"Pardo", None))
        self.cb_rac.setItemText(5, QCoreApplication.translate("MainWindow", u"Preto", None))
        self.cb_rac.setItemText(6, QCoreApplication.translate("MainWindow", u"Indefinido", None))

        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Cod.Paciente:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Paciente:", None))
        self.txt_nmPacient.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Nome Social:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3stico:", None))
        self.txt_diagnostic.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Tratamento:", None))
        self.txt_tratamento.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Dt|Hr Evento:", None))
#if QT_CONFIG(tooltip)
        self.rb_mt.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>De 7h \u00e0s 19h</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rb_mt.setText(QCoreApplication.translate("MainWindow", u"MT", None))
#if QT_CONFIG(tooltip)
        self.rb_sn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>19h \u00e0s 7h</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rb_sn.setText(QCoreApplication.translate("MainWindow", u"SN", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Dt|Hr Notifica\u00e7\u00e3o:", None))
        self.chk_nsp.setText(QCoreApplication.translate("MainWindow", u"NSP - N\u00daCLEO DE SEGURAN\u00c7A DO PACIENTE", None))
        self.ck_falha_id.setText(QCoreApplication.translate("MainWindow", u"Falha na Identifica\u00e7\u00e3o do Paciente", None))
        self.ck_falha_comu.setText(QCoreApplication.translate("MainWindow", u"Falha de Comunica\u00e7\u00e3o do Paciente.", None))
        self.ck_falha_oxi.setText(QCoreApplication.translate("MainWindow", u"Falha no Uso de Oxig\u00eanio e Outros Gases", None))
        self.ck_falha_sonda.setText(QCoreApplication.translate("MainWindow", u"Falha no Manuseio e na Identifica\u00e7\u00e3o dos Cateteres e\n"
"Sondas", None))
        self.ck_falha_nutri.setText(QCoreApplication.translate("MainWindow", u"Falha na Administra\u00e7\u00e3o da Nutri\u00e7\u00e3o.", None))
        self.ck_falha_hemo.setText(QCoreApplication.translate("MainWindow", u"Falha na Administra\u00e7\u00e3o de Hemocomponentes", None))
        self.ck_falha_med.setText(QCoreApplication.translate("MainWindow", u"Falha na Prescri\u00e7\u00e3o, Dispensa\u00e7\u00e3o, Manuseio, Preparo e/ou \n"
"Administra\u00e7\u00e3o de Medicamentos", None))
        self.ck_falha_usu.setText(QCoreApplication.translate("MainWindow", u"Falha no Transporte do Usu\u00e1rio", None))
        self.ck_falha_anest_2.setText(QCoreApplication.translate("MainWindow", u"Falha no Procedimento Anest\u00e9sico", None))
        self.ck_falha_dispo_2.setText(QCoreApplication.translate("MainWindow", u"Falha no Uso de Dispositivos e Equipamentos", None))
        self.ck_queda_hosp_2.setText(QCoreApplication.translate("MainWindow", u"Queda em Paciente Hospitalizado", None))
        self.ck_falha_cirurg_2.setText(QCoreApplication.translate("MainWindow", u"Falha no Procedimento Cir\u00fargico", None))
        self.ck_ulcera_2.setText(QCoreApplication.translate("MainWindow", u"\u00dalcera por Press\u00e3o Durante a Interna\u00e7\u00e3o", None))
        self.ck_infeccao_2.setText(QCoreApplication.translate("MainWindow", u"Infec\u00e7\u00e3o Associada \u00e0 Assist\u00eancia \u00e0 Sa\u00fade", None))
        self.ck_inadequada_2.setText(QCoreApplication.translate("MainWindow", u"Higiene das M\u00e3os Inadequada", None))
        self.ck_higiene_paciente_2.setText(QCoreApplication.translate("MainWindow", u"Higiene Prec\u00e1ria do Paciente", None))
        self.ck_neonato_2.setText(QCoreApplication.translate("MainWindow", u"Trauma no Nascimento: Dano ao Neonato", None))
        self.ck_vaginal_2.setText(QCoreApplication.translate("MainWindow", u"Trauma Obst\u00e9trico: Em Parto Vaginal", None))
        self.ck_cesariana_2.setText(QCoreApplication.translate("MainWindow", u"Trauma Obst\u00e9trico: Em Cesariana", None))
        self.ck_atendimento_2.setText(QCoreApplication.translate("MainWindow", u"Atraso no Atendimento", None))
        self.ck_conflito_2.setText(QCoreApplication.translate("MainWindow", u"Conflito", None))
        self.ck_evasao_2.setText(QCoreApplication.translate("MainWindow", u"Evas\u00e3o do Paciente", None))
        self.ck_sentinela_2.setText(QCoreApplication.translate("MainWindow", u"Evento Sentinela", None))
        self.ck_queimadura_2.setText(QCoreApplication.translate("MainWindow", u"Queimadura P\u00f3s-Procedimento", None))
        self.ck_outros_2.setText(QCoreApplication.translate("MainWindow", u"outros:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tipos de Eventos", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O DA OCORRENCIA:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"HOUVE DANO AO PACIENTE?", None))
        self.rb_dano_sim.setText(QCoreApplication.translate("MainWindow", u"SIM", None))
        self.rb_dano_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00c3O", None))
        self.rb_dano_SI.setText(QCoreApplication.translate("MainWindow", u"S.I", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"ESCALA DO DANO", None))
        self.cb_dan.setItemText(0, "")
        self.cb_dan.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u00c3O REGISTRADO", None))
        self.cb_dan.setItemText(2, QCoreApplication.translate("MainWindow", u"NENHUM", None))
        self.cb_dan.setItemText(3, QCoreApplication.translate("MainWindow", u"LEVE -(apresentou sintomas leves, danos de curta dura\u00e7\u00e3o, necessitou de observa\u00e7\u00e3o m\u00ednima.)", None))
        self.cb_dan.setItemText(4, QCoreApplication.translate("MainWindow", u"MODERADO -(apresentou sintomas, danos permanentes ou a longo prazo, necessitou de procedimento suplementar ou terap\u00eautica adicional.)", None))
        self.cb_dan.setItemText(5, QCoreApplication.translate("MainWindow", u"GRAVE - (necessitou de interven\u00e7\u00e3o para salvar vida, interven\u00e7\u00e3o m\u00e9dico-cir\u00fargica, danos permanentes ou em longo prazo..)", None))
        self.cb_dan.setItemText(6, QCoreApplication.translate("MainWindow", u"\u00d3BITO -(causado pelo evento adverso.)", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da Ocorrencia", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"COMO FOI IDENTIFICADO:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"A\u00c7\u00c3O TOMADA NO EVENTO:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"QUEM IDENTIFICOU:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"IDENTIFICA\u00c7\u00c3O(OPCIONAL)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Detalhes do Evento", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES -FNEA", None))
        self.label_3.setText("")
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"IDENTIFICA\u00c7\u00c3O DE FATORES CONTRIBUINTES: DIAGRAMA DE CAUSA E EFEITO - ISHIKAWA", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Paciente", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Pessoas", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Pessoas", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Materiais | Equipamentos", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Ambiente de Trabalho", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es:", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Recomenda\u00e7\u00f5es:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Investiga\u00e7\u00e3o", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Como?", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Conclus\u00e3o do Time:", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"O que?", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Por que?", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Quem?", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Quando?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Plano de A\u00e7\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES-FNEA", None))
#if QT_CONFIG(tooltip)
        self.btn_voltar_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_2.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Buscar Notifica\u00e7\u00e3o", None))
        self.btn_buscarInv.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Concluir |    Cancelar |    Alterar", None))
        self.btn_conclusao_2.setText("")
        self.btn_cancela_investiga_2.setText("")
        self.btn_alterarInv_2.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Resumo Notifica\u00e7\u00e3o", None))
        self.btn_resumo.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Habilitar Edi\u00e7\u00e3o", None))
        self.btn_editarInv.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Status Investiga\u00e7\u00e3o", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"N\u00e3o iniciada", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Em andamento", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Com Pend\u00eancias", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Conclu\u00eddo", None))

        self.btn_Spdf_2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES-FNEA", None))
        self.groupBox_61.setTitle(QCoreApplication.translate("MainWindow", u"Consultar Notifica\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.btn_voltar_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_3.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Paciente:", None))
        self.btn_consultarNoti_2.setText("")
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa por Status", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Iniciada", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Em Andamento", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Com Pend\u00eancias", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"Conclu\u00edda", None))
        ___qtablewidgetitem = self.tb_consulta_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CodN", None));
        ___qtablewidgetitem1 = self.tb_consulta_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CodP", None));
        ___qtablewidgetitem2 = self.tb_consulta_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem3 = self.tb_consulta_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem4 = self.tb_consulta_4.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Unidade de interna\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tb_consulta_4.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cod-Inv", None));
        ___qtablewidgetitem6 = self.tb_consulta_4.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data Evento", None));
        ___qtablewidgetitem7 = self.tb_consulta_4.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data Notifica\u00e7\u00e3o", None));
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Usu\u00e1rios", None))
#if QT_CONFIG(tooltip)
        self.btn_voltar_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_4.setText("")
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.txt_cadnome_4.setText("")
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_cadnome_5.setText("")
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_cadnome_6.setText("")
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_outros_4.setItemText(0, "")
        self.cb_outros_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Notificador", None))
        self.cb_outros_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Investigador N1", None))
        self.cb_outros_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Investigador N2", None))
        self.cb_outros_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"Consulta Usu\u00e1rios Cadastrados", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.btn_consultaUser_2.setText("")
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Perfil", None));
        self.groupBox_48.setTitle(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_salvaUser_2.setText("")
        self.groupBox_49.setTitle(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_cancelaUser_2.setText("")
        self.groupBox_45.setTitle(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.btn_novoUser_2.setText("")
        self.groupBox_46.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_editaUser_2.setText("")
        self.groupBox_47.setTitle(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_alterarUser_2.setText("")
        self.groupBox_50.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Setor", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Setor", None));
        self.groupBox_51.setTitle(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.btn_novo_setor.setText("")
        self.groupBox_52.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_edita_setor.setText("")
        self.groupBox_55.setTitle(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_conf_alterar.setText("")
        self.groupBox_53.setTitle(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_salvar_setor.setText("")
        self.groupBox_54.setTitle(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_cancela_setor.setText("")
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES-FNEA", None))
#if QT_CONFIG(tooltip)
        self.btn_voltar_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_5.setText("")
        self.groupBox_56.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro de E-mail para recebimento de notifica\u00e7\u00e3o", None))
        self.groupBox_58.setTitle(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.btn_novoEmail.setText("")
        self.groupBox_59.setTitle(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_alterar_email.setText("")
        self.groupBox_60.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisa_email.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.groupBox_57.setTitle(QCoreApplication.translate("MainWindow", u"E-mails Cadastrados", None))
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_11.setText("")
#if QT_CONFIG(tooltip)
        self.btn_voltar_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RESUMO DA INVESTIGA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_voltar_6.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SIN - SISTEMA INTEGRADO DE NOTIFICA\u00c7\u00d5ES-FNEA", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"REGISTRO DE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u" N\u00c3O CONFORMIDADE", None))
        self.txt_usuario.setText("")
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu Usu\u00e1rio", None))
        self.txt_senha.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua Senha", None))
        self.cb_empresa.setItemText(0, QCoreApplication.translate("MainWindow", u"bd_rnc", None))
        self.cb_empresa.setItemText(1, QCoreApplication.translate("MainWindow", u"bd_rnc_homologa", None))

        self.cb_empresa.setPlaceholderText("")
        self.btn_anonimo.setText(QCoreApplication.translate("MainWindow", u"AN\u00d4NIMO", None))
        self.btn_login_rnc.setText(QCoreApplication.translate("MainWindow", u"L O G I N", None))
        self.label_14.setText("")
        self.btn_SairApp.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.groupBox_128.setTitle(QCoreApplication.translate("MainWindow", u"Logoff", None))
        self.btn_logoff_3.setText("")
        self.groupBox_129.setTitle(QCoreApplication.translate("MainWindow", u"Estrat\u00e9gico", None))
#if QT_CONFIG(tooltip)
        self.btn_dashboard_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMA\u00c7\u00d5ES</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_dashboard_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_dashboard_2.setText("")
        self.groupBox_123.setTitle(QCoreApplication.translate("MainWindow", u"Cadastros", None))
#if QT_CONFIG(tooltip)
        self.btn_rnc_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMUL\u00c1RIO DE NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rnc_2.setText("")
        self.btn_usuarios_2.setText("")
        self.groupBox_124.setTitle(QCoreApplication.translate("MainWindow", u"Investiga\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_tratativa.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMUL\u00c1RIO DE INVESTIGA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tratativa.setText("")
        self.groupBox_127.setTitle(QCoreApplication.translate("MainWindow", u"Consulta", None))
#if QT_CONFIG(tooltip)
        self.btn_consultar_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CONSULTA DE NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_consultar_2.setText("")
        self.groupBox_125.setTitle(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.groupBox_126.setTitle(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

