from FNEA.bd.conn import conexaoBD
from PyQt5.QtWidgets import QMessageBox

def inserir_usuarios_FNEA(self):
        nome = self.txt_cadnome_4.text()
        username = self.txt_cadnome_5.text()
        senha = self.txt_cadnome_6.text()
        perfil = self.cb_outros_4.currentText()

        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        if not self.txt_cadnome_4.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME O CODIGO O NOME DO FUNCIONARIO")
            msg.exec()

        elif not self.txt_cadnome_5.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME O USUARIO")
            msg.exec()

        elif not self.txt_cadnome_6.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME A SENHA")
            msg.exec()

        elif not self.cb_outros_4.currentText():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME O PERFIL")
            msg.exec()
        else:
            con.manipular("INSERT INTO usuario (nome, username, senha, perfil)VALUES('" +
                                  nome + "','" + username + "','" + senha + "','" + perfil + "')")
            
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Dados Cadastrados com Sucesso")
            msg.exec()
            limparcamposUsuario(self)

def alterUserFnea(self):
        global cd_usuario
        nome = self.txt_cadnome_4.text()
        senha = self.txt_cadnome_6.text()
        perfil = self.cb_outros_4.currentText()
        username = self.txt_cadnome_5.text()
        user = self.txt_consultaUser_2.text()

        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        resul = con.manipular("UPDATE usuario SET nome = '{}', senha = '{}', perfil = '{}' WHERE  username ='{}'".format(
            nome, senha, perfil, username))

        if resul == 1:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Dados alterados com Sucesso")
            msg.exec()
            limparcamposUsuario(self)            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Erro ao atualizar usuário, favor verifique os dados")
            msg.exec()

def cancelar(self):
        self.txt_cadnome_4.setText("")
        self.txt_cadnome_5.setText("")
        self.txt_cadnome_6.setText("")

        self.cb_outros_4.setCurrentIndex(-1)
        self.txt_cadnome_4.setEnabled(False)
        self.txt_cadnome_5.setEnabled(False)
        self.txt_cadnome_6.setEnabled(False)

        self.cb_outros_4.setEnabled(False)
        self.btn_salvaUser_2.setEnabled(False)
        self.btn_cancelaUser_2.setEnabled(False)

def limparcamposUsuario(self):
        self.txt_cadnome_4.setText("")
        self.txt_cadnome_5.setText("")
        self.txt_cadnome_6.setText("")
        self.cb_outros_4.setCurrentIndex(-1)
        self.txt_cadnome_4.setEnabled(False)
        self.txt_cadnome_5.setEnabled(False)
        self.txt_cadnome_6.setEnabled(False)
        self.cb_outros_4.setEnabled(False)
        self.btn_salvaUser_2.setEnabled(False)
        self.btn_cancelaUser_2.setEnabled(False)

def habilitaCampos(self):
        self.txt_cadnome_4.setText("")
        self.txt_cadnome_5.setText("")
        self.txt_cadnome_6.setText("")

        self.cb_outros_4.setCurrentIndex(-1)
        self.txt_cadnome_4.setEnabled(True)
        self.txt_cadnome_5.setEnabled(True)
        self.txt_cadnome_6.setEnabled(True)
        self.cb_outros_4.setEnabled(True)
        

        self.cb_outros_4.setEnabled(True)
        self.btn_salvaUser_2.setEnabled(True)
        self.btn_cancelaUser_2.setEnabled(True)

def editarUsuario(self):
        self.txt_cadnome_4.setEnabled(True)
        self.txt_cadnome_6.setEnabled(True)
        self.cb_outros_4.setEnabled(True)
        self.btn_cancelaUser_2.setEnabled(True)