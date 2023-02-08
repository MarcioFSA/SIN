from FNEA.bd.conn import conexaoBD
from FNEA.model.login import *


def preencherCBfnea(self):
    banco = self.comboBox_2.currentText()
    con = conexaoBD(bd=banco)
    setores = con.consultar("SELECT setor from setores")  # BUSCA OS SETORES CADASTRADOS NA TABELA
    for item in setores:
        self.cb_seto.addItems(item)  # ADICIONA OS ITENS ENCONTRADOS A COMBOBOX