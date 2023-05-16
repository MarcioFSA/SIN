from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FNEA.bd.conn import conexaoBD
# from cryptography.fernet import Fernet
# from win32api import GetKeyState
# from win32con import VK_CAPITAL
from FNEA.model.usuarios import *

def validarLogin(self):

    nome_usuario = self.lineEdit.text()
    senha = self.lineEdit_2.text()

    if not nome_usuario:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("AVISO")
        msg.setText("INFORME O NOME DO USUÁRIO")
        msg.exec()
        return False


    elif not senha:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("AVISO")
        msg.setText("INFORME A SENHA DO USUÁRIO")
        msg.exec()
        return False

    else:
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd=banco)
        resul = con.consultar(
            "SELECT  senha, cd_usuario,perfil,username  FROM usuario WHERE username ='{}'".format(nome_usuario))
        vazio = []
        if resul == vazio:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("AVISO")
            msg.setText("USUARIO OU SENHA INVÁLIDOS")
            msg.exec()

        else:

            if senha == resul[0][0]:
                dados = list()
                dados.append(str(resul[0][2]))

                for i in dados:
                    if i == 'Administrador':
                        self.btn_usuarios.setEnabled(True)
                        self.btn_dashboard.setVisible(True)
                        self.btn_dashboard.setEnabled(True)
                        self.btn_investigar.setEnabled(True)
                        self.btn_notifica.setVisible(True)
                        self.btn_investigar.setVisible(True)
                        self.btn_consultar.setVisible(True)
                        self.btn_relatorio.setVisible(True)
                        self.btn_relatorio_2.setVisible(True)
                        self.btn_usuarios.setVisible(True)
                        self.btn_relatorio.setEnabled(True)
                        self.btn_usuarios.setEnabled(True)
                        self.btn_notificar.setEnabled(True)
                        self.btn_setor.setEnabled(True)
                        self.btn_email.setEnabled(True)
                        self.btn_relatorio.setEnabled(True)
                        self.comboBox.setEnabled(True)
                        

                        self.stackedWidget.setCurrentWidget(self.page_6)

                    if i == 'Investigador N1':
                        self.stackedWidget.setCurrentWidget(self.page_6)
                        self.btn_dashboard.setVisible(True)
                        self.btn_dashboard.setEnabled(True)
                        self.btn_notifica.setVisible(True)
                        self.btn_investigar.setVisible(True)
                        self.btn_investigar.setEnabled(True)
                        self.btn_consultar.setVisible(True)
                        self.comboBox.setEnabled(False)
                        self.btn_notificar.setEnabled(True)
                        self.btn_usuarios.setEnabled(False)
                        self.btn_setor.setEnabled(False)
                        self.btn_email.setEnabled(False)
                        self.btn_relatorio.setEnabled(True)
                        

                    if i == 'Investigador N2':
                        self.stackedWidget.setCurrentWidget(self.page_6)
                        self.btn_dashboard.setVisible(True)
                        self.btn_dashboard.setEnabled(True)
                        self.btn_notifica.setVisible(True)
                        self.btn_investigar.setVisible(True)
                        self.btn_investigar.setEnabled(True)
                        self.btn_consultar.setVisible(True)
                        self.comboBox.setEnabled(False)
                        self.btn_notificar.setEnabled(True)
                        self.comboBox.setEnabled(True)
                        
                        self.btn_relatorio.setEnabled(True)
                        self.btn_relatorio.setVisible(True)
                        self.btn_usuarios.setEnabled(False)
                        self.btn_setor.setEnabled(False)
                        self.btn_email.setEnabled(False)
                        
                        self.comboBox.setEnabled(True)
                    
                        # self.stackedWidget.setCurrentWidget(self.page_6)
                        # self.btn_dashboard.setVisible(True)
                        # self.btn_dashboard.setEnabled(True)
                        # self.btn_notifica.setVisible(True)
                        # self.btn_investigar.setVisible(True)
                        # self.btn_investigar.setEnabled(True)
                        # self.btn_consultar.setVisible(True)
                        # self.comboBox.setEnabled(True)
                        # self.btn_relatorio.setEnabled(True)
                        # self.btn_relatorio.setVisible(True)
                        # self.btn_resumo.setEnabled(True)
                        # self.comboBox.setEnabled(True)
                        # self.btn_notificar.setEnabled(True)

                    if i == 'Notificador':
                        self.stackedWidget.setCurrentWidget(self.page_6)
                        self.btn_notifica.setVisible(True)
                        self.btn_dashboard.setVisible(True)
                        self.btn_notifica.setVisible(True)
                        self.btn_notificar.setEnabled(True)
                        self.btn_usuarios.setEnabled(False)
                        self.btn_setor.setEnabled(False)
                        self.btn_email.setEnabled(False)
                        self.btn_relatorio.setEnabled(False)
                        self.btn_tratativa.setEnabled(False)

                    else:
                        self.btn_dashboard.setVisible(True)
                        self.btn_dashboard.setEnabled(True)

                    if senha == resul[0][0]:
                        dados = list()
                        dados.append(str(resul[0][3]))

                        user = "".join(dados)

                        self.logado.setText(str(user))
                    else:
                        self.logado.setText('anonimo')