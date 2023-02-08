from PyQt5.QtWidgets import QDesktopWidget, QMessageBox

from FNEA.bd.conn import conexaoBD


def AlterarInvestigacao(self):
        
        self.btn_alterarInv.setEnabled(True)
        self.txt_processos.setEnabled(True)
        self.txt_pessoas.setEnabled(True)
        self.txt_equipamentos.setEnabled(True)
        self.txt_ambiente.setEnabled(True)
        self.txt_observacao.setEnabled(True)
        self.txt_recomendacao.setEnabled(True)
        self.txt_pessoas_2.setEnabled(True)
        self.txt_pessoas_3.setEnabled(True)
        self.txt_pessoas_4.setEnabled(True)
        self.txt_pessoas_5.setEnabled(True)
        self.txt_pessoas_6.setEnabled(True)
        self.txt_recomendacao_2.setEnabled(True)
        self.btn_consultar.setEnabled(False)
        self.btn_relatorio.setEnabled(False)
        self.btn_dashboard.setEnabled(False)
        self.btn_notifica.setEnabled(False)
        self.btn_logoff.setEnabled(False)
        
        

def iniciandoInvestigacao(self):
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao.clear()
        self.txt_recomendacao_2.clear()
        self.txt_pessoas_2.clear()
        self.txt_pessoas_3.clear()
        self.txt_pessoas_4.clear()
        self.txt_pessoas_5.clear()
        self.txt_pessoas_6.clear()
        self.txt_recomendacao.clear()
        self.txt_recomendacao_2.clear()
        
        self.txt_pessoas.setEnabled(True)
        self.txt_processos.setEnabled(True)
        self.txt_ambiente.setEnabled(True)
        self.txt_equipamentos.setEnabled(True)
        self.txt_observacao.setEnabled(True)
        self.txt_recomendacao_2.setEnabled(True)
        self.txt_pessoas_2.setEnabled(True)
        self.txt_pessoas_3.setEnabled(True)
        self.txt_pessoas_4.setEnabled(True)
        self.txt_pessoas_5.setEnabled(True)
        self.txt_pessoas_6.setEnabled(True)
        self.txt_recomendacao.setEnabled(True)
        self.txt_recomendacao_2.setEnabled(True)
        self.btn_conclusao.setEnabled(True)
        self.btn_notifica.setEnabled(False)
        self.btn_consultar.setEnabled(False)
        self.btn_relatorio_2.setEnabled(False)
        self.btn_relatorio.setEnabled(False)
        self.btn_dashboard.setEnabled(False)
        
        self.btn_alterarInv.setEnabled(False)
        #self.radioButton.setChecked(True)

def cancelarReabilitarCampos(self):
        
        self.txt_paciente.clear()
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao.clear()        
        self.txt_pessoas_2.clear()
        self.txt_pessoas_3.clear()
        self.txt_pessoas_4.clear()
        self.txt_pessoas_5.clear()
        self.txt_pessoas_6.clear()
        self.txt_recomendacao.clear()
        self.txt_recomendacao_2.clear()
        
        self.txt_pessoas.setEnabled(False)
        self.txt_processos.setEnabled(False)
        self.txt_ambiente.setEnabled(False)
        self.txt_equipamentos.setEnabled(False)
        self.txt_observacao.setEnabled(False)        
        self.txt_pessoas_2.setEnabled(False)
        self.txt_pessoas_3.setEnabled(False)
        self.txt_pessoas_4.setEnabled(False)
        self.txt_pessoas_5.setEnabled(False)
        self.txt_pessoas_6.setEnabled(False)
        self.txt_recomendacao.setEnabled(False)
        self.txt_recomendacao_2.setEnabled(False)

        self.btn_notifica.setEnabled(True)
        self.btn_consultar.setEnabled(True)
        self.btn_relatorio_2.setEnabled(True)
        self.btn_relatorio.setEnabled(True)
        self.btn_dashboard.setEnabled(True)
        self.btn_dashboard.setEnabled(True)
        
        self.btn_conclusao.setEnabled(False)
        self.btn_consultar.setEnabled(True)
        self.btn_relatorio.setEnabled(True)
        self.btn_dashboard.setEnabled(True)
        self.btn_notifica.setEnabled(True)
        self.btn_logoff.setEnabled(True)
        self.btn_alterarInv.setEnabled(False)
        self.txt_paciente_3.clear()


def limparcamposInvestigacao(self):
        
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao.clear()
        self.txt_recomendacao_2.clear()
        self.txt_pessoas_2.clear()
        self.txt_pessoas_3.clear()
        self.txt_pessoas_4.clear()
        self.txt_pessoas_5.clear()
        self.txt_pessoas_6.clear()
        self.txt_recomendacao.clear()
        self.txt_recomendacao_2.clear()

def desabilitaCampos(self):
        
        self.txt_pessoas.setEnabled(False)
        self.txt_processos.setEnabled(False)
        self.txt_ambiente.setEnabled(False)
        self.txt_equipamentos.setEnabled(False)
        self.txt_observacao.setEnabled(False)
        self.txt_recomendacao_2.setEnabled(False)
        self.txt_pessoas_2.setEnabled(False)
        self.txt_pessoas_3.setEnabled(False)
        self.txt_pessoas_4.setEnabled(False)
        self.txt_pessoas_5.setEnabled(False)
        self.txt_pessoas_6.setEnabled(False)
        self.txt_recomendacao.setEnabled(False)
        self.txt_recomendacao_2.setEnabled(False)

def ConsultaResumoInvestigacao(self):
        
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)
        paciente = self.txt_paciente_2.text()

        if not self.txt_consultaNoti.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.Information)
            msg.setText("INFORME O NUMERO DA NOTIFICAÇÃO")
            msg.exec()
        
        else:
            banco =self.comboBox_2.currentText()
            con = conexaoBD(bd = banco)
            paciente = self.txt_paciente_4.text()

            resul = con.consultar("SELECT n.cd_notificacao,i.cd_notificacao, n.cd_paciente,n.nm_paciente, \
                i.pessoas,i.processos,i.amb_trabalho,i.materias_equipa,i.obs,i.recomendacoes,i.pg_o_que,i.pg_pq,i.pg_quem,i.pq_quando,i.pg_como,i.conclusao_time, i.status \
                         FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao\
                                 AND n.cd_notificacao ="+str(paciente)+"  ")
            cd_paciente = paciente

            vazio = []
            if resul == vazio:
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
                        print(resul)
                        print(dt)
                        

        



        
        
        
