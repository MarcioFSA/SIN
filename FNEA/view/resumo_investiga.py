from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox

from FNEA.bd.conn import conexaoBD
from view.principal import *


class Ui_ui_investiga(object):
    def setupUi(self, ui_investiga):
        ui_investiga.setObjectName("ui_investiga")
        ui_investiga.resize(966, 600)
        ui_investiga.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ui_investiga)
        self.centralwidget.setObjectName("centralwidget")
        self.label_104 = QtWidgets.QLabel(self.centralwidget)
        self.label_104.setGeometry(QtCore.QRect(320, 40, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(14)
        font.setBold(False)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet("color: rgb(0,0,0);")
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(250, 90, 488, 42))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_81 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_29.addWidget(self.label_81)
        self.txt_consultaNoti = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.txt_consultaNoti.setMinimumSize(QtCore.QSize(250, 0))
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
        self.txt_consultaNoti.setObjectName("txt_consultaNoti")
        self.horizontalLayout_29.addWidget(self.txt_consultaNoti)
        self.btn_resumoInvestigacao = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_resumoInvestigacao.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_resumoInvestigacao.setFont(font)
        self.btn_resumoInvestigacao.setStyleSheet("QPushButton#btn_resumoInvestigacao{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_resumoInvestigacao:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_resumoInvestigacao:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagem/historia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_resumoInvestigacao.setIcon(icon)
        self.btn_resumoInvestigacao.setIconSize(QtCore.QSize(24, 24))
        self.btn_resumoInvestigacao.setObjectName("btn_resumoInvestigacao")
        self.horizontalLayout_29.addWidget(self.btn_resumoInvestigacao)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 201, 91))
        self.label_2.setStyleSheet("\n"
"image: url(:/Imagem/FNEA.jpg);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 140, 929, 452))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_85 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(11)
        font.setBold(True)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color: rgb(0,0,0);")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.verticalLayout_2.addWidget(self.label_85)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_99 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("color: rgb(0,0,0);")
        self.label_99.setObjectName("label_99")
        self.horizontalLayout_24.addWidget(self.label_99)
        self.txt_que = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_que.setEnabled(False)
        self.txt_que.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_que.setFont(font)
        self.txt_que.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_que.setObjectName("txt_que")
        self.horizontalLayout_24.addWidget(self.txt_que)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_100 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(0,0,0);")
        self.label_100.setObjectName("label_100")
        self.horizontalLayout_25.addWidget(self.label_100)
        self.txt_porque = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_porque.setEnabled(False)
        self.txt_porque.setMinimumSize(QtCore.QSize(411, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_porque.setFont(font)
        self.txt_porque.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_porque.setObjectName("txt_porque")
        self.horizontalLayout_25.addWidget(self.txt_porque)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_25)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_102 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("color: rgb(0,0,0);")
        self.label_102.setObjectName("label_102")
        self.horizontalLayout_27.addWidget(self.label_102)
        self.txt_quem = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_quem.setEnabled(False)
        self.txt_quem.setMinimumSize(QtCore.QSize(395, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_quem.setFont(font)
        self.txt_quem.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_quem.setObjectName("txt_quem")
        self.horizontalLayout_27.addWidget(self.txt_quem)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_103 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("color: rgb(0,0,0);")
        self.label_103.setObjectName("label_103")
        self.horizontalLayout_28.addWidget(self.label_103)
        self.txt_quando = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_quando.setEnabled(False)
        self.txt_quando.setMinimumSize(QtCore.QSize(405, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_quando.setFont(font)
        self.txt_quando.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_quando.setObjectName("txt_quando")
        self.horizontalLayout_28.addWidget(self.txt_quando)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_28)
        self.verticalLayout.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_98 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(0,0,0);")
        self.label_98.setObjectName("label_98")
        self.horizontalLayout_22.addWidget(self.label_98)
        self.txt_como = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_como.setEnabled(False)
        self.txt_como.setMinimumSize(QtCore.QSize(395, 0))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_como.setFont(font)
        self.txt_como.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_como.setObjectName("txt_como")
        self.horizontalLayout_22.addWidget(self.txt_como)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_101 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(11)
        font.setBold(True)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("color: rgb(0,0,0);")
        self.label_101.setAlignment(QtCore.Qt.AlignCenter)
        self.label_101.setObjectName("label_101")
        self.verticalLayout_10.addWidget(self.label_101)
        self.txt_conclusaoTime = QtWidgets.QTextEdit(self.layoutWidget)
        self.txt_conclusaoTime.setEnabled(False)
        self.txt_conclusaoTime.setMinimumSize(QtCore.QSize(921, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_conclusaoTime.setFont(font)
        self.txt_conclusaoTime.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_conclusaoTime.setObjectName("txt_conclusaoTime")
        self.verticalLayout_10.addWidget(self.txt_conclusaoTime)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.btn_sair_resumo = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sair_resumo.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_sair_resumo.setFont(font)
        self.btn_sair_resumo.setStyleSheet("QPushButton#btn_sair_resumo{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 39,119, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sair_resumo:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sair_resumo:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imagem/remover (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sair_resumo.setIcon(icon1)
        self.btn_sair_resumo.setIconSize(QtCore.QSize(24, 24))
        self.btn_sair_resumo.setObjectName("btn_sair_resumo")
        self.verticalLayout_3.addWidget(self.btn_sair_resumo)
        ui_investiga.setCentralWidget(self.centralwidget)

        self.retranslateUi(ui_investiga)
        QtCore.QMetaObject.connectSlotsByName(ui_investiga)
        ui_investiga.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        ui_investiga.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint,False)

    def retranslateUi(self, ui_investiga):
        _translate = QtCore.QCoreApplication.translate
        ui_investiga.setWindowTitle(_translate("ui_investiga", "RESUMO DA INVESTIGAÇÃO"))
        self.label_104.setText(_translate("ui_investiga", "RESUMO DA INVESTIGAÇÃO"))
        self.label_81.setText(_translate("ui_investiga", "Número da notificação"))
        self.btn_resumoInvestigacao.setToolTip(_translate("ui_investiga", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_resumoInvestigacao.setText(_translate("ui_investiga", "P E S Q U I S A R"))
        self.label_85.setText(_translate("ui_investiga", "Plano de Ação Executado:"))
        self.label_99.setText(_translate("ui_investiga", "O Que?"))
        self.label_100.setText(_translate("ui_investiga", "Por que?"))
        self.label_102.setText(_translate("ui_investiga", "Quem?"))
        self.label_103.setText(_translate("ui_investiga", "Quando?"))
        self.label_98.setText(_translate("ui_investiga", "Como?"))
        self.label_101.setText(_translate("ui_investiga", "Conclusão do Time:"))
        self.btn_sair_resumo.setText(_translate("ui_investiga", "S A I R"))
        
        self.btn_resumoInvestigacao.clicked.connect(self.ConsultaResumoInvestigacao)
        self.btn_sair_resumo.clicked.connect(ui_investiga.close)
        
    def ConsultaResumoInvestigacao(self):
        
        global cd_notificacao

        database="notiproducao"
        con = conexaoBD(bd = database)
                
        notificacao = self.txt_consultaNoti.text()

        if not self.txt_consultaNoti.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.Information)
            msg.setText("INFORME O NUMERO DA NOTIFICAÇÃO")
            msg.exec()
            return False

        resul = con.consultar("SELECT n.cd_notificacao,i.cd_notificacao, n.cd_paciente,n.nm_paciente, \
                i.pessoas,i.processos,i.amb_trabalho,i.materias_equipa,i.obs,i.recomendacoes,i.pg_o_que,i.pg_pq,i.pg_quem,i.pq_quando,i.pg_como,i.conclusao_time, i.status \
                         FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao\
                                 AND n.cd_notificacao ="+str(notificacao)+"  ")
        cd_notificacao = notificacao
        
        if resul == []:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("AVISO")
                msg.setText("NOTIFICAÇÃO SEM INVESTIGAÇÃO!!")
                msg.exec()
            
        for dt in resul:               
                        self.txt_que.setText(str(dt[10]))
                        self.txt_porque.setText(str(dt[11]))
                        self.txt_quem.setText(str(dt[12]))
                        self.txt_quando.setText(str(dt[13]))
                        self.txt_como.setText(str(dt[14]))
                        self.txt_conclusaoTime.setText(str(dt[15]))

