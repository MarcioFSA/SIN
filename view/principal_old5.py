import datetime
import getpass
import sys
import webbrowser
from distutils.log import error
from functools import lru_cache

from fpdf import FPDF
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QPoint, Qt, QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

from FNEA.bd.conn import conexaoBD

from FNEA.relatorio.manip_dados import Relatorio
from FNEA.view.outros import *
from FNEA.view.resumo_investiga import *
from FNEA.view.resumo_notifica import *

# from bd.connect import conexaoOracle

con = conexaoBD()
# conn = conexaoOracle()

cd_notificacao = 0
cd_usuario = 0
cd_paciente = 0
window = None
from FNEA.model.anonimo import *
from FNEA.model.usuarios import*
from FNEA.model.investigacao import*
from FNEA.model.comboxes import*
from FNEA.model.login import*
from FNEA.model.logoff import*
from FNEA.model.dashboard import*
from FNEA.model.relatorio import*
from FNEA.model.anonimo import*
from FNEA.model.consulta import*
from FNEA.controller.botoes import *
from FNEA.model.login import *
from FNEA.model.notificacao import *
from FNEA.model.email import *
from FNEA.model.tabelas import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1024, 700))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(5, 9, 1020, 700))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1020, 700))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1020, 700))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(210, 80))
        self.label_4.setStyleSheet("image: url(:/Imagem/Logo SIN.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_13.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label)
        self.gridLayout_6.addLayout(self.verticalLayout_13, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(290, 440))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 110, 251, 80))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_fnea = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_fnea.setGeometry(QtCore.QRect(70, 30, 100, 40))
        self.btn_fnea.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_fnea.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.btn_fnea.setFont(font)
        self.btn_fnea.setStatusTip("")
        self.btn_fnea.setStyleSheet("QPushButton#btn_fnea{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_fnea:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_fnea:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagem/dashboard (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fnea.setIcon(icon)
        self.btn_fnea.setIconSize(QtCore.QSize(24, 24))
        self.btn_fnea.setObjectName("btn_fnea")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 270, 251, 80))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn_rnc = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_rnc.setEnabled(False)
        self.btn_rnc.setGeometry(QtCore.QRect(73, 26, 100, 40))
        self.btn_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_rnc.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_rnc.setFont(font)
        self.btn_rnc.setStyleSheet("QPushButton#btn_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imagem/prancheta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rnc.setIcon(icon1)
        self.btn_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_rnc.setObjectName("btn_rnc")
        self.gridLayout_6.addWidget(self.groupBox, 1, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(324, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(324, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 62, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(271, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        self.btn_voltar_fnea = QtWidgets.QPushButton(self.page_2)
        self.btn_voltar_fnea.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_voltar_fnea.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(True)
        font.setItalic(False)
        self.btn_voltar_fnea.setFont(font)
        self.btn_voltar_fnea.setStyleSheet("QPushButton#btn_voltar_fnea{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar_fnea:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar_fnea:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Imagens/vire-a-esquerda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voltar_fnea.setIcon(icon2)
        self.btn_voltar_fnea.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_fnea.setObjectName("btn_voltar_fnea")
        self.gridLayout_2.addWidget(self.btn_voltar_fnea, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 4, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(771, 541))
        self.groupBox_4.setStyleSheet("border-top-left-radius:50px;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_2.setMinimumSize(QtCore.QSize(510, 410))
        self.widget_2.setMaximumSize(QtCore.QSize(510, 410))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 201, 411))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"border-top-left-radius:50px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(210, 10, 221, 411))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(241, 200, 250, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(241, 240, 250, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(282, 27, 151, 151))
        self.label_9.setMinimumSize(QtCore.QSize(151, 151))
        self.label_9.setStyleSheet("image: url(:/Imagem/user.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(239, 290, 251, 22))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.layoutWidget_5 = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(240, 320, 252, 88))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_login.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton#btn_login{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Imagem/user (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon3)
        self.btn_login.setIconSize(QtCore.QSize(24, 24))
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_19.addWidget(self.btn_login)
        self.btn_notificaSlogin = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_notificaSlogin.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.btn_notificaSlogin.setFont(font)
        self.btn_notificaSlogin.setStyleSheet("QPushButton#btn_notificaSlogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(110, 1, 0, 255), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notificaSlogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notificaSlogin:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Imagem/investigacao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_notificaSlogin.setIcon(icon4)
        self.btn_notificaSlogin.setIconSize(QtCore.QSize(24, 24))
        self.btn_notificaSlogin.setObjectName("btn_notificaSlogin")
        self.verticalLayout_19.addWidget(self.btn_notificaSlogin)
        self.gridLayout_7.addWidget(self.widget_2, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 1, 2, 5)
        spacerItem9 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(84, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 2, 5, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_5.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_5.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_dashboard = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_dashboard.setGeometry(QtCore.QRect(9, 16, 60, 30))
        self.btn_dashboard.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_dashboard.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.btn_dashboard.setFont(font)
        self.btn_dashboard.setStatusTip("")
        self.btn_dashboard.setStyleSheet("QPushButton#btn_dashboard{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_dashboard:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_dashboard:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_dashboard.setText("")
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(24, 24))
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.horizontalLayout_7.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_6.setMinimumSize(QtCore.QSize(271, 51))
        self.groupBox_6.setMaximumSize(QtCore.QSize(271, 51))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget_3.setGeometry(QtCore.QRect(6, 14, 260, 32))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.btn_notifica = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_notifica.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_notifica.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_notifica.setFont(font)
        self.btn_notifica.setStyleSheet("QPushButton#btn_notifica{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_notifica.setText("")
        self.btn_notifica.setIcon(icon1)
        self.btn_notifica.setIconSize(QtCore.QSize(24, 24))
        self.btn_notifica.setObjectName("btn_notifica")
        self.horizontalLayout_27.addWidget(self.btn_notifica)
        self.btn_usuarios = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_usuarios.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_usuarios.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_usuarios.setFont(font)
        self.btn_usuarios.setStyleSheet("QPushButton#btn_usuarios{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_usuarios:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_usuarios:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_usuarios.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Imagem/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_usuarios.setIcon(icon5)
        self.btn_usuarios.setIconSize(QtCore.QSize(24, 24))
        self.btn_usuarios.setObjectName("btn_usuarios")
        self.horizontalLayout_27.addWidget(self.btn_usuarios)
        self.btn_setor = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_setor.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_setor.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_setor.setFont(font)
        self.btn_setor.setStyleSheet("QPushButton#btn_setor{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_setor:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_setor:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_setor.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Imagem/grafico-de-setores.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_setor.setIcon(icon6)
        self.btn_setor.setIconSize(QtCore.QSize(24, 24))
        self.btn_setor.setObjectName("btn_setor")
        self.horizontalLayout_27.addWidget(self.btn_setor)
        self.btn_email = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_email.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_email.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_email.setFont(font)
        self.btn_email.setStyleSheet("QPushButton#btn_email{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_email:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_email:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_email.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Imagem/marketing-de-email (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon7)
        self.btn_email.setIconSize(QtCore.QSize(24, 24))
        self.btn_email.setObjectName("btn_email")
        self.horizontalLayout_27.addWidget(self.btn_email)
        self.horizontalLayout_7.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_7.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_7.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.btn_investigar = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_investigar.setEnabled(True)
        self.btn_investigar.setGeometry(QtCore.QRect(9, 17, 60, 30))
        self.btn_investigar.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_investigar.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_investigar.setFont(font)
        self.btn_investigar.setStyleSheet("QPushButton#btn_investigar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_investigar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_investigar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_investigar.setText("")
        self.btn_investigar.setIcon(icon4)
        self.btn_investigar.setIconSize(QtCore.QSize(24, 24))
        self.btn_investigar.setDefault(False)
        self.btn_investigar.setObjectName("btn_investigar")
        self.horizontalLayout_7.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_8.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_8.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_8.setObjectName("groupBox_8")
        self.btn_consultar = QtWidgets.QPushButton(self.groupBox_8)
        self.btn_consultar.setGeometry(QtCore.QRect(10, 17, 60, 30))
        self.btn_consultar.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_consultar.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_consultar.setFont(font)
        self.btn_consultar.setStyleSheet("QPushButton#btn_consultar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultar.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Imagem/pesquisa-de-dados (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_consultar.setIcon(icon8)
        self.btn_consultar.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultar.setObjectName("btn_consultar")
        self.horizontalLayout_7.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_9.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_9.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.btn_relatorio_2 = QtWidgets.QPushButton(self.groupBox_9)
        self.btn_relatorio_2.setEnabled(True)
        self.btn_relatorio_2.setGeometry(QtCore.QRect(10, 16, 60, 30))
        self.btn_relatorio_2.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_relatorio_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_relatorio_2.setFont(font)
        self.btn_relatorio_2.setStyleSheet("QPushButton#btn_relatorio_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_relatorio_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_relatorio_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_relatorio_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Imagem/relatorio-de-negocios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_relatorio_2.setIcon(icon9)
        self.btn_relatorio_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_relatorio_2.setObjectName("btn_relatorio_2")
        self.horizontalLayout_7.addWidget(self.groupBox_9)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.groupBox_10 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_10.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_10.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_10.setObjectName("groupBox_10")
        self.btn_logoff = QtWidgets.QPushButton(self.groupBox_10)
        self.btn_logoff.setGeometry(QtCore.QRect(6, 16, 60, 30))
        self.btn_logoff.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_logoff.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_logoff.setFont(font)
        self.btn_logoff.setStyleSheet("QPushButton#btn_logoff{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_logoff:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_logoff:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_logoff.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Imagem/check-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logoff.setIcon(icon10)
        self.btn_logoff.setIconSize(QtCore.QSize(24, 24))
        self.btn_logoff.setObjectName("btn_logoff")
        self.horizontalLayout_32.addWidget(self.groupBox_10)
        self.groupBox_11 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_11.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_11.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.btn_sairApp = QtWidgets.QPushButton(self.groupBox_11)
        self.btn_sairApp.setGeometry(QtCore.QRect(9, 16, 60, 30))
        self.btn_sairApp.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_sairApp.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_sairApp.setFont(font)
        self.btn_sairApp.setStyleSheet("QPushButton#btn_sairApp{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sairApp:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sairApp:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_sairApp.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Imagem/remover (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sairApp.setIcon(icon11)
        self.btn_sairApp.setIconSize(QtCore.QSize(24, 24))
        self.btn_sairApp.setObjectName("btn_sairApp")
        self.horizontalLayout_32.addWidget(self.groupBox_11)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.logado = QtWidgets.QLabel(self.page_6)
        self.logado.setMinimumSize(QtCore.QSize(111, 21))
        self.logado.setMaximumSize(QtCore.QSize(16777215, 21))
        self.logado.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.logado.setText("")
        self.logado.setAlignment(QtCore.Qt.AlignCenter)
        self.logado.setObjectName("logado")
        self.horizontalLayout_12.addWidget(self.logado)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.label_2 = QtWidgets.QLabel(self.page_6)
        self.label_2.setMinimumSize(QtCore.QSize(780, 490))
        self.label_2.setStyleSheet("image: url(:/Imagem/FNEA.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout_11.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem17 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_30 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_30.setMinimumSize(QtCore.QSize(181, 61))
        self.groupBox_30.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_30.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_30.setObjectName("groupBox_30")
        self.btn_notificar = QtWidgets.QPushButton(self.groupBox_30)
        self.btn_notificar.setEnabled(False)
        self.btn_notificar.setGeometry(QtCore.QRect(15, 19, 30, 30))
        self.btn_notificar.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_notificar.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_notificar.setFont(font)
        self.btn_notificar.setWhatsThis("")
        self.btn_notificar.setStyleSheet("QPushButton#btn_notificar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notificar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notificar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_notificar.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Imagem/registro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_notificar.setIcon(icon12)
        self.btn_notificar.setIconSize(QtCore.QSize(24, 24))
        self.btn_notificar.setObjectName("btn_notificar")
        self.btn_editarNoti = QtWidgets.QPushButton(self.groupBox_30)
        self.btn_editarNoti.setEnabled(False)
        self.btn_editarNoti.setGeometry(QtCore.QRect(75, 19, 30, 30))
        self.btn_editarNoti.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_editarNoti.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_editarNoti.setFont(font)
        self.btn_editarNoti.setStyleSheet("QPushButton#btn_editarNoti{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editarNoti:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editarNoti:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_editarNoti.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Imagem/registro (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editarNoti.setIcon(icon13)
        self.btn_editarNoti.setIconSize(QtCore.QSize(24, 24))
        self.btn_editarNoti.setObjectName("btn_editarNoti")
        self.btn_buscarMv = QtWidgets.QPushButton(self.groupBox_30)
        self.btn_buscarMv.setEnabled(False)
        self.btn_buscarMv.setGeometry(QtCore.QRect(132, 18, 30, 30))
        self.btn_buscarMv.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_buscarMv.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.btn_buscarMv.setFont(font)
        self.btn_buscarMv.setStyleSheet("QPushButton#btn_buscarMv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_buscarMv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_buscarMv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_buscarMv.setText("")
        self.btn_buscarMv.setIcon(icon8)
        self.btn_buscarMv.setIconSize(QtCore.QSize(24, 24))
        self.btn_buscarMv.setObjectName("btn_buscarMv")
        self.horizontalLayout.addWidget(self.groupBox_30)
        self.groupBox_33 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_33.setMinimumSize(QtCore.QSize(180, 61))
        self.groupBox_33.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_33.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_33.setObjectName("groupBox_33")
        self.txt_consultaNoti = QtWidgets.QLineEdit(self.groupBox_33)
        self.txt_consultaNoti.setGeometry(QtCore.QRect(10, 30, 121, 30))
        self.txt_consultaNoti.setMinimumSize(QtCore.QSize(100, 30))
        self.txt_consultaNoti.setMaximumSize(QtCore.QSize(167777, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_consultaNoti.setFont(font)
        self.txt_consultaNoti.setStyleSheet("\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")
        self.txt_consultaNoti.setText("")
        self.txt_consultaNoti.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_consultaNoti.setObjectName("txt_consultaNoti")
        self.btn_pesquisarNoti = QtWidgets.QPushButton(self.groupBox_33)
        self.btn_pesquisarNoti.setGeometry(QtCore.QRect(140, 20, 30, 30))
        self.btn_pesquisarNoti.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_pesquisarNoti.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_pesquisarNoti.setFont(font)
        self.btn_pesquisarNoti.setStyleSheet("QPushButton#btn_pesquisarNoti{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisarNoti:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisarNoti:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisarNoti.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Imagem/historia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pesquisarNoti.setIcon(icon14)
        self.btn_pesquisarNoti.setIconSize(QtCore.QSize(24, 24))
        self.btn_pesquisarNoti.setObjectName("btn_pesquisarNoti")
        self.horizontalLayout.addWidget(self.groupBox_33)
        self.groupBox_31 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_31.setMinimumSize(QtCore.QSize(80, 61))
        self.groupBox_31.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_31.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_31.setObjectName("groupBox_31")
        self.btn_relatorio = QtWidgets.QPushButton(self.groupBox_31)
        self.btn_relatorio.setEnabled(False)
        self.btn_relatorio.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.btn_relatorio.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_relatorio.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_relatorio.setFont(font)
        self.btn_relatorio.setStyleSheet("QPushButton#btn_relatorio{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_relatorio:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_relatorio:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_relatorio.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Imagem/pdf (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_relatorio.setIcon(icon15)
        self.btn_relatorio.setIconSize(QtCore.QSize(24, 24))
        self.btn_relatorio.setObjectName("btn_relatorio")
        self.horizontalLayout.addWidget(self.groupBox_31)
        self.groupBox_32 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_32.setMinimumSize(QtCore.QSize(105, 61))
        self.groupBox_32.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_32.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_32.setObjectName("groupBox_32")
        self.btn_salva_noti = QtWidgets.QPushButton(self.groupBox_32)
        self.btn_salva_noti.setEnabled(False)
        self.btn_salva_noti.setGeometry(QtCore.QRect(6, 21, 30, 30))
        self.btn_salva_noti.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_salva_noti.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_salva_noti.setFont(font)
        self.btn_salva_noti.setStyleSheet("QPushButton#btn_salva_noti{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salva_noti:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salva_noti:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salva_noti.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/Imagem/salve-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_salva_noti.setIcon(icon16)
        self.btn_salva_noti.setIconSize(QtCore.QSize(24, 24))
        self.btn_salva_noti.setObjectName("btn_salva_noti")
        self.btn_cancela_noti = QtWidgets.QPushButton(self.groupBox_32)
        self.btn_cancela_noti.setEnabled(False)
        self.btn_cancela_noti.setGeometry(QtCore.QRect(58, 21, 30, 30))
        self.btn_cancela_noti.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_cancela_noti.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_cancela_noti.setFont(font)
        self.btn_cancela_noti.setStyleSheet("QPushButton#btn_cancela_noti{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_noti:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_noti:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_noti.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/Imagem/cancelar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancela_noti.setIcon(icon17)
        self.btn_cancela_noti.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_noti.setObjectName("btn_cancela_noti")
        self.horizontalLayout.addWidget(self.groupBox_32)
        self.groupBox_34 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_34.setMinimumSize(QtCore.QSize(101, 61))
        self.groupBox_34.setMaximumSize(QtCore.QSize(101, 61))
        self.groupBox_34.setObjectName("groupBox_34")
        self.btn_alterar = QtWidgets.QPushButton(self.groupBox_34)
        self.btn_alterar.setEnabled(False)
        self.btn_alterar.setGeometry(QtCore.QRect(33, 20, 30, 30))
        self.btn_alterar.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_alterar.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_alterar.setFont(font)
        self.btn_alterar.setStyleSheet("QPushButton#btn_alterar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterar.setText("")
        self.btn_alterar.setIcon(icon13)
        self.btn_alterar.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterar.setObjectName("btn_alterar")
        self.horizontalLayout.addWidget(self.groupBox_34)
        self.groupBox_35 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_35.setMinimumSize(QtCore.QSize(131, 61))
        self.groupBox_35.setMaximumSize(QtCore.QSize(131, 61))
        self.groupBox_35.setObjectName("groupBox_35")
        self.btn_resumoInvest = QtWidgets.QPushButton(self.groupBox_35)
        self.btn_resumoInvest.setEnabled(True)
        self.btn_resumoInvest.setGeometry(QtCore.QRect(45, 21, 30, 30))
        self.btn_resumoInvest.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_resumoInvest.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_resumoInvest.setFont(font)
        self.btn_resumoInvest.setStyleSheet("QPushButton#btn_resumoInvest{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumoInvest:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumoInvest:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_resumoInvest.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/Imagem/resumo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_resumoInvest.setIcon(icon18)
        self.btn_resumoInvest.setIconSize(QtCore.QSize(24, 24))
        self.btn_resumoInvest.setObjectName("btn_resumoInvest")
        self.horizontalLayout.addWidget(self.groupBox_35)
        self.groupBox_36 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_36.setMinimumSize(QtCore.QSize(61, 61))
        self.groupBox_36.setMaximumSize(QtCore.QSize(61, 61))
        self.groupBox_36.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_36.setObjectName("groupBox_36")
        self.btn_voltar = QtWidgets.QPushButton(self.groupBox_36)
        self.btn_voltar.setEnabled(True)
        self.btn_voltar.setGeometry(QtCore.QRect(15, 20, 30, 30))
        self.btn_voltar.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar.setFont(font)
        self.btn_voltar.setStyleSheet("QPushButton#btn_voltar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/Imagem/voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voltar.setIcon(icon19)
        self.btn_voltar.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar.setObjectName("btn_voltar")
        self.horizontalLayout.addWidget(self.groupBox_36)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.frame_21 = QtWidgets.QFrame(self.page_3)
        self.frame_21.setMinimumSize(QtCore.QSize(901, 135))
        self.frame_21.setMaximumSize(QtCore.QSize(901, 135))
        self.frame_21.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setLineWidth(1)
        self.frame_21.setMidLineWidth(0)
        self.frame_21.setObjectName("frame_21")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_21)
        self.layoutWidget_6.setGeometry(QtCore.QRect(13, 11, 863, 115))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_67 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_22.addWidget(self.label_67)
        self.txt_codPacient = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txt_codPacient.setEnabled(False)
        self.txt_codPacient.setMinimumSize(QtCore.QSize(60, 0))
        self.txt_codPacient.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_codPacient.setFont(font)
        self.txt_codPacient.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_codPacient.setObjectName("txt_codPacient")
        self.horizontalLayout_22.addWidget(self.txt_codPacient)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_68 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_21.addWidget(self.label_68)
        self.txt_nmPacient = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txt_nmPacient.setEnabled(False)
        self.txt_nmPacient.setMinimumSize(QtCore.QSize(250, 0))
        self.txt_nmPacient.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_nmPacient.setFont(font)
        self.txt_nmPacient.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_nmPacient.setText("")
        self.txt_nmPacient.setObjectName("txt_nmPacient")
        self.horizontalLayout_21.addWidget(self.txt_nmPacient)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)
        self.label_82 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.horizontalLayout_22.addWidget(self.label_82)
        self.txt_social = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txt_social.setEnabled(False)
        self.txt_social.setMinimumSize(QtCore.QSize(60, 0))
        self.txt_social.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_social.setFont(font)
        self.txt_social.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_social.setObjectName("txt_social")
        self.horizontalLayout_22.addWidget(self.txt_social)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_22.addWidget(self.label_69)
        self.dt_nascimento = QtWidgets.QDateEdit(self.layoutWidget_6)
        self.dt_nascimento.setEnabled(False)
        self.dt_nascimento.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dt_nascimento.setFont(font)
        self.dt_nascimento.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 3), QtCore.QTime(21, 0, 0)))
        self.dt_nascimento.setCalendarPopup(True)
        self.dt_nascimento.setObjectName("dt_nascimento")
        self.horizontalLayout_22.addWidget(self.dt_nascimento)
        self.verticalLayout_6.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_70 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_70.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_4.addWidget(self.label_70)
        self.cb_sex = QtWidgets.QComboBox(self.layoutWidget_6)
        self.cb_sex.setEnabled(False)
        self.cb_sex.setMinimumSize(QtCore.QSize(160, 0))
        self.cb_sex.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.cb_sex.setFont(font)
        self.cb_sex.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_sex.setObjectName("cb_sex")
        self.cb_sex.addItem("")
        self.cb_sex.setItemText(0, "")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.horizontalLayout_4.addWidget(self.cb_sex)
        self.horizontalLayout_84.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.label_71 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_82.addWidget(self.label_71)
        self.cb_seto = QtWidgets.QComboBox(self.layoutWidget_6)
        self.cb_seto.setEnabled(False)
        self.cb_seto.setMinimumSize(QtCore.QSize(291, 0))
        self.cb_seto.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.cb_seto.setFont(font)
        self.cb_seto.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_seto.setObjectName("cb_seto")
        self.horizontalLayout_82.addWidget(self.cb_seto)
        self.horizontalLayout_84.addLayout(self.horizontalLayout_82)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.label_66 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_83.addWidget(self.label_66)
        self.cb_rac = QtWidgets.QComboBox(self.layoutWidget_6)
        self.cb_rac.setEnabled(False)
        self.cb_rac.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.cb_rac.setFont(font)
        self.cb_rac.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_rac.setObjectName("cb_rac")
        self.cb_rac.addItem("")
        self.cb_rac.setItemText(0, "")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.cb_rac.addItem("")
        self.horizontalLayout_83.addWidget(self.cb_rac)
        self.horizontalLayout_84.addLayout(self.horizontalLayout_83)
        self.verticalLayout_6.addLayout(self.horizontalLayout_84)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_81 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_41.addWidget(self.label_81)
        self.cb_seto_ocorrencia = QtWidgets.QComboBox(self.layoutWidget_6)
        self.cb_seto_ocorrencia.setEnabled(False)
        self.cb_seto_ocorrencia.setMinimumSize(QtCore.QSize(291, 0))
        self.cb_seto_ocorrencia.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.cb_seto_ocorrencia.setFont(font)
        self.cb_seto_ocorrencia.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_seto_ocorrencia.setObjectName("cb_seto_ocorrencia")
        self.horizontalLayout_41.addWidget(self.cb_seto_ocorrencia)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_72.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_41.addWidget(self.label_72)
        self.txt_leit = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txt_leit.setEnabled(False)
        self.txt_leit.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_leit.setFont(font)
        self.txt_leit.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_leit.setObjectName("txt_leit")
        self.horizontalLayout_41.addWidget(self.txt_leit)
        self.label_73 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_73.setFont(font)
        self.label_73.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_41.addWidget(self.label_73)
        self.dt_internacao = QtWidgets.QDateEdit(self.layoutWidget_6)
        self.dt_internacao.setEnabled(False)
        self.dt_internacao.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dt_internacao.setFont(font)
        self.dt_internacao.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 3), QtCore.QTime(21, 0, 0)))
        self.dt_internacao.setCalendarPopup(True)
        self.dt_internacao.setObjectName("dt_internacao")
        self.horizontalLayout_41.addWidget(self.dt_internacao)
        self.verticalLayout_6.addLayout(self.horizontalLayout_41)
        self.verticalLayout_8.addWidget(self.frame_21)
        self.frame_19 = QtWidgets.QFrame(self.page_3)
        self.frame_19.setMinimumSize(QtCore.QSize(901, 91))
        self.frame_19.setMaximumSize(QtCore.QSize(901, 91))
        self.frame_19.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.layoutWidget_8 = QtWidgets.QWidget(self.frame_19)
        self.layoutWidget_8.setGeometry(QtCore.QRect(21, 6, 856, 77))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_62 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_25.addWidget(self.label_62)
        self.txt_diagnostic = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.txt_diagnostic.setEnabled(False)
        self.txt_diagnostic.setMinimumSize(QtCore.QSize(301, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_diagnostic.setFont(font)
        self.txt_diagnostic.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_diagnostic.setText("")
        self.txt_diagnostic.setObjectName("txt_diagnostic")
        self.horizontalLayout_25.addWidget(self.txt_diagnostic)
        self.label_63 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_25.addWidget(self.label_63)
        self.txt_tratamento = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.txt_tratamento.setEnabled(False)
        self.txt_tratamento.setMinimumSize(QtCore.QSize(401, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_tratamento.setFont(font)
        self.txt_tratamento.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_tratamento.setText("")
        self.txt_tratamento.setObjectName("txt_tratamento")
        self.horizontalLayout_25.addWidget(self.txt_tratamento)
        self.verticalLayout_20.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_64 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_23.addWidget(self.label_64)
        self.dt_evento = QtWidgets.QDateEdit(self.layoutWidget_8)
        self.dt_evento.setEnabled(False)
        self.dt_evento.setMinimumSize(QtCore.QSize(101, 0))
        self.dt_evento.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dt_evento.setFont(font)
        self.dt_evento.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 2), QtCore.QTime(18, 0, 0)))
        self.dt_evento.setCalendarPopup(True)
        self.dt_evento.setObjectName("dt_evento")
        self.horizontalLayout_23.addWidget(self.dt_evento)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.rb_mt = QtWidgets.QRadioButton(self.layoutWidget_8)
        self.rb_mt.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.rb_mt.setFont(font)
        self.rb_mt.setObjectName("rb_mt")
        self.horizontalLayout_24.addWidget(self.rb_mt)
        self.rb_sn = QtWidgets.QRadioButton(self.layoutWidget_8)
        self.rb_sn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.rb_sn.setFont(font)
        self.rb_sn.setObjectName("rb_sn")
        self.horizontalLayout_24.addWidget(self.rb_sn)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_65 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_65.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_17.addWidget(self.label_65)
        self.dt_notificacao = QtWidgets.QDateEdit(self.layoutWidget_8)
        self.dt_notificacao.setEnabled(False)
        self.dt_notificacao.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dt_notificacao.setFont(font)
        self.dt_notificacao.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 2), QtCore.QTime(18, 0, 0)))
        self.dt_notificacao.setCalendarPopup(True)
        self.dt_notificacao.setObjectName("dt_notificacao")
        self.horizontalLayout_17.addWidget(self.dt_notificacao)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_17)
        self.chk_nsp = QtWidgets.QCheckBox(self.layoutWidget_8)
        self.chk_nsp.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.chk_nsp.setFont(font)
        self.chk_nsp.setObjectName("chk_nsp")
        self.horizontalLayout_26.addWidget(self.chk_nsp)
        self.verticalLayout_20.addLayout(self.horizontalLayout_26)
        self.verticalLayout_8.addWidget(self.frame_19)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.page_3)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(901, 361))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(901, 361))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 13, 870, 307))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ck_falha_id = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_id.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_id.setFont(font)
        self.ck_falha_id.setObjectName("ck_falha_id")
        self.verticalLayout_2.addWidget(self.ck_falha_id)
        self.ck_falha_comu = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_comu.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_comu.setFont(font)
        self.ck_falha_comu.setObjectName("ck_falha_comu")
        self.verticalLayout_2.addWidget(self.ck_falha_comu)
        self.ck_falha_oxi = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_oxi.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_oxi.setFont(font)
        self.ck_falha_oxi.setObjectName("ck_falha_oxi")
        self.verticalLayout_2.addWidget(self.ck_falha_oxi)
        self.ck_falha_sonda = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_sonda.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_sonda.setFont(font)
        self.ck_falha_sonda.setObjectName("ck_falha_sonda")
        self.verticalLayout_2.addWidget(self.ck_falha_sonda)
        self.ck_falha_nutri = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_nutri.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_nutri.setFont(font)
        self.ck_falha_nutri.setObjectName("ck_falha_nutri")
        self.verticalLayout_2.addWidget(self.ck_falha_nutri)
        self.ck_falha_hemo = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_hemo.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_hemo.setFont(font)
        self.ck_falha_hemo.setObjectName("ck_falha_hemo")
        self.verticalLayout_2.addWidget(self.ck_falha_hemo)
        self.ck_falha_med = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_med.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_med.setFont(font)
        self.ck_falha_med.setObjectName("ck_falha_med")
        self.verticalLayout_2.addWidget(self.ck_falha_med)
        self.ck_falha_usu = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_usu.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_usu.setFont(font)
        self.ck_falha_usu.setObjectName("ck_falha_usu")
        self.verticalLayout_2.addWidget(self.ck_falha_usu)
        self.horizontalLayout_15.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ck_falha_anest_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_anest_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_anest_2.setFont(font)
        self.ck_falha_anest_2.setObjectName("ck_falha_anest_2")
        self.verticalLayout_3.addWidget(self.ck_falha_anest_2)
        self.ck_falha_dispo_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_dispo_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_dispo_2.setFont(font)
        self.ck_falha_dispo_2.setObjectName("ck_falha_dispo_2")
        self.verticalLayout_3.addWidget(self.ck_falha_dispo_2)
        self.ck_queda_hosp_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_queda_hosp_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_queda_hosp_2.setFont(font)
        self.ck_queda_hosp_2.setObjectName("ck_queda_hosp_2")
        self.verticalLayout_3.addWidget(self.ck_queda_hosp_2)
        self.ck_falha_cirurg_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_falha_cirurg_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_falha_cirurg_2.setFont(font)
        self.ck_falha_cirurg_2.setObjectName("ck_falha_cirurg_2")
        self.verticalLayout_3.addWidget(self.ck_falha_cirurg_2)
        self.ck_ulcera_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_ulcera_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_ulcera_2.setFont(font)
        self.ck_ulcera_2.setObjectName("ck_ulcera_2")
        self.verticalLayout_3.addWidget(self.ck_ulcera_2)
        self.ck_infeccao_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_infeccao_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_infeccao_2.setFont(font)
        self.ck_infeccao_2.setObjectName("ck_infeccao_2")
        self.verticalLayout_3.addWidget(self.ck_infeccao_2)
        self.ck_inadequada_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_inadequada_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_inadequada_2.setFont(font)
        self.ck_inadequada_2.setObjectName("ck_inadequada_2")
        self.verticalLayout_3.addWidget(self.ck_inadequada_2)
        self.ck_higiene_paciente_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_higiene_paciente_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_higiene_paciente_2.setFont(font)
        self.ck_higiene_paciente_2.setObjectName("ck_higiene_paciente_2")
        self.verticalLayout_3.addWidget(self.ck_higiene_paciente_2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ck_neonato_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_neonato_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_neonato_2.setFont(font)
        self.ck_neonato_2.setObjectName("ck_neonato_2")
        self.verticalLayout_4.addWidget(self.ck_neonato_2)
        self.ck_vaginal_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_vaginal_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_vaginal_2.setFont(font)
        self.ck_vaginal_2.setObjectName("ck_vaginal_2")
        self.verticalLayout_4.addWidget(self.ck_vaginal_2)
        self.ck_cesariana_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_cesariana_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_cesariana_2.setFont(font)
        self.ck_cesariana_2.setObjectName("ck_cesariana_2")
        self.verticalLayout_4.addWidget(self.ck_cesariana_2)
        self.ck_atendimento_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_atendimento_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_atendimento_2.setFont(font)
        self.ck_atendimento_2.setObjectName("ck_atendimento_2")
        self.verticalLayout_4.addWidget(self.ck_atendimento_2)
        self.ck_conflito_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_conflito_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_conflito_2.setFont(font)
        self.ck_conflito_2.setObjectName("ck_conflito_2")
        self.verticalLayout_4.addWidget(self.ck_conflito_2)
        self.ck_evasao_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_evasao_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_evasao_2.setFont(font)
        self.ck_evasao_2.setObjectName("ck_evasao_2")
        self.verticalLayout_4.addWidget(self.ck_evasao_2)
        self.ck_sentinela_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_sentinela_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_sentinela_2.setFont(font)
        self.ck_sentinela_2.setObjectName("ck_sentinela_2")
        self.verticalLayout_4.addWidget(self.ck_sentinela_2)
        self.ck_queimadura_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_queimadura_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.ck_queimadura_2.setFont(font)
        self.ck_queimadura_2.setObjectName("ck_queimadura_2")
        self.verticalLayout_4.addWidget(self.ck_queimadura_2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ck_outros_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.ck_outros_2.setEnabled(False)
        self.ck_outros_2.setObjectName("ck_outros_2")
        self.horizontalLayout_14.addWidget(self.ck_outros_2)
        self.ds_outros = QtWidgets.QLineEdit(self.layoutWidget)
        self.ds_outros.setEnabled(True)
        self.ds_outros.setMinimumSize(QtCore.QSize(800, 31))
        self.ds_outros.setMaximumSize(QtCore.QSize(800, 31))
        self.ds_outros.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.ds_outros.setObjectName("ds_outros")
        self.horizontalLayout_14.addWidget(self.ds_outros)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_74 = QtWidgets.QLabel(self.tab_4)
        self.label_74.setGeometry(QtCore.QRect(342, 24, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(37, 42, 826, 283))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.txt_ocorrencia = QtWidgets.QTextEdit(self.layoutWidget1)
        self.txt_ocorrencia.setEnabled(False)
        self.txt_ocorrencia.setMinimumSize(QtCore.QSize(400, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_ocorrencia.setFont(font)
        self.txt_ocorrencia.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_ocorrencia.setObjectName("txt_ocorrencia")
        self.verticalLayout_17.addWidget(self.txt_ocorrencia)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_75 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.verticalLayout_16.addWidget(self.label_75)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.rb_dano_sim = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_dano_sim.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.rb_dano_sim.setFont(font)
        self.rb_dano_sim.setObjectName("rb_dano_sim")
        self.horizontalLayout_29.addWidget(self.rb_dano_sim)
        self.rb_dano_nao = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_dano_nao.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.rb_dano_nao.setFont(font)
        self.rb_dano_nao.setObjectName("rb_dano_nao")
        self.horizontalLayout_29.addWidget(self.rb_dano_nao)
        self.rb_dano_SI = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_dano_SI.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.rb_dano_SI.setFont(font)
        self.rb_dano_SI.setObjectName("rb_dano_SI")
        self.horizontalLayout_29.addWidget(self.rb_dano_SI)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_16.addLayout(self.verticalLayout_16)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_76 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_76.setMinimumSize(QtCore.QSize(343, 0))
        self.label_76.setMaximumSize(QtCore.QSize(343, 16777215))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.verticalLayout_5.addWidget(self.label_76)
        self.cb_dan = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_dan.setEnabled(False)
        self.cb_dan.setMinimumSize(QtCore.QSize(661, 0))
        self.cb_dan.setMaximumSize(QtCore.QSize(661, 16777215))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.cb_dan.setFont(font)
        self.cb_dan.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_dan.setObjectName("cb_dan")
        self.cb_dan.addItem("")
        self.cb_dan.setItemText(0, "")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.cb_dan.addItem("")
        self.verticalLayout_5.addWidget(self.cb_dan)
        self.horizontalLayout_16.addLayout(self.verticalLayout_5)
        self.verticalLayout_17.addLayout(self.horizontalLayout_16)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget2.setGeometry(QtCore.QRect(39, 3, 814, 325))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_77 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.verticalLayout_22.addWidget(self.label_77)
        self.txt_como = QtWidgets.QTextEdit(self.layoutWidget2)
        self.txt_como.setEnabled(False)
        self.txt_como.setMinimumSize(QtCore.QSize(400, 211))
        self.txt_como.setMaximumSize(QtCore.QSize(400, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_como.setFont(font)
        self.txt_como.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_como.setObjectName("txt_como")
        self.verticalLayout_22.addWidget(self.txt_como)
        self.horizontalLayout_20.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_78 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.verticalLayout_23.addWidget(self.label_78)
        self.txt_acao = QtWidgets.QTextEdit(self.layoutWidget2)
        self.txt_acao.setEnabled(False)
        self.txt_acao.setMinimumSize(QtCore.QSize(400, 211))
        self.txt_acao.setMaximumSize(QtCore.QSize(400, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_acao.setFont(font)
        self.txt_acao.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_acao.setObjectName("txt_acao")
        self.verticalLayout_23.addWidget(self.txt_acao)
        self.horizontalLayout_20.addLayout(self.verticalLayout_23)
        self.verticalLayout_24.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_79 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.verticalLayout_18.addWidget(self.label_79)
        self.txt_quem = QtWidgets.QTextEdit(self.layoutWidget2)
        self.txt_quem.setEnabled(False)
        self.txt_quem.setMinimumSize(QtCore.QSize(400, 50))
        self.txt_quem.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_quem.setFont(font)
        self.txt_quem.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_quem.setObjectName("txt_quem")
        self.verticalLayout_18.addWidget(self.txt_quem)
        self.horizontalLayout_18.addLayout(self.verticalLayout_18)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_80 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(7)
        font.setBold(True)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.verticalLayout_21.addWidget(self.label_80)
        self.txt_identificacao = QtWidgets.QTextEdit(self.layoutWidget2)
        self.txt_identificacao.setEnabled(False)
        self.txt_identificacao.setMinimumSize(QtCore.QSize(400, 50))
        self.txt_identificacao.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_identificacao.setFont(font)
        self.txt_identificacao.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_identificacao.setObjectName("txt_identificacao")
        self.verticalLayout_21.addWidget(self.txt_identificacao)
        self.horizontalLayout_18.addLayout(self.verticalLayout_21)
        self.verticalLayout_24.addLayout(self.horizontalLayout_18)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.verticalLayout_8.addWidget(self.tabWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        spacerItem18 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_3 = QtWidgets.QLabel(self.page_4)
        self.label_3.setGeometry(QtCore.QRect(258, 40, 441, 101))
        self.label_3.setStyleSheet("image: url(:/Imagem/Peixe.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_98 = QtWidgets.QLabel(self.page_4)
        self.label_98.setGeometry(QtCore.QRect(160, 10, 691, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(0,0,0);")
        self.label_98.setAlignment(QtCore.Qt.AlignCenter)
        self.label_98.setObjectName("label_98")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(240, 656, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(False)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.btn_voltar_2 = QtWidgets.QPushButton(self.page_4)
        self.btn_voltar_2.setEnabled(True)
        self.btn_voltar_2.setGeometry(QtCore.QRect(740, 50, 30, 30))
        self.btn_voltar_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar_2.setFont(font)
        self.btn_voltar_2.setStyleSheet("QPushButton#btn_voltar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_2.setText("")
        self.btn_voltar_2.setIcon(icon19)
        self.btn_voltar_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_2.setObjectName("btn_voltar_2")
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_14.setGeometry(QtCore.QRect(850, 60, 126, 61))
        self.groupBox_14.setMinimumSize(QtCore.QSize(0, 61))
        self.groupBox_14.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_14.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_14.setObjectName("groupBox_14")
        self.btn_resumo = QtWidgets.QPushButton(self.groupBox_14)
        self.btn_resumo.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.btn_resumo.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_resumo.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_resumo.setFont(font)
        self.btn_resumo.setStyleSheet("QPushButton#btn_resumo{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumo:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumo:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_resumo.setText("")
        self.btn_resumo.setIcon(icon18)
        self.btn_resumo.setIconSize(QtCore.QSize(24, 24))
        self.btn_resumo.setObjectName("btn_resumo")
        self.widget1 = QtWidgets.QWidget(self.page_4)
        self.widget1.setGeometry(QtCore.QRect(50, 170, 932, 432))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_75 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_75.setMinimumSize(QtCore.QSize(210, 61))
        self.groupBox_75.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_75.setObjectName("groupBox_75")
        self.txt_paciente_3 = QtWidgets.QLineEdit(self.groupBox_75)
        self.txt_paciente_3.setEnabled(True)
        self.txt_paciente_3.setGeometry(QtCore.QRect(80, 20, 110, 31))
        self.txt_paciente_3.setMinimumSize(QtCore.QSize(110, 31))
        self.txt_paciente_3.setMaximumSize(QtCore.QSize(100, 31))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_paciente_3.setFont(font)
        self.txt_paciente_3.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_paciente_3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_paciente_3.setObjectName("txt_paciente_3")
        self.btn_iniciar_investigacao = QtWidgets.QPushButton(self.groupBox_75)
        self.btn_iniciar_investigacao.setGeometry(QtCore.QRect(42, 20, 30, 30))
        self.btn_iniciar_investigacao.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_iniciar_investigacao.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_iniciar_investigacao.setFont(font)
        self.btn_iniciar_investigacao.setStyleSheet("QPushButton#btn_iniciar_investigacao{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_iniciar_investigacao:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_iniciar_investigacao:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_iniciar_investigacao.setText("")
        self.btn_iniciar_investigacao.setIcon(icon4)
        self.btn_iniciar_investigacao.setIconSize(QtCore.QSize(24, 24))
        self.btn_iniciar_investigacao.setObjectName("btn_iniciar_investigacao")
        self.horizontalLayout_5.addWidget(self.groupBox_75)
        self.groupBox_12 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_12.setMinimumSize(QtCore.QSize(210, 61))
        self.groupBox_12.setMaximumSize(QtCore.QSize(210, 61))
        self.groupBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_12.setObjectName("groupBox_12")
        self.btn_buscarInv = QtWidgets.QPushButton(self.groupBox_12)
        self.btn_buscarInv.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.btn_buscarInv.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_buscarInv.setFont(font)
        self.btn_buscarInv.setStyleSheet("QPushButton#btn_buscarInv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_buscarInv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_buscarInv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_buscarInv.setText("")
        self.btn_buscarInv.setIcon(icon14)
        self.btn_buscarInv.setIconSize(QtCore.QSize(24, 24))
        self.btn_buscarInv.setObjectName("btn_buscarInv")
        self.txt_paciente_4 = QtWidgets.QLineEdit(self.groupBox_12)
        self.txt_paciente_4.setEnabled(True)
        self.txt_paciente_4.setGeometry(QtCore.QRect(80, 20, 110, 31))
        self.txt_paciente_4.setMinimumSize(QtCore.QSize(100, 21))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_paciente_4.setFont(font)
        self.txt_paciente_4.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_paciente_4.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_paciente_4.setObjectName("txt_paciente_4")
        self.horizontalLayout_5.addWidget(self.groupBox_12)
        self.groupBox_13 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_13.setMinimumSize(QtCore.QSize(0, 61))
        self.groupBox_13.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_13.setObjectName("groupBox_13")
        self.btn_conclusao_2 = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_conclusao_2.setEnabled(False)
        self.btn_conclusao_2.setGeometry(QtCore.QRect(20, 17, 30, 30))
        self.btn_conclusao_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_conclusao_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_conclusao_2.setFont(font)
        self.btn_conclusao_2.setStyleSheet("QPushButton#btn_conclusao_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_conclusao_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_conclusao_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_conclusao_2.setText("")
        self.btn_conclusao_2.setIcon(icon16)
        self.btn_conclusao_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_conclusao_2.setObjectName("btn_conclusao_2")
        self.btn_cancela_investiga_2 = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_cancela_investiga_2.setGeometry(QtCore.QRect(78, 18, 30, 30))
        self.btn_cancela_investiga_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_cancela_investiga_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_cancela_investiga_2.setFont(font)
        self.btn_cancela_investiga_2.setStyleSheet("QPushButton#btn_cancela_investiga_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_investiga_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_investiga_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_investiga_2.setText("")
        self.btn_cancela_investiga_2.setIcon(icon17)
        self.btn_cancela_investiga_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_investiga_2.setObjectName("btn_cancela_investiga_2")
        self.btn_alterarInv_2 = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_alterarInv_2.setEnabled(False)
        self.btn_alterarInv_2.setGeometry(QtCore.QRect(137, 18, 30, 30))
        self.btn_alterarInv_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_alterarInv_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_alterarInv_2.setFont(font)
        self.btn_alterarInv_2.setStyleSheet("QPushButton#btn_alterarInv_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarInv_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarInv_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterarInv_2.setText("")
        self.btn_alterarInv_2.setIcon(icon13)
        self.btn_alterarInv_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterarInv_2.setObjectName("btn_alterarInv_2")
        self.horizontalLayout_5.addWidget(self.groupBox_13)
        self.groupBox_15 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_15.setMinimumSize(QtCore.QSize(0, 61))
        self.groupBox_15.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_15.setObjectName("groupBox_15")
        self.btn_editarInv = QtWidgets.QPushButton(self.groupBox_15)
        self.btn_editarInv.setGeometry(QtCore.QRect(32, 18, 30, 30))
        self.btn_editarInv.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_editarInv.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_editarInv.setFont(font)
        self.btn_editarInv.setStyleSheet("QPushButton#btn_editarInv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_btn_editarInv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editarInv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_editarInv.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/Imagem/editar-codigo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editarInv.setIcon(icon20)
        self.btn_editarInv.setIconSize(QtCore.QSize(24, 24))
        self.btn_editarInv.setObjectName("btn_editarInv")
        self.horizontalLayout_5.addWidget(self.groupBox_15)
        self.groupBox_23 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_23.setMinimumSize(QtCore.QSize(201, 61))
        self.groupBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_23.setObjectName("groupBox_23")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_23)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.groupBox_23)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.widget1)
        self.tabWidget.setMinimumSize(QtCore.QSize(911, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 11, 882, 357))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_16 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_16.setMinimumSize(QtCore.QSize(871, 51))
        self.groupBox_16.setObjectName("groupBox_16")
        self.txt_paciente = QtWidgets.QLineEdit(self.groupBox_16)
        self.txt_paciente.setEnabled(False)
        self.txt_paciente.setGeometry(QtCore.QRect(5, 21, 871, 21))
        self.txt_paciente.setMinimumSize(QtCore.QSize(200, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_paciente.setFont(font)
        self.txt_paciente.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_paciente.setObjectName("txt_paciente")
        self.verticalLayout_11.addWidget(self.groupBox_16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_17 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_17.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_17.setMaximumSize(QtCore.QSize(435, 51))
        self.groupBox_17.setObjectName("groupBox_17")
        self.txt_pessoas = QtWidgets.QLineEdit(self.groupBox_17)
        self.txt_pessoas.setEnabled(False)
        self.txt_pessoas.setGeometry(QtCore.QRect(7, 15, 421, 31))
        self.txt_pessoas.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas.setFont(font)
        self.txt_pessoas.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas.setObjectName("txt_pessoas")
        self.horizontalLayout_8.addWidget(self.groupBox_17)
        self.groupBox_18 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_18.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_18.setMaximumSize(QtCore.QSize(435, 51))
        self.groupBox_18.setObjectName("groupBox_18")
        self.txt_processos = QtWidgets.QLineEdit(self.groupBox_18)
        self.txt_processos.setEnabled(False)
        self.txt_processos.setGeometry(QtCore.QRect(9, 15, 421, 31))
        self.txt_processos.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_processos.setFont(font)
        self.txt_processos.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_processos.setObjectName("txt_processos")
        self.horizontalLayout_8.addWidget(self.groupBox_18)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.groupBox_19 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_19.setMinimumSize(QtCore.QSize(871, 51))
        self.groupBox_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_19.setObjectName("groupBox_19")
        self.txt_equipamentos = QtWidgets.QLineEdit(self.groupBox_19)
        self.txt_equipamentos.setEnabled(False)
        self.txt_equipamentos.setGeometry(QtCore.QRect(10, 16, 861, 31))
        self.txt_equipamentos.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_equipamentos.setFont(font)
        self.txt_equipamentos.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_equipamentos.setObjectName("txt_equipamentos")
        self.verticalLayout_11.addWidget(self.groupBox_19)
        self.groupBox_20 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_20.setMinimumSize(QtCore.QSize(871, 51))
        self.groupBox_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_20.setObjectName("groupBox_20")
        self.txt_ambiente = QtWidgets.QLineEdit(self.groupBox_20)
        self.txt_ambiente.setEnabled(False)
        self.txt_ambiente.setGeometry(QtCore.QRect(10, 15, 861, 31))
        self.txt_ambiente.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_ambiente.setFont(font)
        self.txt_ambiente.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_ambiente.setObjectName("txt_ambiente")
        self.verticalLayout_11.addWidget(self.groupBox_20)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_21 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_21.setMinimumSize(QtCore.QSize(435, 121))
        self.groupBox_21.setObjectName("groupBox_21")
        self.txt_observacao_2 = QtWidgets.QTextEdit(self.groupBox_21)
        self.txt_observacao_2.setEnabled(False)
        self.txt_observacao_2.setGeometry(QtCore.QRect(7, 16, 420, 100))
        self.txt_observacao_2.setMinimumSize(QtCore.QSize(355, 100))
        self.txt_observacao_2.setMaximumSize(QtCore.QSize(420, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_observacao_2.setFont(font)
        self.txt_observacao_2.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_observacao_2.setObjectName("txt_observacao_2")
        self.horizontalLayout_3.addWidget(self.groupBox_21)
        self.groupBox_22 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_22.setMinimumSize(QtCore.QSize(435, 121))
        self.groupBox_22.setObjectName("groupBox_22")
        self.txt_recomendacao_4 = QtWidgets.QTextEdit(self.groupBox_22)
        self.txt_recomendacao_4.setEnabled(False)
        self.txt_recomendacao_4.setGeometry(QtCore.QRect(14, 16, 410, 100))
        self.txt_recomendacao_4.setMinimumSize(QtCore.QSize(355, 100))
        self.txt_recomendacao_4.setMaximumSize(QtCore.QSize(410, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_recomendacao_4.setFont(font)
        self.txt_recomendacao_4.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_recomendacao_4.setObjectName("txt_recomendacao_4")
        self.horizontalLayout_3.addWidget(self.groupBox_22)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_28 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_28.setGeometry(QtCore.QRect(20, 129, 435, 51))
        self.groupBox_28.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_28.setObjectName("groupBox_28")
        self.txt_pessoas_12 = QtWidgets.QLineEdit(self.groupBox_28)
        self.txt_pessoas_12.setEnabled(False)
        self.txt_pessoas_12.setGeometry(QtCore.QRect(10, 16, 411, 31))
        self.txt_pessoas_12.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas_12.setFont(font)
        self.txt_pessoas_12.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas_12.setObjectName("txt_pessoas_12")
        self.groupBox_29 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_29.setGeometry(QtCore.QRect(20, 182, 881, 91))
        self.groupBox_29.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_29.setObjectName("groupBox_29")
        self.txt_recomendacao_3 = QtWidgets.QTextEdit(self.groupBox_29)
        self.txt_recomendacao_3.setEnabled(False)
        self.txt_recomendacao_3.setGeometry(QtCore.QRect(6, 27, 871, 57))
        self.txt_recomendacao_3.setMinimumSize(QtCore.QSize(871, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_recomendacao_3.setFont(font)
        self.txt_recomendacao_3.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_recomendacao_3.setObjectName("txt_recomendacao_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 10, 880, 114))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_24 = QtWidgets.QGroupBox(self.layoutWidget4)
        self.groupBox_24.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_24.setObjectName("groupBox_24")
        self.txt_pessoas_8 = QtWidgets.QLineEdit(self.groupBox_24)
        self.txt_pessoas_8.setEnabled(False)
        self.txt_pessoas_8.setGeometry(QtCore.QRect(10, 17, 411, 31))
        self.txt_pessoas_8.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas_8.setFont(font)
        self.txt_pessoas_8.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas_8.setObjectName("txt_pessoas_8")
        self.horizontalLayout_9.addWidget(self.groupBox_24)
        self.groupBox_25 = QtWidgets.QGroupBox(self.layoutWidget4)
        self.groupBox_25.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_25.setObjectName("groupBox_25")
        self.txt_pessoas_9 = QtWidgets.QLineEdit(self.groupBox_25)
        self.txt_pessoas_9.setEnabled(False)
        self.txt_pessoas_9.setGeometry(QtCore.QRect(10, 18, 411, 31))
        self.txt_pessoas_9.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas_9.setFont(font)
        self.txt_pessoas_9.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas_9.setObjectName("txt_pessoas_9")
        self.horizontalLayout_9.addWidget(self.groupBox_25)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.groupBox_26 = QtWidgets.QGroupBox(self.layoutWidget4)
        self.groupBox_26.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_26.setObjectName("groupBox_26")
        self.txt_pessoas_11 = QtWidgets.QLineEdit(self.groupBox_26)
        self.txt_pessoas_11.setEnabled(False)
        self.txt_pessoas_11.setGeometry(QtCore.QRect(10, 16, 411, 31))
        self.txt_pessoas_11.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas_11.setFont(font)
        self.txt_pessoas_11.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas_11.setObjectName("txt_pessoas_11")
        self.horizontalLayout_13.addWidget(self.groupBox_26)
        self.groupBox_27 = QtWidgets.QGroupBox(self.layoutWidget4)
        self.groupBox_27.setMinimumSize(QtCore.QSize(435, 51))
        self.groupBox_27.setObjectName("groupBox_27")
        self.txt_pessoas_10 = QtWidgets.QLineEdit(self.groupBox_27)
        self.txt_pessoas_10.setEnabled(False)
        self.txt_pessoas_10.setGeometry(QtCore.QRect(12, 16, 411, 31))
        self.txt_pessoas_10.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txt_pessoas_10.setFont(font)
        self.txt_pessoas_10.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_pessoas_10.setObjectName("txt_pessoas_10")
        self.horizontalLayout_13.addWidget(self.groupBox_27)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_12.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_4)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.btn_Spdf_2 = QtWidgets.QPushButton(self.page_12)
        self.btn_Spdf_2.setEnabled(False)
        self.btn_Spdf_2.setGeometry(QtCore.QRect(950, 620, 30, 30))
        self.btn_Spdf_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_Spdf_2.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_Spdf_2.setStyleSheet("QPushButton#btn_Spdf{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_Spdf:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_Spdf:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_Spdf_2.setText("")
        self.btn_Spdf_2.setIcon(icon15)
        self.btn_Spdf_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_Spdf_2.setObjectName("btn_Spdf_2")
        self.label_18 = QtWidgets.QLabel(self.page_12)
        self.label_18.setGeometry(QtCore.QRect(350, 660, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(False)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.layoutWidget5 = QtWidgets.QWidget(self.page_12)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 60, 993, 550))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.groupBox_61 = QtWidgets.QGroupBox(self.layoutWidget5)
        self.groupBox_61.setMinimumSize(QtCore.QSize(991, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_61.setFont(font)
        self.groupBox_61.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_61.setObjectName("groupBox_61")
        self.btn_voltar_3 = QtWidgets.QPushButton(self.groupBox_61)
        self.btn_voltar_3.setEnabled(True)
        self.btn_voltar_3.setGeometry(QtCore.QRect(930, 50, 30, 30))
        self.btn_voltar_3.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar_3.setFont(font)
        self.btn_voltar_3.setStyleSheet("QPushButton#btn_voltar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_3.setText("")
        self.btn_voltar_3.setIcon(icon19)
        self.btn_voltar_3.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_3.setObjectName("btn_voltar_3")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_61)
        self.layoutWidget6.setGeometry(QtCore.QRect(84, 20, 822, 93))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_136 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_136.setFont(font)
        self.label_136.setStyleSheet("color:rgb(0,0,0);")
        self.label_136.setObjectName("label_136")
        self.horizontalLayout_19.addWidget(self.label_136)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(441, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_19.addWidget(self.lineEdit_6)
        self.btn_consultarNoti_2 = QtWidgets.QPushButton(self.layoutWidget6)
        self.btn_consultarNoti_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_consultarNoti_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_consultarNoti_2.setFont(font)
        self.btn_consultarNoti_2.setStyleSheet("QPushButton#btn_consultarNoti_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultarNoti_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultarNoti_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultarNoti_2.setText("")
        self.btn_consultarNoti_2.setIcon(icon14)
        self.btn_consultarNoti_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultarNoti_2.setObjectName("btn_consultarNoti_2")
        self.horizontalLayout_19.addWidget(self.btn_consultarNoti_2)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_19)
        self.groupBox_37 = QtWidgets.QGroupBox(self.layoutWidget6)
        self.groupBox_37.setMinimumSize(QtCore.QSize(281, 91))
        self.groupBox_37.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_37.setObjectName("groupBox_37")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_37)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 108, 62))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.radioButton_10 = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioButton_10.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_35.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioButton_11.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_35.addWidget(self.radioButton_11)
        self.layoutWidget_42 = QtWidgets.QWidget(self.groupBox_37)
        self.layoutWidget_42.setGeometry(QtCore.QRect(140, 20, 113, 62))
        self.layoutWidget_42.setObjectName("layoutWidget_42")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.layoutWidget_42)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.radioButton_12 = QtWidgets.QRadioButton(self.layoutWidget_42)
        self.radioButton_12.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_36.addWidget(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.layoutWidget_42)
        self.radioButton_13.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.verticalLayout_36.addWidget(self.radioButton_13)
        self.horizontalLayout_28.addWidget(self.groupBox_37)
        self.verticalLayout_25.addWidget(self.groupBox_61)
        self.tb_consulta_4 = QtWidgets.QTableWidget(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_consulta_4.sizePolicy().hasHeightForWidth())
        self.tb_consulta_4.setSizePolicy(sizePolicy)
        self.tb_consulta_4.setMinimumSize(QtCore.QSize(991, 421))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(True)
        self.tb_consulta_4.setFont(font)
        self.tb_consulta_4.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"\n"
"\n"
"\n"
"")
        self.tb_consulta_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_consulta_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tb_consulta_4.setAutoScrollMargin(21)
        self.tb_consulta_4.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tb_consulta_4.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tb_consulta_4.setGridStyle(QtCore.Qt.NoPen)
        self.tb_consulta_4.setObjectName("tb_consulta_4")
        self.tb_consulta_4.setColumnCount(8)
        self.tb_consulta_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_consulta_4.setHorizontalHeaderItem(7, item)
        self.tb_consulta_4.horizontalHeader().setVisible(True)
        self.tb_consulta_4.horizontalHeader().setDefaultSectionSize(125)
        self.verticalLayout_25.addWidget(self.tb_consulta_4)
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.groupBox_38 = QtWidgets.QGroupBox(self.page_13)
        self.groupBox_38.setGeometry(QtCore.QRect(90, 0, 821, 681))
        self.groupBox_38.setMinimumSize(QtCore.QSize(821, 681))
        self.groupBox_38.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_38.setObjectName("groupBox_38")
        self.btn_voltar_4 = QtWidgets.QPushButton(self.groupBox_38)
        self.btn_voltar_4.setEnabled(True)
        self.btn_voltar_4.setGeometry(QtCore.QRect(770, 50, 30, 30))
        self.btn_voltar_4.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar_4.setFont(font)
        self.btn_voltar_4.setStyleSheet("QPushButton#btn_voltar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_4.setText("")
        self.btn_voltar_4.setIcon(icon19)
        self.btn_voltar_4.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_4.setObjectName("btn_voltar_4")
        self.layoutWidget7 = QtWidgets.QWidget(self.groupBox_38)
        self.layoutWidget7.setGeometry(QtCore.QRect(201, 93, 445, 569))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.groupBox_39 = QtWidgets.QGroupBox(self.layoutWidget7)
        self.groupBox_39.setMinimumSize(QtCore.QSize(441, 80))
        self.groupBox_39.setObjectName("groupBox_39")
        self.txt_cadnome_4 = QtWidgets.QLineEdit(self.groupBox_39)
        self.txt_cadnome_4.setEnabled(False)
        self.txt_cadnome_4.setGeometry(QtCore.QRect(10, 30, 421, 31))
        self.txt_cadnome_4.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome_4.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")
        self.txt_cadnome_4.setText("")
        self.txt_cadnome_4.setObjectName("txt_cadnome_4")
        self.verticalLayout_38.addWidget(self.groupBox_39)
        self.groupBox_40 = QtWidgets.QGroupBox(self.layoutWidget7)
        self.groupBox_40.setMinimumSize(QtCore.QSize(441, 80))
        self.groupBox_40.setObjectName("groupBox_40")
        self.txt_cadnome_5 = QtWidgets.QLineEdit(self.groupBox_40)
        self.txt_cadnome_5.setEnabled(False)
        self.txt_cadnome_5.setGeometry(QtCore.QRect(10, 30, 421, 31))
        self.txt_cadnome_5.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome_5.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")
        self.txt_cadnome_5.setText("")
        self.txt_cadnome_5.setObjectName("txt_cadnome_5")
        self.verticalLayout_38.addWidget(self.groupBox_40)
        self.groupBox_42 = QtWidgets.QGroupBox(self.layoutWidget7)
        self.groupBox_42.setMinimumSize(QtCore.QSize(441, 80))
        self.groupBox_42.setObjectName("groupBox_42")
        self.txt_cadnome_6 = QtWidgets.QLineEdit(self.groupBox_42)
        self.txt_cadnome_6.setEnabled(False)
        self.txt_cadnome_6.setGeometry(QtCore.QRect(10, 30, 421, 31))
        self.txt_cadnome_6.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome_6.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")
        self.txt_cadnome_6.setText("")
        self.txt_cadnome_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_cadnome_6.setObjectName("txt_cadnome_6")
        self.verticalLayout_38.addWidget(self.groupBox_42)
        self.groupBox_41 = QtWidgets.QGroupBox(self.layoutWidget7)
        self.groupBox_41.setMinimumSize(QtCore.QSize(441, 80))
        self.groupBox_41.setObjectName("groupBox_41")
        self.cb_outros_4 = QtWidgets.QComboBox(self.groupBox_41)
        self.cb_outros_4.setEnabled(True)
        self.cb_outros_4.setGeometry(QtCore.QRect(80, 40, 300, 29))
        self.cb_outros_4.setMinimumSize(QtCore.QSize(300, 0))
        self.cb_outros_4.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.cb_outros_4.setObjectName("cb_outros_4")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.setItemText(0, "")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.cb_outros_4.addItem("")
        self.verticalLayout_38.addWidget(self.groupBox_41)
        self.verticalLayout_39.addLayout(self.verticalLayout_38)
        self.groupBox_43 = QtWidgets.QGroupBox(self.layoutWidget7)
        self.groupBox_43.setMinimumSize(QtCore.QSize(0, 221))
        self.groupBox_43.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_43.setObjectName("groupBox_43")
        self.groupBox_44 = QtWidgets.QGroupBox(self.groupBox_43)
        self.groupBox_44.setGeometry(QtCore.QRect(10, 20, 420, 80))
        self.groupBox_44.setMinimumSize(QtCore.QSize(420, 80))
        self.groupBox_44.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox_44.setObjectName("groupBox_44")
        self.layoutWidget8 = QtWidgets.QWidget(self.groupBox_44)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 30, 389, 32))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.txt_consultaUser_2 = QtWidgets.QLineEdit(self.layoutWidget8)
        self.txt_consultaUser_2.setMinimumSize(QtCore.QSize(351, 22))
        self.txt_consultaUser_2.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:3px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px")
        self.txt_consultaUser_2.setObjectName("txt_consultaUser_2")
        self.horizontalLayout_59.addWidget(self.txt_consultaUser_2)
        self.btn_consultaUser_2 = QtWidgets.QPushButton(self.layoutWidget8)
        self.btn_consultaUser_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_consultaUser_2.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_consultaUser_2.setStyleSheet("QPushButton#btn_consultaUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultaUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultaUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultaUser_2.setText("")
        self.btn_consultaUser_2.setIcon(icon14)
        self.btn_consultaUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultaUser_2.setObjectName("btn_consultaUser_2")
        self.horizontalLayout_59.addWidget(self.btn_consultaUser_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_43)
        self.tableWidget_2.setGeometry(QtCore.QRect(1, 110, 441, 101))
        self.tableWidget_2.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"\n"
"padding-bottom: 7px")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(146)
        self.verticalLayout_39.addWidget(self.groupBox_43)
        self.layoutWidget9 = QtWidgets.QWidget(self.groupBox_38)
        self.layoutWidget9.setGeometry(QtCore.QRect(521, 25, 124, 63))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.groupBox_48 = QtWidgets.QGroupBox(self.layoutWidget9)
        self.groupBox_48.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_48.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_48.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_48.setObjectName("groupBox_48")
        self.btn_salvaUser_2 = QtWidgets.QPushButton(self.groupBox_48)
        self.btn_salvaUser_2.setEnabled(False)
        self.btn_salvaUser_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_salvaUser_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_salvaUser_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_salvaUser_2.setFont(font)
        self.btn_salvaUser_2.setStyleSheet("QPushButton#btn_salvaUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salvaUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salvaUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salvaUser_2.setText("")
        self.btn_salvaUser_2.setIcon(icon16)
        self.btn_salvaUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_salvaUser_2.setObjectName("btn_salvaUser_2")
        self.horizontalLayout_60.addWidget(self.groupBox_48)
        self.groupBox_49 = QtWidgets.QGroupBox(self.layoutWidget9)
        self.groupBox_49.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_49.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_49.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_49.setObjectName("groupBox_49")
        self.btn_cancelaUser_2 = QtWidgets.QPushButton(self.groupBox_49)
        self.btn_cancelaUser_2.setEnabled(False)
        self.btn_cancelaUser_2.setGeometry(QtCore.QRect(17, 20, 30, 30))
        self.btn_cancelaUser_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_cancelaUser_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_cancelaUser_2.setFont(font)
        self.btn_cancelaUser_2.setStyleSheet("QPushButton#btn_cancelaUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancelaUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancelaUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancelaUser_2.setText("")
        self.btn_cancelaUser_2.setIcon(icon17)
        self.btn_cancelaUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancelaUser_2.setObjectName("btn_cancelaUser_2")
        self.horizontalLayout_60.addWidget(self.groupBox_49)
        self.layoutWidget10 = QtWidgets.QWidget(self.groupBox_38)
        self.layoutWidget10.setGeometry(QtCore.QRect(202, 26, 170, 63))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.groupBox_45 = QtWidgets.QGroupBox(self.layoutWidget10)
        self.groupBox_45.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_45.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_45.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_45.setObjectName("groupBox_45")
        self.btn_novoUser_2 = QtWidgets.QPushButton(self.groupBox_45)
        self.btn_novoUser_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.btn_novoUser_2.sizePolicy().hasHeightForWidth())
        self.btn_novoUser_2.setSizePolicy(sizePolicy)
        self.btn_novoUser_2.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_novoUser_2.setFont(font)
        self.btn_novoUser_2.setStyleSheet("QPushButton#btn_novoUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novoUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novoUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_novoUser_2.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/Imagem/adicionar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_novoUser_2.setIcon(icon21)
        self.btn_novoUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_novoUser_2.setObjectName("btn_novoUser_2")
        self.horizontalLayout_61.addWidget(self.groupBox_45)
        self.groupBox_46 = QtWidgets.QGroupBox(self.layoutWidget10)
        self.groupBox_46.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_46.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_46.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_46.setObjectName("groupBox_46")
        self.btn_editaUser_2 = QtWidgets.QPushButton(self.groupBox_46)
        self.btn_editaUser_2.setEnabled(False)
        self.btn_editaUser_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_editaUser_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_editaUser_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_editaUser_2.setFont(font)
        self.btn_editaUser_2.setStyleSheet("QPushButton#btn_editaUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editaUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editaUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_editaUser_2.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/Imagem/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editaUser_2.setIcon(icon22)
        self.btn_editaUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_editaUser_2.setObjectName("btn_editaUser_2")
        self.horizontalLayout_61.addWidget(self.groupBox_46)
        self.groupBox_47 = QtWidgets.QGroupBox(self.layoutWidget10)
        self.groupBox_47.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_47.setMaximumSize(QtCore.QSize(16777215, 61))
        self.groupBox_47.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_47.setObjectName("groupBox_47")
        self.btn_alterarUser_2 = QtWidgets.QPushButton(self.groupBox_47)
        self.btn_alterarUser_2.setEnabled(False)
        self.btn_alterarUser_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_alterarUser_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_alterarUser_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_alterarUser_2.setFont(font)
        self.btn_alterarUser_2.setStyleSheet("QPushButton#btn_alterarUser_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarUser_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarUser_2:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterarUser_2.setText("")
        self.btn_alterarUser_2.setIcon(icon13)
        self.btn_alterarUser_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterarUser_2.setObjectName("btn_alterarUser_2")
        self.horizontalLayout_61.addWidget(self.groupBox_47)
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.groupBox_50 = QtWidgets.QGroupBox(self.page_14)
        self.groupBox_50.setGeometry(QtCore.QRect(241, 138, 511, 321))
        self.groupBox_50.setMinimumSize(QtCore.QSize(511, 241))
        self.groupBox_50.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_50.setObjectName("groupBox_50")
        self.layoutWidget11 = QtWidgets.QWidget(self.groupBox_50)
        self.layoutWidget11.setGeometry(QtCore.QRect(60, 100, 397, 201))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.layoutWidget11)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget11)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_62.addWidget(self.label_19)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget11)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(351, 0))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_62.addWidget(self.lineEdit_7)
        self.verticalLayout_40.addLayout(self.horizontalLayout_62)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.layoutWidget11)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(391, 151))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(391)
        self.verticalLayout_40.addWidget(self.tableWidget_3)
        self.layoutWidget12 = QtWidgets.QWidget(self.groupBox_50)
        self.layoutWidget12.setGeometry(QtCore.QRect(50, 20, 167, 63))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.groupBox_51 = QtWidgets.QGroupBox(self.layoutWidget12)
        self.groupBox_51.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_51.setMaximumSize(QtCore.QSize(51, 61))
        self.groupBox_51.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_51.setObjectName("groupBox_51")
        self.btn_novo_setor = QtWidgets.QPushButton(self.groupBox_51)
        self.btn_novo_setor.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_novo_setor.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_novo_setor.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_novo_setor.setStyleSheet("QPushButton#btn_novo_setor{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novo_setor:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novo_setor:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_novo_setor.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/Imagem/grafico-de-setores (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_novo_setor.setIcon(icon23)
        self.btn_novo_setor.setIconSize(QtCore.QSize(24, 24))
        self.btn_novo_setor.setObjectName("btn_novo_setor")
        self.horizontalLayout_63.addWidget(self.groupBox_51)
        self.groupBox_52 = QtWidgets.QGroupBox(self.layoutWidget12)
        self.groupBox_52.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_52.setMaximumSize(QtCore.QSize(51, 61))
        self.groupBox_52.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_52.setObjectName("groupBox_52")
        self.btn_edita_setor = QtWidgets.QPushButton(self.groupBox_52)
        self.btn_edita_setor.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_edita_setor.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_edita_setor.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_edita_setor.setStyleSheet("QPushButton#btn_edita_setor{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_edita_setor:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_edita_setor:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_edita_setor.setText("")
        self.btn_edita_setor.setIcon(icon20)
        self.btn_edita_setor.setIconSize(QtCore.QSize(24, 24))
        self.btn_edita_setor.setObjectName("btn_edita_setor")
        self.horizontalLayout_63.addWidget(self.groupBox_52)
        self.groupBox_55 = QtWidgets.QGroupBox(self.layoutWidget12)
        self.groupBox_55.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_55.setMaximumSize(QtCore.QSize(51, 61))
        self.groupBox_55.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_55.setObjectName("groupBox_55")
        self.btn_conf_alterar = QtWidgets.QPushButton(self.groupBox_55)
        self.btn_conf_alterar.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_conf_alterar.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_conf_alterar.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_conf_alterar.setStyleSheet("QPushButton#btn_conf_alterar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_conf_alterar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_conf_alterar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_conf_alterar.setText("")
        self.btn_conf_alterar.setIcon(icon13)
        self.btn_conf_alterar.setIconSize(QtCore.QSize(24, 24))
        self.btn_conf_alterar.setObjectName("btn_conf_alterar")
        self.horizontalLayout_63.addWidget(self.groupBox_55)
        self.layoutWidget13 = QtWidgets.QWidget(self.groupBox_50)
        self.layoutWidget13.setGeometry(QtCore.QRect(370, 20, 110, 63))
        self.layoutWidget13.setObjectName("layoutWidget13")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.groupBox_53 = QtWidgets.QGroupBox(self.layoutWidget13)
        self.groupBox_53.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_53.setMaximumSize(QtCore.QSize(51, 61))
        self.groupBox_53.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_53.setObjectName("groupBox_53")
        self.btn_salvar_setor = QtWidgets.QPushButton(self.groupBox_53)
        self.btn_salvar_setor.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_salvar_setor.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_salvar_setor.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_salvar_setor.setStyleSheet("QPushButton#btn_salvar_setor{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salvar_setor:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salvar_setor:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salvar_setor.setText("")
        self.btn_salvar_setor.setIcon(icon16)
        self.btn_salvar_setor.setIconSize(QtCore.QSize(24, 24))
        self.btn_salvar_setor.setObjectName("btn_salvar_setor")
        self.horizontalLayout_64.addWidget(self.groupBox_53)
        self.groupBox_54 = QtWidgets.QGroupBox(self.layoutWidget13)
        self.groupBox_54.setMinimumSize(QtCore.QSize(51, 61))
        self.groupBox_54.setMaximumSize(QtCore.QSize(51, 61))
        self.groupBox_54.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_54.setObjectName("groupBox_54")
        self.btn_cancela_setor = QtWidgets.QPushButton(self.groupBox_54)
        self.btn_cancela_setor.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.btn_cancela_setor.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_cancela_setor.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_cancela_setor.setStyleSheet("QPushButton#btn_cancela_setor{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_setor:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_setor:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_setor.setText("")
        self.btn_cancela_setor.setIcon(icon17)
        self.btn_cancela_setor.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_setor.setObjectName("btn_cancela_setor")
        self.horizontalLayout_64.addWidget(self.groupBox_54)
        self.label_20 = QtWidgets.QLabel(self.page_14)
        self.label_20.setGeometry(QtCore.QRect(450, 40, 91, 81))
        self.label_20.setMinimumSize(QtCore.QSize(91, 81))
        self.label_20.setStyleSheet("image: url(:/Imagem/composto.png);")
        self.label_20.setText("")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_14)
        self.label_21.setGeometry(QtCore.QRect(330, 660, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(False)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.btn_voltar_5 = QtWidgets.QPushButton(self.page_14)
        self.btn_voltar_5.setEnabled(True)
        self.btn_voltar_5.setGeometry(QtCore.QRect(720, 100, 30, 30))
        self.btn_voltar_5.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar_5.setFont(font)
        self.btn_voltar_5.setStyleSheet("QPushButton#btn_voltar_5{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar_5:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar_5:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_5.setText("")
        self.btn_voltar_5.setIcon(icon19)
        self.btn_voltar_5.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_5.setObjectName("btn_voltar_5")
        self.stackedWidget.addWidget(self.page_14)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.groupBox_56 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_56.setGeometry(QtCore.QRect(171, 138, 651, 421))
        self.groupBox_56.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_56.setObjectName("groupBox_56")
        self.groupBox_60 = QtWidgets.QGroupBox(self.groupBox_56)
        self.groupBox_60.setGeometry(QtCore.QRect(534, 37, 58, 71))
        self.groupBox_60.setMinimumSize(QtCore.QSize(58, 61))
        self.groupBox_60.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_60.setObjectName("groupBox_60")
        self.btn_pesquisa_email = QtWidgets.QPushButton(self.groupBox_60)
        self.btn_pesquisa_email.setGeometry(QtCore.QRect(11, 25, 30, 30))
        self.btn_pesquisa_email.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_pesquisa_email.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_pesquisa_email.setStyleSheet("QPushButton#btn_pesquisa_email{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisa_email:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisa_email:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisa_email.setText("")
        self.btn_pesquisa_email.setIcon(icon14)
        self.btn_pesquisa_email.setIconSize(QtCore.QSize(24, 24))
        self.btn_pesquisa_email.setObjectName("btn_pesquisa_email")
        self.layoutWidget14 = QtWidgets.QWidget(self.groupBox_56)
        self.layoutWidget14.setGeometry(QtCore.QRect(60, 110, 533, 263))
        self.layoutWidget14.setObjectName("layoutWidget14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget14)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget14)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget14)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(431, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        self.verticalLayout_15.addLayout(self.horizontalLayout_10)
        self.groupBox_57 = QtWidgets.QGroupBox(self.layoutWidget14)
        self.groupBox_57.setMinimumSize(QtCore.QSize(531, 231))
        self.groupBox_57.setObjectName("groupBox_57")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_57)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 481, 161))
        self.tableWidget.setMinimumSize(QtCore.QSize(481, 61))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(477)
        self.verticalLayout_15.addWidget(self.groupBox_57)
        self.layoutWidget15 = QtWidgets.QWidget(self.groupBox_56)
        self.layoutWidget15.setGeometry(QtCore.QRect(61, 40, 188, 63))
        self.layoutWidget15.setObjectName("layoutWidget15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_58 = QtWidgets.QGroupBox(self.layoutWidget15)
        self.groupBox_58.setMinimumSize(QtCore.QSize(58, 61))
        self.groupBox_58.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_58.setObjectName("groupBox_58")
        self.btn_novoEmail = QtWidgets.QPushButton(self.groupBox_58)
        self.btn_novoEmail.setGeometry(QtCore.QRect(13, 26, 30, 30))
        self.btn_novoEmail.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_novoEmail.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_novoEmail.setStyleSheet("QPushButton#btn_novoEmail{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novoEmail:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novoEmail:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_novoEmail.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/Imagem/nova-mensagem (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_novoEmail.setIcon(icon24)
        self.btn_novoEmail.setIconSize(QtCore.QSize(24, 24))
        self.btn_novoEmail.setObjectName("btn_novoEmail")
        self.horizontalLayout_11.addWidget(self.groupBox_58)
        self.groupBox_59 = QtWidgets.QGroupBox(self.layoutWidget15)
        self.groupBox_59.setMinimumSize(QtCore.QSize(58, 61))
        self.groupBox_59.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_59.setObjectName("groupBox_59")
        self.btn_alterar_email = QtWidgets.QPushButton(self.groupBox_59)
        self.btn_alterar_email.setGeometry(QtCore.QRect(10, 24, 30, 30))
        self.btn_alterar_email.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_alterar_email.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_alterar_email.setStyleSheet("QPushButton#btn_alterar_email{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterar_email:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterar_email:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterar_email.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/Imagem/papel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_alterar_email.setIcon(icon25)
        self.btn_alterar_email.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterar_email.setObjectName("btn_alterar_email")
        self.horizontalLayout_11.addWidget(self.groupBox_59)
        self.groupBox_74 = QtWidgets.QGroupBox(self.layoutWidget15)
        self.groupBox_74.setMinimumSize(QtCore.QSize(58, 61))
        self.groupBox_74.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_74.setObjectName("groupBox_74")
        self.btn_excluir_email = QtWidgets.QPushButton(self.groupBox_74)
        self.btn_excluir_email.setGeometry(QtCore.QRect(13, 24, 30, 30))
        self.btn_excluir_email.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_excluir_email.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_excluir_email.setStyleSheet("QPushButton#btn_alterar_email{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterar_email:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterar_email:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_excluir_email.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/Imagem/remover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_excluir_email.setIcon(icon26)
        self.btn_excluir_email.setIconSize(QtCore.QSize(24, 24))
        self.btn_excluir_email.setObjectName("btn_excluir_email")
        self.horizontalLayout_11.addWidget(self.groupBox_74)
        self.label_11 = QtWidgets.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(418, 28, 141, 101))
        self.label_11.setStyleSheet("image: url(:/Imagem/marketing-de-email.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.btn_voltar_6 = QtWidgets.QPushButton(self.page_5)
        self.btn_voltar_6.setEnabled(True)
        self.btn_voltar_6.setGeometry(QtCore.QRect(788, 98, 30, 30))
        self.btn_voltar_6.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_voltar_6.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_voltar_6.setFont(font)
        self.btn_voltar_6.setStyleSheet("QPushButton#btn_voltar_6{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_voltar_6:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_voltar_6:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_voltar_6.setText("")
        self.btn_voltar_6.setIcon(icon19)
        self.btn_voltar_6.setIconSize(QtCore.QSize(24, 24))
        self.btn_voltar_6.setObjectName("btn_voltar_6")
        self.label_22 = QtWidgets.QLabel(self.page_5)
        self.label_22.setGeometry(QtCore.QRect(320, 660, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(False)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.page_5)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_3 = QtWidgets.QFrame(self.page_7)
        self.frame_3.setGeometry(QtCore.QRect(239, 80, 281, 511))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("border-top-left-radius:50px;\n"
"image: url(:/Imagens/Fundo_login.jpg);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(13, 110, 261, 351))
        self.label_12.setStyleSheet("image: url(:/Imagens/Dia-da-Qualidadecorte (1).png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(51, 28, 179, 70))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(108, 52, 19);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_26.addWidget(self.label_13)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        font.setBold(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(108, 52, 19);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_26.addWidget(self.label_23)
        self.frame_4 = QtWidgets.QFrame(self.page_7)
        self.frame_4.setGeometry(QtCore.QRect(520, 80, 281, 531))
        self.frame_4.setStyleSheet("border-bottom-right-radius:50px;\n"
"background-color: rgb(244, 244, 244);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_9 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_9.setGeometry(QtCore.QRect(40, 176, 204, 105))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.txt_usuario = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.txt_usuario.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_usuario.setText("")
        self.txt_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_usuario.setObjectName("txt_usuario")
        self.verticalLayout_28.addWidget(self.txt_usuario)
        self.txt_senha = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.txt_senha.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_senha.setText("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.verticalLayout_28.addWidget(self.txt_senha)
        self.verticalLayout_27.addLayout(self.verticalLayout_28)
        self.cb_empresa = QtWidgets.QComboBox(self.layoutWidget_9)
        self.cb_empresa.setMinimumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.cb_empresa.setFont(font)
        self.cb_empresa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_empresa.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_empresa.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_empresa.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cb_empresa.setPlaceholderText("")
        self.cb_empresa.setObjectName("cb_empresa")
        self.cb_empresa.addItem("")
        self.cb_empresa.addItem("")
        self.verticalLayout_27.addWidget(self.cb_empresa)
        self.btn_anonimo = QtWidgets.QPushButton(self.frame_4)
        self.btn_anonimo.setGeometry(QtCore.QRect(100, 390, 100, 30))
        self.btn_anonimo.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_anonimo.setFont(font)
        self.btn_anonimo.setStyleSheet("QPushButton#btn_anonimo{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_anonimo:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_anonimo:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_anonimo.setObjectName("btn_anonimo")
        self.layoutWidget_10 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_10.setGeometry(QtCore.QRect(90, 295, 102, 68))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.btn_login_rnc = QtWidgets.QPushButton(self.layoutWidget_10)
        self.btn_login_rnc.setEnabled(False)
        self.btn_login_rnc.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_login_rnc.setFont(font)
        self.btn_login_rnc.setStyleSheet("QPushButton#btn_login_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_login_rnc.setObjectName("btn_login_rnc")
        self.verticalLayout_29.addWidget(self.btn_login_rnc)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(70, 5, 141, 151))
        self.label_14.setStyleSheet("image: url(:/Imagens/password.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.btn_SairApp = QtWidgets.QPushButton(self.frame_4)
        self.btn_SairApp.setEnabled(False)
        self.btn_SairApp.setGeometry(QtCore.QRect(100, 480, 100, 30))
        self.btn_SairApp.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_SairApp.setFont(font)
        self.btn_SairApp.setStyleSheet("QPushButton#btn_SairApp{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_SairApp:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_SairApp:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_SairApp.setObjectName("btn_SairApp")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.layoutWidget16 = QtWidgets.QWidget(self.page_8)
        self.layoutWidget16.setGeometry(QtCore.QRect(111, 60, 795, 53))
        self.layoutWidget16.setObjectName("layoutWidget16")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.layoutWidget16)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.groupBox_129 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_129.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_129.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_129.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_129.setObjectName("groupBox_129")
        self.btn_dashboard_2 = QtWidgets.QPushButton(self.groupBox_129)
        self.btn_dashboard_2.setEnabled(False)
        self.btn_dashboard_2.setGeometry(QtCore.QRect(23, 17, 30, 30))
        self.btn_dashboard_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_dashboard_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.btn_dashboard_2.setFont(font)
        self.btn_dashboard_2.setStatusTip("")
        self.btn_dashboard_2.setStyleSheet("QPushButton#btn_dashboard{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_dashboard:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_dashboard:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_dashboard_2.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/Imagens/dashboard (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dashboard_2.setIcon(icon27)
        self.btn_dashboard_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_dashboard_2.setObjectName("btn_dashboard_2")
        self.horizontalLayout_30.addWidget(self.groupBox_129)
        self.groupBox_123 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_123.setMinimumSize(QtCore.QSize(271, 51))
        self.groupBox_123.setMaximumSize(QtCore.QSize(271, 51))
        self.groupBox_123.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_123.setObjectName("groupBox_123")
        self.btn_rnc_2 = QtWidgets.QPushButton(self.groupBox_123)
        self.btn_rnc_2.setEnabled(False)
        self.btn_rnc_2.setGeometry(QtCore.QRect(26, 15, 30, 30))
        self.btn_rnc_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_rnc_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_rnc_2.setFont(font)
        self.btn_rnc_2.setStyleSheet("QPushButton#btn_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_rnc_2.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/Imagens/registro-online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rnc_2.setIcon(icon28)
        self.btn_rnc_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_rnc_2.setObjectName("btn_rnc_2")
        self.btn_usuarios_2 = QtWidgets.QPushButton(self.groupBox_123)
        self.btn_usuarios_2.setEnabled(False)
        self.btn_usuarios_2.setGeometry(QtCore.QRect(76, 15, 30, 30))
        self.btn_usuarios_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_usuarios_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_usuarios_2.setFont(font)
        self.btn_usuarios_2.setStyleSheet("QPushButton#btn_usuarios{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_usuarios:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_usuarios:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_usuarios_2.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/Imagens/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_usuarios_2.setIcon(icon29)
        self.btn_usuarios_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_usuarios_2.setObjectName("btn_usuarios_2")
        self.horizontalLayout_30.addWidget(self.groupBox_123)
        self.groupBox_124 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_124.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_124.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_124.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_124.setObjectName("groupBox_124")
        self.btn_tratativa = QtWidgets.QPushButton(self.groupBox_124)
        self.btn_tratativa.setEnabled(False)
        self.btn_tratativa.setGeometry(QtCore.QRect(24, 16, 30, 30))
        self.btn_tratativa.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_tratativa.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_tratativa.setFont(font)
        self.btn_tratativa.setStyleSheet("QPushButton#btn_tratativa{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_tratativa:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_tratativa:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_tratativa.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/Imagens/investigacao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tratativa.setIcon(icon30)
        self.btn_tratativa.setIconSize(QtCore.QSize(24, 24))
        self.btn_tratativa.setDefault(False)
        self.btn_tratativa.setObjectName("btn_tratativa")
        self.horizontalLayout_30.addWidget(self.groupBox_124)
        self.groupBox_127 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_127.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_127.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_127.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_127.setObjectName("groupBox_127")
        self.btn_consultar_2 = QtWidgets.QPushButton(self.groupBox_127)
        self.btn_consultar_2.setEnabled(False)
        self.btn_consultar_2.setGeometry(QtCore.QRect(26, 16, 30, 30))
        self.btn_consultar_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_consultar_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_consultar_2.setFont(font)
        self.btn_consultar_2.setStyleSheet("QPushButton#btn_consultar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_consultar_2.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/Imagens/pesquisa-de-dados (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_consultar_2.setIcon(icon31)
        self.btn_consultar_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultar_2.setObjectName("btn_consultar_2")
        self.horizontalLayout_30.addWidget(self.groupBox_127)
        self.groupBox_125 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_125.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_125.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_125.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_125.setObjectName("groupBox_125")
        self.horizontalLayout_30.addWidget(self.groupBox_125)
        self.groupBox_128 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_128.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_128.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_128.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_128.setObjectName("groupBox_128")
        self.btn_logoff_3 = QtWidgets.QPushButton(self.groupBox_128)
        self.btn_logoff_3.setGeometry(QtCore.QRect(6, 16, 60, 30))
        self.btn_logoff_3.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_logoff_3.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_logoff_3.setFont(font)
        self.btn_logoff_3.setStyleSheet("QPushButton#btn_logoff{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_logoff:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_logoff:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_logoff_3.setText("")
        self.btn_logoff_3.setIcon(icon10)
        self.btn_logoff_3.setIconSize(QtCore.QSize(24, 24))
        self.btn_logoff_3.setObjectName("btn_logoff_3")
        self.horizontalLayout_30.addWidget(self.groupBox_128)
        self.groupBox_126 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_126.setMinimumSize(QtCore.QSize(81, 51))
        self.groupBox_126.setMaximumSize(QtCore.QSize(81, 51))
        self.groupBox_126.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_126.setObjectName("groupBox_126")
        self.btn_sairApp_2 = QtWidgets.QPushButton(self.groupBox_126)
        self.btn_sairApp_2.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.btn_sairApp_2.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_sairApp_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_sairApp_2.setFont(font)
        self.btn_sairApp_2.setStyleSheet("QPushButton#btn_sairApp{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sairApp:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sairApp:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_sairApp_2.setText("")
        self.btn_sairApp_2.setIcon(icon11)
        self.btn_sairApp_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_sairApp_2.setObjectName("btn_sairApp_2")
        self.horizontalLayout_30.addWidget(self.groupBox_126)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.layoutWidget17 = QtWidgets.QWidget(self.page_9)
        self.layoutWidget17.setGeometry(QtCore.QRect(29, 101, 949, 513))
        self.layoutWidget17.setObjectName("layoutWidget17")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.layoutWidget17)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.groupBox_62 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_62.setMinimumSize(QtCore.QSize(231, 71))
        self.groupBox_62.setObjectName("groupBox_62")
        self.cb_setor_1 = QtWidgets.QComboBox(self.groupBox_62)
        self.cb_setor_1.setEnabled(False)
        self.cb_setor_1.setGeometry(QtCore.QRect(14, 25, 200, 29))
        self.cb_setor_1.setMinimumSize(QtCore.QSize(200, 23))
        self.cb_setor_1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_setor_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_setor_1.setObjectName("cb_setor_1")
        self.cb_setor_1.addItem("")
        self.cb_setor_1.setItemText(0, "")
        self.horizontalLayout_33.addWidget(self.groupBox_62)
        self.groupBox_63 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_63.setMinimumSize(QtCore.QSize(231, 71))
        self.groupBox_63.setObjectName("groupBox_63")
        self.cb_setor_2 = QtWidgets.QComboBox(self.groupBox_63)
        self.cb_setor_2.setEnabled(False)
        self.cb_setor_2.setGeometry(QtCore.QRect(20, 30, 200, 29))
        self.cb_setor_2.setMinimumSize(QtCore.QSize(200, 23))
        self.cb_setor_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_setor_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_setor_2.setObjectName("cb_setor_2")
        self.cb_setor_2.addItem("")
        self.cb_setor_2.setItemText(0, "")
        self.horizontalLayout_33.addWidget(self.groupBox_63)
        self.verticalLayout_31.addLayout(self.horizontalLayout_33)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.groupBox_64 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_64.setMinimumSize(QtCore.QSize(771, 71))
        self.groupBox_64.setObjectName("groupBox_64")
        self.cd_tipo_rnc = QtWidgets.QComboBox(self.groupBox_64)
        self.cd_tipo_rnc.setEnabled(True)
        self.cd_tipo_rnc.setGeometry(QtCore.QRect(10, 30, 751, 29))
        self.cd_tipo_rnc.setMinimumSize(QtCore.QSize(751, 23))
        self.cd_tipo_rnc.setMaximumSize(QtCore.QSize(751, 16777215))
        self.cd_tipo_rnc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cd_tipo_rnc.setObjectName("cd_tipo_rnc")
        self.cd_tipo_rnc.addItem("")
        self.cd_tipo_rnc.setItemText(0, "")
        self.verticalLayout_30.addWidget(self.groupBox_64)
        self.groupBox_65 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_65.setMinimumSize(QtCore.QSize(941, 211))
        self.groupBox_65.setObjectName("groupBox_65")
        self.txt_descreva = QtWidgets.QPlainTextEdit(self.groupBox_65)
        self.txt_descreva.setEnabled(True)
        self.txt_descreva.setGeometry(QtCore.QRect(10, 20, 911, 182))
        self.txt_descreva.setMinimumSize(QtCore.QSize(911, 182))
        self.txt_descreva.setMaximumSize(QtCore.QSize(911, 192))
        self.txt_descreva.setStyleSheet("")
        self.txt_descreva.setObjectName("txt_descreva")
        self.verticalLayout_30.addWidget(self.groupBox_65)
        self.verticalLayout_31.addLayout(self.verticalLayout_30)
        self.verticalLayout_32.addLayout(self.verticalLayout_31)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.groupBox_66 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_66.setObjectName("groupBox_66")
        self.layoutWidget18 = QtWidgets.QWidget(self.groupBox_66)
        self.layoutWidget18.setGeometry(QtCore.QRect(20, 20, 203, 33))
        self.layoutWidget18.setObjectName("layoutWidget18")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.layoutWidget18)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget18)
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_42.addWidget(self.radioButton)
        self.cb_sn = QtWidgets.QComboBox(self.layoutWidget18)
        self.cb_sn.setEnabled(False)
        self.cb_sn.setMinimumSize(QtCore.QSize(50, 23))
        self.cb_sn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_sn.setObjectName("cb_sn")
        self.cb_sn.addItem("")
        self.cb_sn.setItemText(0, "")
        self.cb_sn.addItem("")
        self.horizontalLayout_42.addWidget(self.cb_sn)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget18)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_43.addWidget(self.radioButton_2)
        self.cb_mt = QtWidgets.QComboBox(self.layoutWidget18)
        self.cb_mt.setEnabled(False)
        self.cb_mt.setMinimumSize(QtCore.QSize(50, 23))
        self.cb_mt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_mt.setObjectName("cb_mt")
        self.cb_mt.addItem("")
        self.cb_mt.setItemText(0, "")
        self.cb_mt.addItem("")
        self.horizontalLayout_43.addWidget(self.cb_mt)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_43)
        self.horizontalLayout_34.addWidget(self.groupBox_66)
        self.groupBox_67 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_67.setMinimumSize(QtCore.QSize(251, 61))
        self.groupBox_67.setObjectName("groupBox_67")
        self.dt_rnc = QtWidgets.QDateEdit(self.groupBox_67)
        self.dt_rnc.setEnabled(False)
        self.dt_rnc.setGeometry(QtCore.QRect(30, 20, 150, 29))
        self.dt_rnc.setMinimumSize(QtCore.QSize(150, 23))
        self.dt_rnc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.dt_rnc.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_rnc.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 2), QtCore.QTime(18, 0, 0)))
        self.dt_rnc.setCalendarPopup(True)
        self.dt_rnc.setObjectName("dt_rnc")
        self.horizontalLayout_34.addWidget(self.groupBox_67)
        self.groupBox_68 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_68.setMinimumSize(QtCore.QSize(251, 61))
        self.groupBox_68.setObjectName("groupBox_68")
        self.cb_funcao = QtWidgets.QComboBox(self.groupBox_68)
        self.cb_funcao.setEnabled(False)
        self.cb_funcao.setGeometry(QtCore.QRect(10, 20, 240, 29))
        self.cb_funcao.setMinimumSize(QtCore.QSize(240, 23))
        self.cb_funcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao.setObjectName("cb_funcao")
        self.cb_funcao.addItem("")
        self.cb_funcao.setItemText(0, "")
        self.horizontalLayout_34.addWidget(self.groupBox_68)
        self.verticalLayout_32.addLayout(self.horizontalLayout_34)
        self.verticalLayout_33.addLayout(self.verticalLayout_32)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.groupBox_69 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_69.setMinimumSize(QtCore.QSize(251, 61))
        self.groupBox_69.setObjectName("groupBox_69")
        self.cb_funcao_outros = QtWidgets.QLineEdit(self.groupBox_69)
        self.cb_funcao_outros.setEnabled(False)
        self.cb_funcao_outros.setGeometry(QtCore.QRect(20, 20, 220, 23))
        self.cb_funcao_outros.setMinimumSize(QtCore.QSize(220, 23))
        self.cb_funcao_outros.setMaximumSize(QtCore.QSize(220, 23))
        self.cb_funcao_outros.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao_outros.setObjectName("cb_funcao_outros")
        self.horizontalLayout_35.addWidget(self.groupBox_69)
        self.groupBox_70 = QtWidgets.QGroupBox(self.layoutWidget17)
        self.groupBox_70.setMinimumSize(QtCore.QSize(571, 61))
        self.groupBox_70.setObjectName("groupBox_70")
        self.cb_funcao_outros_3 = QtWidgets.QLineEdit(self.groupBox_70)
        self.cb_funcao_outros_3.setEnabled(False)
        self.cb_funcao_outros_3.setGeometry(QtCore.QRect(20, 21, 521, 23))
        self.cb_funcao_outros_3.setMinimumSize(QtCore.QSize(521, 23))
        self.cb_funcao_outros_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao_outros_3.setObjectName("cb_funcao_outros_3")
        self.horizontalLayout_35.addWidget(self.groupBox_70)
        self.verticalLayout_33.addLayout(self.horizontalLayout_35)
        self.layoutWidget19 = QtWidgets.QWidget(self.page_9)
        self.layoutWidget19.setGeometry(QtCore.QRect(275, 26, 420, 63))
        self.layoutWidget19.setObjectName("layoutWidget19")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.layoutWidget19)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.groupBox_72 = QtWidgets.QGroupBox(self.layoutWidget19)
        self.groupBox_72.setMinimumSize(QtCore.QSize(81, 61))
        self.groupBox_72.setMaximumSize(QtCore.QSize(81, 61))
        self.groupBox_72.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_72.setObjectName("groupBox_72")
        self.btn_nova_rnc = QtWidgets.QPushButton(self.groupBox_72)
        self.btn_nova_rnc.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.btn_nova_rnc.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_nova_rnc.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_nova_rnc.setFont(font)
        self.btn_nova_rnc.setStyleSheet("QPushButton#btn_nova_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_nova_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_nova_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_nova_rnc.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/Imagens/registro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nova_rnc.setIcon(icon32)
        self.btn_nova_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_nova_rnc.setObjectName("btn_nova_rnc")
        self.horizontalLayout_38.addWidget(self.groupBox_72)
        self.groupBox_73 = QtWidgets.QGroupBox(self.layoutWidget19)
        self.groupBox_73.setMinimumSize(QtCore.QSize(81, 61))
        self.groupBox_73.setMaximumSize(QtCore.QSize(81, 61))
        self.groupBox_73.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_73.setObjectName("groupBox_73")
        self.btn_gerar_pdf = QtWidgets.QPushButton(self.groupBox_73)
        self.btn_gerar_pdf.setEnabled(False)
        self.btn_gerar_pdf.setGeometry(QtCore.QRect(26, 20, 30, 30))
        self.btn_gerar_pdf.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_gerar_pdf.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_gerar_pdf.setFont(font)
        self.btn_gerar_pdf.setStyleSheet("QPushButton#btn_gerar_pdf{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_gerar_pdf:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_gerar_pdf:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_gerar_pdf.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/Imagens/pdf (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gerar_pdf.setIcon(icon33)
        self.btn_gerar_pdf.setIconSize(QtCore.QSize(24, 24))
        self.btn_gerar_pdf.setObjectName("btn_gerar_pdf")
        self.horizontalLayout_38.addWidget(self.groupBox_73)
        self.groupBox_71 = QtWidgets.QGroupBox(self.layoutWidget19)
        self.groupBox_71.setObjectName("groupBox_71")
        self.layoutWidget20 = QtWidgets.QWidget(self.groupBox_71)
        self.layoutWidget20.setGeometry(QtCore.QRect(40, 20, 98, 32))
        self.layoutWidget20.setObjectName("layoutWidget20")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.layoutWidget20)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.txt_consultaNoti_2 = QtWidgets.QLineEdit(self.layoutWidget20)
        self.txt_consultaNoti_2.setMinimumSize(QtCore.QSize(60, 30))
        self.txt_consultaNoti_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_consultaNoti_2.setFont(font)
        self.txt_consultaNoti_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 2px;\n"
"border-top-right-radius : 20px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_consultaNoti_2.setText("")
        self.txt_consultaNoti_2.setObjectName("txt_consultaNoti_2")
        self.horizontalLayout_31.addWidget(self.txt_consultaNoti_2)
        self.btn_pesquisar_rnc = QtWidgets.QPushButton(self.layoutWidget20)
        self.btn_pesquisar_rnc.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_pesquisar_rnc.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_pesquisar_rnc.setFont(font)
        self.btn_pesquisar_rnc.setStyleSheet("QPushButton#btn_pesquisar_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisar_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisar_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisar_rnc.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/Imagens/historia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pesquisar_rnc.setIcon(icon34)
        self.btn_pesquisar_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_pesquisar_rnc.setObjectName("btn_pesquisar_rnc")
        self.horizontalLayout_31.addWidget(self.btn_pesquisar_rnc)
        self.horizontalLayout_38.addWidget(self.groupBox_71)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.btn_salva_rnc = QtWidgets.QPushButton(self.layoutWidget19)
        self.btn_salva_rnc.setEnabled(True)
        self.btn_salva_rnc.setMinimumSize(QtCore.QSize(30, 28))
        self.btn_salva_rnc.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_salva_rnc.setFont(font)
        self.btn_salva_rnc.setStyleSheet("QPushButton#btn_salva_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salva_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salva_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salva_rnc.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/Imagens/salve-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_salva_rnc.setIcon(icon35)
        self.btn_salva_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_salva_rnc.setObjectName("btn_salva_rnc")
        self.horizontalLayout_37.addWidget(self.btn_salva_rnc)
        self.btn_cancela_rnc = QtWidgets.QPushButton(self.layoutWidget19)
        self.btn_cancela_rnc.setEnabled(True)
        self.btn_cancela_rnc.setMinimumSize(QtCore.QSize(30, 28))
        self.btn_cancela_rnc.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_cancela_rnc.setFont(font)
        self.btn_cancela_rnc.setStyleSheet("QPushButton#btn_cancela_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_rnc.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/Imagens/cancelar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancela_rnc.setIcon(icon36)
        self.btn_cancela_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_rnc.setObjectName("btn_cancela_rnc")
        self.horizontalLayout_37.addWidget(self.btn_cancela_rnc)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_37)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.stackedWidget.addWidget(self.page_10)
        self.layoutWidget21 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget21.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget21.setObjectName("layoutWidget21")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget21)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIN - SISTEMA INTEGRADO DE NOTIFICAÇÕES"))
        self.groupBox.setTitle(_translate("MainWindow", "SELECIONE A NOTIFICAÇÃO QUE DESEJA ACESSAR"))
        self.groupBox_2.setTitle(_translate("MainWindow", " EVENTO ADVERSO"))
        self.btn_fnea.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMAÇÕES</span></p></body></html>"))
        self.btn_fnea.setText(_translate("MainWindow", "FNEA"))
        self.groupBox_3.setTitle(_translate("MainWindow", " NÃO CONFORMIDADE"))
        self.btn_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_rnc.setText(_translate("MainWindow", "RNC"))
        self.label_5.setText(_translate("MainWindow", "Desenvolvido por: Márcio Anderson e Leonardo Aquino"))
        self.btn_voltar_fnea.setText(_translate("MainWindow", "VOLTAR"))
        self.label_7.setText(_translate("MainWindow", "NOTIFICAÇÃO DE EVENTO ADVERSO"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "notihomologacao"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "notiproducao"))
        self.btn_login.setToolTip(_translate("MainWindow", "Informe Usuário e Senha e efetue o login"))
        self.btn_login.setText(_translate("MainWindow", "L O G  I N"))
        self.btn_notificaSlogin.setText(_translate("MainWindow", "A P E N A S | N O T I F I C A R"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Estratégico"))
        self.btn_dashboard.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMAÇÕES</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Cadastros"))
        self.btn_notifica.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Investigação"))
        self.btn_investigar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE INVESTIGAÇÃO</span></p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Consulta"))
        self.btn_consultar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CONSULTA DE NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Relatório"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Logoff"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Sair"))
        self.groupBox_30.setTitle(_translate("MainWindow", "Novo-------Editar-----Integra"))
        self.btn_notificar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_editarNoti.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">EDITAR NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_buscarMv.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">BUSCAR PACIENTE NO MV</span></p></body></html>"))
        self.groupBox_33.setTitle(_translate("MainWindow", "Número da Notificação"))
        self.btn_pesquisarNoti.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_31.setTitle(_translate("MainWindow", "Gerar PDF"))
        self.btn_relatorio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERAR FICHA DE NOTIFICAÇÃO EM PDF</span></p></body></html>"))
        self.groupBox_32.setTitle(_translate("MainWindow", "Salvar | Cancelar"))
        self.btn_salva_noti.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">SALVAR NOTIFICAÇÃO</p></body></html>"))
        self.btn_cancela_noti.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">CANCELAR NOTIFICAÇÃO</p></body></html>"))
        self.groupBox_34.setTitle(_translate("MainWindow", "Habilitar Edição"))
        self.btn_alterar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">ALTERAR NOTIFICAÇÃO</p></body></html>"))
        self.groupBox_35.setTitle(_translate("MainWindow", "Resumo Investigação"))
        self.btn_resumoInvest.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.groupBox_36.setTitle(_translate("MainWindow", "Menu "))
        self.btn_voltar.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.label_67.setText(_translate("MainWindow", "Cod.Paciente:"))
        self.label_68.setText(_translate("MainWindow", "Paciente:"))
        self.label_82.setText(_translate("MainWindow", "Nome Social:"))
        self.label_69.setText(_translate("MainWindow", "Data Nascimento"))
        self.label_70.setText(_translate("MainWindow", "Sexo:"))
        self.cb_sex.setItemText(1, _translate("MainWindow", "Masculino"))
        self.cb_sex.setItemText(2, _translate("MainWindow", "Feminino"))
        self.cb_sex.setItemText(3, _translate("MainWindow", "Transgênero"))
        self.cb_sex.setItemText(4, _translate("MainWindow", "Cisgênero"))
        self.cb_sex.setItemText(5, _translate("MainWindow", "Não-binário"))
        self.label_71.setText(_translate("MainWindow", "Setor de Registro"))
        self.label_66.setText(_translate("MainWindow", "Raça | Cor:"))
        self.cb_rac.setItemText(1, _translate("MainWindow", "Amarelo"))
        self.cb_rac.setItemText(2, _translate("MainWindow", "Branco"))
        self.cb_rac.setItemText(3, _translate("MainWindow", "Indigena"))
        self.cb_rac.setItemText(4, _translate("MainWindow", "Pardo"))
        self.cb_rac.setItemText(5, _translate("MainWindow", "Preto"))
        self.cb_rac.setItemText(6, _translate("MainWindow", "Indefinido"))
        self.label_81.setText(_translate("MainWindow", "Setor de ocorrência da notificação:"))
        self.label_72.setText(_translate("MainWindow", "Leito:"))
        self.label_73.setText(_translate("MainWindow", "Data Internação"))
        self.label_62.setText(_translate("MainWindow", "Diagnóstico:"))
        self.label_63.setText(_translate("MainWindow", "Tratamento:"))
        self.label_64.setText(_translate("MainWindow", "Dt|Hr Evento:"))
        self.rb_mt.setToolTip(_translate("MainWindow", "<html><head/><body><p>De 7h às 19h</p></body></html>"))
        self.rb_mt.setText(_translate("MainWindow", "MT"))
        self.rb_sn.setToolTip(_translate("MainWindow", "<html><head/><body><p>19h às 7h</p></body></html>"))
        self.rb_sn.setText(_translate("MainWindow", "SN"))
        self.label_65.setText(_translate("MainWindow", "Dt|Hr Notificação:"))
        self.chk_nsp.setText(_translate("MainWindow", "NSP - NÚCLEO DE SEGURANÇA DO PACIENTE"))
        self.ck_falha_id.setText(_translate("MainWindow", "Falha na Identificação do Paciente"))
        self.ck_falha_comu.setText(_translate("MainWindow", "Falha de Comunicação do Paciente."))
        self.ck_falha_oxi.setText(_translate("MainWindow", "Falha no Uso de Oxigênio e Outros Gases"))
        self.ck_falha_sonda.setText(_translate("MainWindow", "Falha no Manuseio e na Identificação dos Cateteres e\n"
"Sondas"))
        self.ck_falha_nutri.setText(_translate("MainWindow", "Falha na Administração da Nutrição."))
        self.ck_falha_hemo.setText(_translate("MainWindow", "Falha na Administração de Hemocomponentes"))
        self.ck_falha_med.setText(_translate("MainWindow", "Falha na Prescrição, Dispensação, Manuseio, Preparo e/ou \n"
"Administração de Medicamentos"))
        self.ck_falha_usu.setText(_translate("MainWindow", "Falha no Transporte do Usuário"))
        self.ck_falha_anest_2.setText(_translate("MainWindow", "Falha no Procedimento Anestésico"))
        self.ck_falha_dispo_2.setText(_translate("MainWindow", "Falha no Uso de Dispositivos e Equipamentos"))
        self.ck_queda_hosp_2.setText(_translate("MainWindow", "Queda em Paciente Hospitalizado"))
        self.ck_falha_cirurg_2.setText(_translate("MainWindow", "Falha no Procedimento Cirúrgico"))
        self.ck_ulcera_2.setText(_translate("MainWindow", "Úlcera por Pressão Durante a Internação"))
        self.ck_infeccao_2.setText(_translate("MainWindow", "Infecção Associada à Assistência à Saúde"))
        self.ck_inadequada_2.setText(_translate("MainWindow", "Higiene das Mãos Inadequada"))
        self.ck_higiene_paciente_2.setText(_translate("MainWindow", "Higiene Precária do Paciente"))
        self.ck_neonato_2.setText(_translate("MainWindow", "Trauma no Nascimento: Dano ao Neonato"))
        self.ck_vaginal_2.setText(_translate("MainWindow", "Trauma Obstétrico: Em Parto Vaginal"))
        self.ck_cesariana_2.setText(_translate("MainWindow", "Trauma Obstétrico: Em Cesariana"))
        self.ck_atendimento_2.setText(_translate("MainWindow", "Atraso no Atendimento"))
        self.ck_conflito_2.setText(_translate("MainWindow", "Conflito"))
        self.ck_evasao_2.setText(_translate("MainWindow", "Evasão do Paciente"))
        self.ck_sentinela_2.setText(_translate("MainWindow", "Evento Sentinela"))
        self.ck_queimadura_2.setText(_translate("MainWindow", "Queimadura Pós-Procedimento"))
        self.ck_outros_2.setText(_translate("MainWindow", "outros:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tipos de Eventos"))
        self.label_74.setText(_translate("MainWindow", "DESCRIÇÃO DA OCORRENCIA:"))
        self.label_75.setText(_translate("MainWindow", "HOUVE DANO AO PACIENTE?"))
        self.rb_dano_sim.setText(_translate("MainWindow", "SIM"))
        self.rb_dano_nao.setText(_translate("MainWindow", "NÃO"))
        self.rb_dano_SI.setText(_translate("MainWindow", "S.I"))
        self.label_76.setText(_translate("MainWindow", "ESCALA DO DANO"))
        self.cb_dan.setItemText(1, _translate("MainWindow", "NÃO REGISTRADO"))
        self.cb_dan.setItemText(2, _translate("MainWindow", "NENHUM"))
        self.cb_dan.setItemText(3, _translate("MainWindow", "LEVE -(apresentou sintomas leves, danos de curta duração, necessitou de observação mínima.)"))
        self.cb_dan.setItemText(4, _translate("MainWindow", "MODERADO -(apresentou sintomas, danos permanentes ou a longo prazo, necessitou de procedimento suplementar ou terapêutica adicional.)"))
        self.cb_dan.setItemText(5, _translate("MainWindow", "GRAVE - (necessitou de intervenção para salvar vida, intervenção médico-cirúrgica, danos permanentes ou em longo prazo..)"))
        self.cb_dan.setItemText(6, _translate("MainWindow", "ÓBITO -(causado pelo evento adverso.)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Descrição da Ocorrencia"))
        self.label_77.setText(_translate("MainWindow", "COMO FOI IDENTIFICADO:"))
        self.label_78.setText(_translate("MainWindow", "AÇÃO TOMADA NO EVENTO:"))
        self.label_79.setText(_translate("MainWindow", "QUEM IDENTIFICOU:"))
        self.label_80.setText(_translate("MainWindow", "IDENTIFICAÇÃO(OPCIONAL)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Detalhes do Evento"))
        self.label_98.setText(_translate("MainWindow", "IDENTIFICAÇÃO DE FATORES CONTRIBUINTES: DIAGRAMA DE CAUSA E EFEITO - ISHIKAWA"))
        self.label_16.setText(_translate("MainWindow", "SIN - SISTEMA INTEGRADO DE NOTIFICAÇÕES-FNEA"))
        self.btn_voltar_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Resumo Notificação"))
        self.groupBox_75.setTitle(_translate("MainWindow", "Iniciar Investigação"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Buscar Notificação"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Concluir |    Cancelar |    Alterar"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Habilitar Edição"))
        self.groupBox_23.setTitle(_translate("MainWindow", "Status Investigação"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Não iniciada"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Em andamento"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Com Pendências"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Concluído"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Paciente"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Pessoas"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Pessoas"))
        self.groupBox_19.setTitle(_translate("MainWindow", "Materiais | Equipamentos"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Ambiente de Trabalho"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Observações:"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Recomendações:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Investigação"))
        self.groupBox_28.setTitle(_translate("MainWindow", "Como?"))
        self.groupBox_29.setTitle(_translate("MainWindow", "Conclusão do Time:"))
        self.groupBox_24.setTitle(_translate("MainWindow", "O que?"))
        self.groupBox_25.setTitle(_translate("MainWindow", "Por que?"))
        self.groupBox_26.setTitle(_translate("MainWindow", "Quem?"))
        self.groupBox_27.setTitle(_translate("MainWindow", "Quando?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Plano de Ação"))
        self.label_18.setText(_translate("MainWindow", "SIN - SISTEMA INTEGRADO DE NOTIFICAÇÕES-FNEA"))
        self.groupBox_61.setTitle(_translate("MainWindow", "Consultar Notificações"))
        self.btn_voltar_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.label_136.setText(_translate("MainWindow", "Paciente:"))
        self.groupBox_37.setTitle(_translate("MainWindow", "Pesquisa por Status"))
        self.radioButton_10.setText(_translate("MainWindow", "Não Iniciada"))
        self.radioButton_11.setText(_translate("MainWindow", "Em Andamento"))
        self.radioButton_12.setText(_translate("MainWindow", "Com Pendências"))
        self.radioButton_13.setText(_translate("MainWindow", "Concluída"))
        item = self.tb_consulta_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CodN"))
        item = self.tb_consulta_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CodP"))
        item = self.tb_consulta_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Paciente"))
        item = self.tb_consulta_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.tb_consulta_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Unidade de internação"))
        item = self.tb_consulta_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cod-Inv"))
        item = self.tb_consulta_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data Evento"))
        item = self.tb_consulta_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Data Notificação"))
        self.groupBox_38.setTitle(_translate("MainWindow", "Cadastro de Usuários"))
        self.btn_voltar_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.groupBox_39.setTitle(_translate("MainWindow", "Nome Completo"))
        self.groupBox_40.setTitle(_translate("MainWindow", "Usuário"))
        self.groupBox_42.setTitle(_translate("MainWindow", "Senha"))
        self.groupBox_41.setTitle(_translate("MainWindow", "Perfil"))
        self.cb_outros_4.setItemText(1, _translate("MainWindow", "Notificador"))
        self.cb_outros_4.setItemText(2, _translate("MainWindow", "Investigador N1"))
        self.cb_outros_4.setItemText(3, _translate("MainWindow", "Investigador N2"))
        self.cb_outros_4.setItemText(4, _translate("MainWindow", "Administrador"))
        self.groupBox_43.setTitle(_translate("MainWindow", "Consulta Usuários Cadastrados"))
        self.groupBox_44.setTitle(_translate("MainWindow", "Nome:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Usuário"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Perfil"))
        self.groupBox_48.setTitle(_translate("MainWindow", "Salvar"))
        self.groupBox_49.setTitle(_translate("MainWindow", "Cancelar"))
        self.groupBox_45.setTitle(_translate("MainWindow", "Novo"))
        self.groupBox_46.setTitle(_translate("MainWindow", "Editar"))
        self.groupBox_47.setTitle(_translate("MainWindow", "Alterar"))
        self.groupBox_50.setTitle(_translate("MainWindow", "Cadastro de Setor"))
        self.label_19.setText(_translate("MainWindow", "Nome:"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Setor"))
        self.groupBox_51.setTitle(_translate("MainWindow", "Novo"))
        self.groupBox_52.setTitle(_translate("MainWindow", "Editar"))
        self.groupBox_55.setTitle(_translate("MainWindow", "Alterar"))
        self.groupBox_53.setTitle(_translate("MainWindow", "Salvar"))
        self.groupBox_54.setTitle(_translate("MainWindow", "Cancelar"))
        self.label_21.setText(_translate("MainWindow", "SIN - SISTEMA INTEGRADO DE NOTIFICAÇÕES-FNEA"))
        self.btn_voltar_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.groupBox_56.setTitle(_translate("MainWindow", "Cadastro de E-mail para recebimento de notificação"))
        self.groupBox_60.setTitle(_translate("MainWindow", "Pesquisar"))
        self.label_10.setText(_translate("MainWindow", "E-mail:"))
        self.groupBox_57.setTitle(_translate("MainWindow", "E-mails Cadastrados"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        self.groupBox_58.setTitle(_translate("MainWindow", "Novo"))
        self.groupBox_59.setTitle(_translate("MainWindow", "Alterar"))
        self.groupBox_74.setTitle(_translate("MainWindow", "Excluir"))
        self.btn_voltar_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>RESUMO DA INVESTIGAÇÃO</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "SIN - SISTEMA INTEGRADO DE NOTIFICAÇÕES-FNEA"))
        self.label_13.setText(_translate("MainWindow", "REGISTRO DE"))
        self.label_23.setText(_translate("MainWindow", " NÃO CONFORMIDADE"))
        self.txt_usuario.setPlaceholderText(_translate("MainWindow", "Digite seu Usuário"))
        self.txt_senha.setPlaceholderText(_translate("MainWindow", "Digite sua Senha"))
        self.cb_empresa.setItemText(0, _translate("MainWindow", "bd_rnc"))
        self.cb_empresa.setItemText(1, _translate("MainWindow", "bd_rnc_homologa"))
        self.btn_anonimo.setText(_translate("MainWindow", "ANÔNIMO"))
        self.btn_login_rnc.setText(_translate("MainWindow", "L O G I N"))
        self.btn_SairApp.setText(_translate("MainWindow", "VOLTAR"))
        self.groupBox_129.setTitle(_translate("MainWindow", "Estratégico"))
        self.btn_dashboard_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMAÇÕES</span></p></body></html>"))
        self.groupBox_123.setTitle(_translate("MainWindow", "Cadastros"))
        self.btn_rnc_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_124.setTitle(_translate("MainWindow", "Investigação"))
        self.btn_tratativa.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE INVESTIGAÇÃO</span></p></body></html>"))
        self.groupBox_127.setTitle(_translate("MainWindow", "Consulta"))
        self.btn_consultar_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CONSULTA DE NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_125.setTitle(_translate("MainWindow", "Relatório"))
        self.groupBox_128.setTitle(_translate("MainWindow", "Logoff"))
        self.groupBox_126.setTitle(_translate("MainWindow", "Sair"))
        self.groupBox_62.setTitle(_translate("MainWindow", "Setor de Registro"))
        self.groupBox_63.setTitle(_translate("MainWindow", "Setor de ocorrência da Não Conformidade"))
        self.groupBox_64.setTitle(_translate("MainWindow", "Não conformidade"))
        self.groupBox_65.setTitle(_translate("MainWindow", "Descreva a Não Conformidade"))
        self.txt_descreva.setToolTip(_translate("MainWindow", "Ocorrência: Iniciar o relato com uma breve frase que possa resumir a ocorrência da Não Conformidade constatado, de forma clara, concisa e compreensível;\n"
"\n"
"Evidência Objetiva: Apresentar as evidências objetivas (dados, informações) que dão veracidade a informação;\n"
"\n"
"Contrariedade: Justifica a existência da não conformidade (Contrário normativa Institucional/Informação documentada);\n"
"\n"
"Cláusula e Requisitos: Identificar o requisito pertinente e desenvolver um breve relato sobre o item não atendido. (Se conhecimento da norma ou informação documentada)."))
        self.groupBox_66.setTitle(_translate("MainWindow", "Turno de ocorrência da Não conformidade"))
        self.radioButton.setText(_translate("MainWindow", "SN"))
        self.cb_sn.setItemText(1, _translate("MainWindow", "SIM"))
        self.radioButton_2.setText(_translate("MainWindow", "MT"))
        self.cb_mt.setItemText(1, _translate("MainWindow", "SIM"))
        self.groupBox_67.setTitle(_translate("MainWindow", "Data de ocorrência da Não conformidade"))
        self.groupBox_68.setTitle(_translate("MainWindow", "Informe a Função"))
        self.cb_funcao.setToolTip(_translate("MainWindow", "Informe neste campo a função relacionada a não conformidade. Neste Campo não deve ser informada a sua função."))
        self.groupBox_69.setTitle(_translate("MainWindow", "Se outra função, especifique"))
        self.groupBox_70.setTitle(_translate("MainWindow", "Nome do Colaborador"))
        self.cb_funcao_outros_3.setToolTip(_translate("MainWindow", "Em caso de Não Conformidade NR32, informe o nome do colaborador"))
        self.groupBox_72.setTitle(_translate("MainWindow", "Novo"))
        self.btn_nova_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_73.setTitle(_translate("MainWindow", "Gerar PDF"))
        self.btn_gerar_pdf.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICAÇÃO</span></p></body></html>"))
        self.groupBox_71.setTitle(_translate("MainWindow", "Pesquisar não conformidade"))
        self.btn_pesquisar_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICAÇÃO</span></p></body></html>"))

        self.dt_notificacao.setDate(QtCore.QDate.currentDate())
        self.dt_internacao.setDate(QtCore.QDate.currentDate())
        self.dt_evento.setDate(QtCore.QDate.currentDate())

        self.ck_outros_2.stateChanged.connect(self.method)
        self.rb_dano_sim.clicked.connect(self.check)
        self.rb_dano_nao.clicked.connect(self.check)
        self.rb_dano_SI.clicked.connect(self.check)
        self.chk_nsp.setCheckState(True)

        preencherCBfnea(self)
        botoes(self)
        tabelaEmail(self)

        setores = con.consultar("SELECT setor from setores") #BUSCA OS SETORES CADASTRADOS NA TABELA
        for item in setores:
            self.cb_seto.addItems(item) # ADICIONA OS ITENS ENCONTRADOS A COMBOBOX

    def method(self):
        if self.ck_outros_2.isChecked() == True:
            self.ds_outros.setEnabled(True)

        else:
            self.ds_outros.setEnabled(False)

    def check(self):
        if self.rb_dano_sim.isChecked() == True:
            self.cb_dan.setEnabled(True)
        elif self.rb_dano_nao.isChecked() == True:
            self.cb_dan.setCurrentIndex(1)
        elif self.rb_dano_nao.isChecked() == True:
            self.cb_dan.setEnabled(False)
            self.cb_dan.setCurrentIndex(0)
        else:
            self.cb_dan.setCurrentIndex(2)

    ####################################################################################################################################
    ##########################################FUNCIONALIDADES BOTÕESFORMULÁRIO DE NOTIFICAÇÃO#################################################
    ####################################################################################################################################
    
    def inicioFnea(self):
            self.stackedWidget.setCurrentWidget(self.page_2)
    def login(self):
            validarLogin(self)
    def anonimo(self):
            anonimo(self)
    def novanotificacao(self):
            habilitarNotificar(self)
    def cancelanotificacao(self):
            desabilitarLimparCampos(self)
    def buscarPaciente(self):
            buscarMV(self)
    def notificar(self):
            salvarNotificacao(self)
    def consultarNotificacao(self):
            pesquisarNotificacao(self)
    def editarNotificacao(self):
            editandoNotificacao(self)
    def confirmarEdicao(self):
            atualizaNotificacao(self)
    def voltarMenuInicial(self):
            voltarMenu(self)
    ######################################################################################################################################
    ##########################################################FUNCOES INVESTIGAÇÃO########################################################
    ######################################################################################################################################

    def iniciarInvestigacao(self):
            iniciarinvestigacao(self)
    def cancelarInvestigacao(self):
            cancelarReabilitarCampos(self)
    def salvarInvestigacao(self):
            salvarInvestigacao(self)
    def buscarInvestigacao(self):
            buscarInvestigacao(self)
    def habilitarEdicaoInvestigacao(self):
            habilitarInvestigacao(self)
    def salvarEdicao(self):
            editarInvestigacao(self)

    def carregarEmail(self):
            tabelaEmail(self)
    def cadastrarEmail(self):
            inserir_email(self)
    def alterarEmail(self):
            alterarEmail(self)


    ######################################################################################################################################
    ##########################################################FUNCOES BOTOES STACKEDWIDGET MENU PRINCIPAL#################################
    ######################################################################################################################################

    def formularioNotificacao(self):
         self.stackedWidget.setCurrentWidget(self.page_3)   

    def formularioUsuarios(self):
         self.stackedWidget.setCurrentWidget(self.page_13)

    def formularioSetor(self):
        self.stackedWidget.setCurrentWidget(self.page_14)
    
    def formularioEmail(self):
        self.stackedWidget.setCurrentWidget(self.page_5)

    def formularioInvestigacao(self):
        self.stackedWidget.setCurrentWidget(self.page_4)
    
    def formularioConsultaFnea(self):
        self.stackedWidget.setCurrentWidget(self.page_12)

    def paginaDashboard(self):
        webbrowser.open("http://192.168.0.36:3000/public/dashboard/121eb4c6-7c7b-4b80-905a-c18dac19247f")


    ######################################################################################################################################
    ##########################################################RELATÓRIOS########################################################
    ######################################################################################################################################

    def gerarPDF(self):
        gerarPdf(self)

    def relatoriosPDF(self):
        consultaInvestigacao(self)

    ######################################################################################################################################
    ##########################################################USUÁRIOS########################################################
    ######################################################################################################################################

    def novoUsuario(self):
        habilitaCampos(self)
    def inserirUsuario(self):
        inserir_usuarios(self)
    def carregarCombo(self):
        consultaNome(self)
    def habilitarEdicao(self):
        editarUsuario(self)
    def alterarUsuario(self):
        alterUser(self)
    def cancelaUsuario(self):
        cancelar(self)


