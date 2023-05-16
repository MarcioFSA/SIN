from FNEA.bd.conn import conexaoBD
from PyQt5 import QtGui, QtWidgets
from distutils.log import error

def consultaInvestigacao(self):

    resul = []
    self.tb_consulta_4.clear()
    self.tb_consulta_4.setRowCount(0)

    banco =self.comboBox_2.currentText()
    con = conexaoBD(bd = banco)

    paciente = self.txt_consultapStatus.text()
    cd_notificacao = 1

    if self.radioButton_11.isChecked():
            resul = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y'),DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y'),DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Em Andamento' AND (n.cd_paciente LIKE '%" +
                                  str(paciente)+"%' OR n.nm_paciente LIKE '%"+str(paciente)+"%');")
        
            for row_number, row_data in enumerate(resul):
                self.tb_consulta_4.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tb_consulta_4.setItem(
                        row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                    self.tb_consulta_4.setColumnWidth(0, 30)
                    self.tb_consulta_4.setColumnWidth(1, 30)
                    self.tb_consulta_4.setColumnWidth(2, 320)
                    self.tb_consulta_4.setColumnWidth(3, 80)
                    self.tb_consulta_4.setColumnWidth(4, 200)
                    self.tb_consulta_4.setColumnWidth(5, 60)
                    self.tb_consulta_4.setColumnWidth(6, 125)
                    self.tb_consulta_4.setColumnWidth(7, 125)

                    self.tb_consulta_4.resizeRowsToContents()

                    self.tb_consulta_4.setHorizontalHeaderLabels(
                            ['CodN', 'CodP', 'Paciente', 'Sexo', 'Unidade Internação', 'Cod-Inv', 'Data Evento', 'Data Notificação','Data Inicio','Ultima Atual.'])

                    self.tb_consulta_4.verticalHeader().setVisible(False)

    elif self.radioButton_12.isChecked():
            resul = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Com Pendências' AND (n.cd_paciente LIKE '%" +
                                  str(paciente)+"%' OR n.nm_paciente LIKE '%"+str(paciente)+"%');")
        
            for row_number, row_data in enumerate(resul):
                self.tb_consulta_4.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tb_consulta_4.setItem(
                        row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                    self.tb_consulta_4.setColumnWidth(0, 30)
                    self.tb_consulta_4.setColumnWidth(1, 30)
                    self.tb_consulta_4.setColumnWidth(2, 320)
                    self.tb_consulta_4.setColumnWidth(3, 80)
                    self.tb_consulta_4.setColumnWidth(4, 200)
                    self.tb_consulta_4.setColumnWidth(5, 60)
                    self.tb_consulta_4.setColumnWidth(6, 125)
                    self.tb_consulta_4.setColumnWidth(7, 125)

                    self.tb_consulta_4.resizeRowsToContents()

                    self.tb_consulta_4.setHorizontalHeaderLabels(
                            ['CodN', 'CodP', 'Paciente', 'Sexo', 'Unidade Internação', 'Cod-Inv', 'Data Evento', 'Data Notificação','Data Inicio','Ultima Atual.'])

                    self.tb_consulta_4.verticalHeader().setVisible(False)

    elif self.radioButton_13.isChecked():
            resul = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,n.dt_evento, n.dt_notificacao FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Concluído' AND (n.cd_paciente LIKE '%" +
                                  str(paciente)+"%' OR n.nm_paciente LIKE '%"+str(paciente)+"%');")
        
            for row_number, row_data in enumerate(resul):
                self.tb_consulta_4.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tb_consulta_4.setItem(
                        row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                    self.tb_consulta_4.setColumnWidth(0, 30)
                    self.tb_consulta_4.setColumnWidth(1, 30)
                    self.tb_consulta_4.setColumnWidth(2, 320)
                    self.tb_consulta_4.setColumnWidth(3, 80)
                    self.tb_consulta_4.setColumnWidth(4, 200)
                    self.tb_consulta_4.setColumnWidth(5, 60)
                    self.tb_consulta_4.setColumnWidth(6, 125)
                    self.tb_consulta_4.setColumnWidth(7, 125)

                    self.tb_consulta_4.resizeRowsToContents()

                    self.tb_consulta_4.setHorizontalHeaderLabels(
                            ['CodN', 'CodP', 'Paciente', 'Sexo', 'Unidade Internação', 'Cod-Inv', 'Data Evento', 'Data Notificação','Data Inicio','Ultima Atual.'])

                    self.tb_consulta_4.verticalHeader().setVisible(False)

    else:
                    resul = []
                    self.tb_consulta_4.clear()
                    self.tb_consulta_4.setRowCount(0)

                    banco =self.comboBox_2.currentText()
                    con = conexaoBD(bd = banco)

                    paciente = self.txt_consultapStatus.text()

                    resul = con.consultar("SELECT n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao, DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n LEFT JOIN  investigacao i ON n.cd_notificacao = i.cd_notificacao WHERE i.cd_notificacao IS NULL AND (n.cd_paciente LIKE '%" +
                                      str(paciente)+"%' OR n.nm_paciente LIKE '%"+str(paciente)+"%');")

                    for row_number, row_data in enumerate(resul):
                        self.tb_consulta_4.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                            self.tb_consulta_4.setItem(
                                row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                    self.tb_consulta_4.setColumnWidth(0, 30)
                    self.tb_consulta_4.setColumnWidth(1, 30)
                    self.tb_consulta_4.setColumnWidth(2, 300)
                    self.tb_consulta_4.setColumnWidth(3, 80)
                    self.tb_consulta_4.setColumnWidth(4, 200)
                    self.tb_consulta_4.setColumnWidth(5, 60)
                    self.tb_consulta_4.setColumnWidth(6, 125)
                    self.tb_consulta_4.setColumnWidth(7, 125)

                    self.tb_consulta_4.setHorizontalHeaderLabels(
                                    ['CodN', 'CodP', 'Paciente', 'Sexo', 'Unidade Internação', 'Cod-Inv', 'Data Evento', 'Data Notificação','Data Inicio','Ultima Atual.'])

                    self.tb_consulta_4.verticalHeader().setVisible(False)


def consultaUsuariosFnea(self):
        try:
            banco =self.comboBox_2.currentText()    
            con = conexaoBD(bd = banco)

            nome= self.txt_consultaUser_2.text()
            resul = con.consultar(
                "SELECT nome, username, perfil, senha FROM usuario where nome LIKE '%"+str(nome)+"%'")
            self.tableWidget_2.setRowCount(0)
            
            for row_number, row_data in enumerate(resul):
                self.tableWidget_2.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, colum_number,
                                             QtWidgets.QTableWidgetItem(str(data)))
                    self.txt_cadnome_4.setText(str(row_data[0]))
                    self.txt_cadnome_5.setText(str(row_data[1]))
                    self.txt_cadnome_6.setText(str(row_data[3]))
                    self.cb_outros_4.setCurrentText(str(row_data[2]))
                    self.btn_editaUser_2.setEnabled(True)
                    self.btn_alterarUser_2.setEnabled(True)

            self.tableWidget_2.setStyleSheet(
                "background-color: rgb(240,248,255);\n")

        except AttributeError:
            print("Erro ao consultar ao BD", error)

def tabelaEmail(self):
    try:
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        email = self.txt_edita_email.text()
        resul = con.consultar("SELECT idcontatos, email from contatos where email LIKE '%"+str(email)+"%' ") #BUSCA OS EMAILS CADASTRADOS NA TABELA
        # print(email)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(resul):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                 self.tableWidget.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(row_data[1])))
        self.tableWidget.verticalHeader().setVisible(False)
        # self.txt_edita_email.setText(str(row_data[1]))
        # self.txt_email.setText(str(texto[1]))

    except AttributeError:
            print("Erro ao consultar ao BD", error)

def tabelaSetor(self):
    try:
        banco =self.comboBox_2.currentText()    
        con = conexaoBD(bd = banco)

        setor= self.txt_setor.text()
        setores = con.consultar("SELECT setor from setores where setor LIKE '%"+str(setor)+"%' ")
        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(setores):
                self.tableWidget_3.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_number, colum_number,
                                             QtWidgets.QTableWidgetItem(str(data)))
                    
        self.tableWidget_3.verticalHeader().setVisible(False)
        # self.btn_pesquisar_setor.
                    
    except AttributeError:
            print("Erro ao consultar ao BD", error)
                      



