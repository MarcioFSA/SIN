from FNEA.bd.conn import conexaoBD
from PyQt5.QtWidgets import QMessageBox
from FNEA.relatorio.manip_dados import Relatorio

def gerarPdf(self):
        if not self.txt_consultaNoti.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("INFORME O CODIGO DA NOTIFICAÇÃO")
            msg.exec()
        else:
            report = Relatorio()
            report.setCodNotificao(self.txt_consultaNoti.text())
            report.savePDF(bd =self.comboBox_2.currentText()) 

