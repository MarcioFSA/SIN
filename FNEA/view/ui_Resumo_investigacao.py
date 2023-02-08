# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Resumo_investigacao.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import Outros_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(966, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_104 = QLabel(self.centralwidget)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(320, 40, 351, 20))
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_104.setAlignment(Qt.AlignCenter)
        self.layoutWidget_5 = QWidget(self.centralwidget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(250, 90, 488, 42))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.layoutWidget_5)
        self.label_81.setObjectName(u"label_81")
        font1 = QFont()
        font1.setFamilies([u"Reem Kufi"])
        self.label_81.setFont(font1)
        self.label_81.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_81)

        self.txt_consultaNoti = QLineEdit(self.layoutWidget_5)
        self.txt_consultaNoti.setObjectName(u"txt_consultaNoti")
        self.txt_consultaNoti.setMinimumSize(QSize(250, 0))
        self.txt_consultaNoti.setFont(font1)
        self.txt_consultaNoti.setStyleSheet(u"\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")

        self.horizontalLayout_29.addWidget(self.txt_consultaNoti)

        self.btn_resumoInvestigacao = QPushButton(self.layoutWidget_5)
        self.btn_resumoInvestigacao.setObjectName(u"btn_resumoInvestigacao")
        self.btn_resumoInvestigacao.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setFamilies([u"Reem Kufi"])
        font2.setPointSize(8)
        font2.setBold(False)
        self.btn_resumoInvestigacao.setFont(font2)
        self.btn_resumoInvestigacao.setStyleSheet(u"QPushButton#btn_resumoInvestigacao{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumoInvestigacao:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumoInvestigacao:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Imagem/historia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resumoInvestigacao.setIcon(icon)
        self.btn_resumoInvestigacao.setIconSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.btn_resumoInvestigacao)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 201, 91))
        self.label_2.setStyleSheet(u"\n"
"image: url(:/Imagem/FNEA.jpg);\n"
"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(17, 140, 929, 452))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_85 = QLabel(self.layoutWidget)
        self.label_85.setObjectName(u"label_85")
        font3 = QFont()
        font3.setFamilies([u"Reem Kufi"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_85.setFont(font3)
        self.label_85.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_85)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_99 = QLabel(self.layoutWidget)
        self.label_99.setObjectName(u"label_99")
        font4 = QFont()
        font4.setFamilies([u"Reem Kufi"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_99.setFont(font4)
        self.label_99.setStyleSheet(u"color: rgb(0,0,0);")

        self.horizontalLayout_24.addWidget(self.label_99)

        self.txt_que = QLineEdit(self.layoutWidget)
        self.txt_que.setObjectName(u"txt_que")
        self.txt_que.setEnabled(False)
        self.txt_que.setMinimumSize(QSize(390, 0))
        self.txt_que.setFont(font1)
        self.txt_que.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_24.addWidget(self.txt_que)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_100 = QLabel(self.layoutWidget)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font4)
        self.label_100.setStyleSheet(u"color: rgb(0,0,0);")

        self.horizontalLayout_25.addWidget(self.label_100)

        self.txt_porque = QLineEdit(self.layoutWidget)
        self.txt_porque.setObjectName(u"txt_porque")
        self.txt_porque.setEnabled(False)
        self.txt_porque.setMinimumSize(QSize(411, 0))
        self.txt_porque.setFont(font1)
        self.txt_porque.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_25.addWidget(self.txt_porque)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_25)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_102 = QLabel(self.layoutWidget)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font4)
        self.label_102.setStyleSheet(u"color: rgb(0,0,0);")

        self.horizontalLayout_27.addWidget(self.label_102)

        self.txt_quem = QLineEdit(self.layoutWidget)
        self.txt_quem.setObjectName(u"txt_quem")
        self.txt_quem.setEnabled(False)
        self.txt_quem.setMinimumSize(QSize(395, 0))
        self.txt_quem.setFont(font1)
        self.txt_quem.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_27.addWidget(self.txt_quem)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_103 = QLabel(self.layoutWidget)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font4)
        self.label_103.setStyleSheet(u"color: rgb(0,0,0);")

        self.horizontalLayout_28.addWidget(self.label_103)

        self.txt_quando = QLineEdit(self.layoutWidget)
        self.txt_quando.setObjectName(u"txt_quando")
        self.txt_quando.setEnabled(False)
        self.txt_quando.setMinimumSize(QSize(405, 0))
        self.txt_quando.setFont(font1)
        self.txt_quando.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_28.addWidget(self.txt_quando)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_28)


        self.verticalLayout.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_98 = QLabel(self.layoutWidget)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font4)
        self.label_98.setStyleSheet(u"color: rgb(0,0,0);")

        self.horizontalLayout_22.addWidget(self.label_98)

        self.txt_como = QLineEdit(self.layoutWidget)
        self.txt_como.setObjectName(u"txt_como")
        self.txt_como.setEnabled(False)
        self.txt_como.setMinimumSize(QSize(395, 0))
        self.txt_como.setFont(font1)
        self.txt_como.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.horizontalLayout_22.addWidget(self.txt_como)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_101 = QLabel(self.layoutWidget)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font3)
        self.label_101.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_101.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_101)

        self.txt_conclusaoTime = QTextEdit(self.layoutWidget)
        self.txt_conclusaoTime.setObjectName(u"txt_conclusaoTime")
        self.txt_conclusaoTime.setEnabled(False)
        self.txt_conclusaoTime.setMinimumSize(QSize(921, 51))
        self.txt_conclusaoTime.setFont(font1)
        self.txt_conclusaoTime.setStyleSheet(u"background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")

        self.verticalLayout_10.addWidget(self.txt_conclusaoTime)


        self.verticalLayout.addLayout(self.verticalLayout_10)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.btn_sair_resumo = QPushButton(self.layoutWidget)
        self.btn_sair_resumo.setObjectName(u"btn_sair_resumo")
        self.btn_sair_resumo.setMinimumSize(QSize(100, 40))
        self.btn_sair_resumo.setFont(font2)
        self.btn_sair_resumo.setStyleSheet(u"QPushButton#btn_sair_resumo{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sair_resumo:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sair_resumo:pressed{\n"
"	padding-left:5px;\n"
"	padding -top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Imagem/remover (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair_resumo.setIcon(icon1)
        self.btn_sair_resumo.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_sair_resumo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"RESUMO DA INVESTIGA\u00c7\u00c3O", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"N\u00famero da notifica\u00e7\u00e3o", None))
        self.txt_consultaNoti.setText("")
#if QT_CONFIG(tooltip)
        self.btn_resumoInvestigacao.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICA\u00c7\u00c3O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_resumoInvestigacao.setText(QCoreApplication.translate("MainWindow", u"P E S Q U I S A R", None))
        self.label_2.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Plano de A\u00e7\u00e3o Executado:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"O Que?", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Por que?", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Quem?", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Quando?", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Como?", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Conclus\u00e3o do Time:", None))
        self.btn_sair_resumo.setText(QCoreApplication.translate("MainWindow", u"S A I R", None))
    # retranslateUi

