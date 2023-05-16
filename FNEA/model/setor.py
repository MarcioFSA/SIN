from FNEA.bd.conn import conexaoBD
from PyQt5.QtWidgets import QMessageBox

def inserirSetor(self):
        setor = self.txt_setor.text()
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        if not self.txt_setor.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME O SETOR QUE SERÁ CADASTRADO")
            msg.exec()
        
        else:
            con.manipular("INSERT INTO SETORES (setor) VALUES('" +
                                  setor + "')")
            
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Setor Cadastrado com Sucesso")
            msg.exec()
            self.txt_setor.clear()
            self.txt_setor.setEnabled(False)
            self.txt_setor_pesquisa.setEnabled(False)

def novoSetor(self):
     self.txt_setor.setEnabled(True)

def cancelaSetor(self):
     self.txt_setor.setEnabled(False)
     self.txt_setor.clear()
