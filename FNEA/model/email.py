from FNEA.bd.conn import conexaoBD
from FNEA.model.consulta import *
from PyQt5.QtWidgets import QMessageBox

idcontatos = 0
def enviarEmailleve(self):
    import smtplib
    from email.message import EmailMessage
    banco = self.comboBox_2.currentText()
    con = conexaoBD(bd=banco)
    resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
    dados = list()
    dados.append(str(resultado[0][0]))
    num_noti = str("".join(dados))
    contatos = con.consultar("SELECT email from contatos")
    for email in contatos:
        print(email)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.subject('NOVA NOTIFICAÇÃO FNEA -EVENTO ADVERSO - LEVE ')
        server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
        server.sendmail('sender@example.com', email, 'Um novo Evento Adverso de Grau Leve foi cadastrado no FNEA. ')
        server.quit()

def enviarEmailModerado(self):
            import smtplib
            from email.message import EmailMessage
            banco = self.comboBox_2.currentText()
            con = conexaoBD(bd=banco)
            resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
            dados = list()
            dados.append(str(resultado[0][0]))
            num_noti = str("".join(dados))

            contatos = con.consultar("SELECT email from contatos")
            for email in contatos:
                print(email)

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                # server.subject('NOVA NOTIFICAÇÃO FNEA -EVENTO ADVERSO - LEVE ')
                server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
                server.sendmail('sender@example.com', email,
                                'Um novo Evento Adverso de Grau MODERADO foi cadastrado no FNEA. ')
                server.quit()


def enviarEmailGrave(self):
    import smtplib
    from email.message import EmailMessage
    banco = self.comboBox_2.currentText()
    con = conexaoBD(bd=banco)
    resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
    dados = list()
    dados.append(str(resultado[0][0]))
    num_noti = str("".join(dados))

    contatos = con.consultar("SELECT email from contatos")
    for email in contatos:
        print(email)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.subject('NOVA NOTIFICAÇÃO FNEA -EVENTO ADVERSO - LEVE ')
        server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
        server.sendmail('sender@example.com', email, 'Um novo Evento Adverso de GRAVE foi cadastrado no FNEA. ')
        server.quit()


def enviarEmailObito(self):
    import smtplib
    from email.message import EmailMessage
    banco = self.comboBox_2.currentText()
    con = conexaoBD(bd=banco)
    resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
    dados = list()
    dados.append(str(resultado[0][0]))
    num_noti = str("".join(dados))

    contatos = con.consultar("SELECT email from contatos")
    for email in contatos:
        print(email)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.subject('NOVA NOTIFICAÇÃO FNEA -EVENTO ADVERSO - LEVE ')
        server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
        server.sendmail('sender@example.com', email, 'Um novo Evento Adverso de ÓBITO foi cadastrado no FNEA. ')
        server.quit()

def novo_email(self):
     self.txt_email.setEnabled(True)
     self.txt_email.clear()
     self.btn_alterar_email.setEnabled(True)

def inserir_email(self):
        email = self.txt_email.text()
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        if not self.txt_email.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            # msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME E-MAIL QUE SERÁ CADASTRADO")
            msg.exec()
        
        else:
            con.manipular("INSERT INTO CONTATOS (email) VALUES('" +
                                  email + "')")
            
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Dados Cadastrados com Sucesso")
            msg.exec()
            limparCampoEmail(self)


def alterarEmail(self):
        global idcontatos
        email = self.txt_edita_email.text()
        
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        resul = con.manipular("UPDATE contatos SET email = '{}'".format(
            email))

        if resul == 1:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("E-mail alterado com Sucesso")
            msg.exec()
            limparCampoEmail(self)            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Erro ao atualizar usuário, favor verifique os dados")
            msg.exec()

    

def limparCampoEmail(self):
    self.txt_email.setText("")
    self.txt_edita_email.setText("")
    tabelaEmail(self)

def excluirEmail(self):
     email = self.txt_edita_email.text()
     banco = self.comboBox_2.currentText()
     con = conexaoBD(bd = banco)
     resul = con.manipular("DELETE from contatos WHERE email ='{}'".format( email))

     msg = QMessageBox()
     msg.setWindowTitle("AVISO")
     msg.setText("E-mail excluido com sucesso")
     msg.exec()
     limparCampoEmail(self)

def cancelaEmail(self):
    self.txt_email.setText("")
    self.txt_email.setEnabled(False)

    
