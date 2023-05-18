from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from FNEA.bd.conn import conexaoBD
from view.principal import con

 
def tabelaEmail(self):
    
    banco =self.comboBox_2.currentText()
    con = conexaoBD(bd = banco)
    consulta = self.txt_edita_email.text()
    email = con.consultar("SELECT email, idcontatos from contatos where email LIKE '%"+str(consulta)+"%' ") #BUSCA OS EMAILS CADASTRADOS NA TABELA
    self.tableWidget.setRowCount(0)
    for linha, texto in enumerate(email):
        self.tableWidget.insertRow(linha)
        for coluna, dados in enumerate(texto):
            self.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados)))
            

    self.tableWidget.verticalHeader().setVisible(False)
    self.txt_edita_email.setText(str(texto[1]))
    self.txt_email.setText(str(texto[0]))
   
    
    
    

