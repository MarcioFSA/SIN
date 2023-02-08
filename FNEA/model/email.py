from FNEA.bd.conn import conexaoBD


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