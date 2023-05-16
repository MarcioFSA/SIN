from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from FNEA.bd.conn import conexaoBD
import datetime
# from FNEA.bd.conn import conexaoBD
# from FNEA.view.principal import con

def iniciarinvestigacao(self):
        global cd_notificacao
        
        if not self.txt_paciente_3.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.Information)
            msg.setText("INFORME O NUMERO DA NOTIFICAÇÃO QUE DESEJA INVESTIGAR")
            msg.exec()
        
        else:
            self.txt_paciente_4.clear()
            banco =self.comboBox_2.currentText()    
            con = conexaoBD(bd = banco)
            notificacao = self.txt_paciente_3.text()
            resul = con.consultar("SELECT cd_notificacao, nm_paciente FROM notificacao WHERE cd_notificacao ="+str(notificacao)+"")
            
            vazio = []
            if resul == vazio:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("AVISO")
                msg.setText("NOTIFICAÇÃO NÃO LOCAZIDADA!\nPOR FAVOR VERIFIQUE O CÓDIGO INFORMADO E TENTE NOVAMENTE.")
                msg.exec()

            banco =self.comboBox_2.currentText()    
            con = conexaoBD(bd = banco)
            notificacao = self.txt_paciente_3.text()
            resul2 = con.consultar("SELECT cd_notificacao FROM investigacao WHERE cd_notificacao ="+str(notificacao)+"")

            if resul2 == vazio:
                for dt in resul:
                        self.txt_paciente.setText(str(dt[1]))
                        iniciandoInvestigacao(self)               
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("AVISO")
                msg.setText("A NOTIFICAÇÃO INFORMADA JÁ POSSUI UMA INVESTIGAÇÃO EM ANDAMENTO!")
                msg.exec()

            resul = con.consultar("SELECT n.cd_paciente,n.nm_paciente,n.ds_ocorrencia FROM notificacao n WHERE n.cd_notificacao = "+str(notificacao)+"")

            cd_notificacao = notificacao
                
            if resul == []:
                        msg = QMessageBox()
                        msg.setWindowTitle("AVISO")
                        msg.setText("NOTIFICAÇÃO NÃO ENCONTRADA!")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec()

            if(resul):
                        for dt in resul:              
                                self.txt_codPaciente.setText(str(dt[0]))
                                self.txt_nmPaciente.setText(str(dt[1]))
                                self.txt_resumo_ocorrencia.setText(str(dt[2]))

def iniciandoInvestigacao(self):
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao_2.clear()
        self.txt_recomendacao_4.clear()
        self.txt_pessoas_8.clear()
        self.txt_pessoas_9.clear()
        self.txt_pessoas_10.clear()
        self.txt_pessoas_11.clear()
        self.txt_pessoas_12.clear()
        self.txt_recomendacao_3.clear()
        
        
        self.txt_pessoas.setEnabled(True)
        self.txt_processos.setEnabled(True)
        self.txt_ambiente.setEnabled(True)
        self.txt_equipamentos.setEnabled(True)
        self.txt_observacao_2.setEnabled(True)
        self.txt_recomendacao_4.setEnabled(True)
        self.txt_pessoas_8.setEnabled(True)
        self.txt_pessoas_9.setEnabled(True)
        self.txt_pessoas_10.setEnabled(True)
        self.txt_pessoas_11.setEnabled(True)
        self.txt_pessoas_12.setEnabled(True)
        self.txt_recomendacao_3.setEnabled(True)
        self.btn_conclusao_2.setEnabled(True)
        self.btn_voltar_2.setEnabled(False)
        self.btn_alterarInv_2.setEnabled(False)
        self.btn_editarInv.setEnabled(False)
        self.comboBox.setCurrentIndex(-1)

def cancelarReabilitarCampos(self):
        
        self.txt_paciente.clear()
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao_2.clear()
        self.txt_recomendacao_4.clear()
        self.txt_pessoas_8.clear()
        self.txt_pessoas_9.clear()
        self.txt_pessoas_10.clear()
        self.txt_pessoas_11.clear()
        self.txt_pessoas_12.clear()
        self.txt_recomendacao_3.clear()
        
        
        self.txt_pessoas.setEnabled(False)
        self.txt_processos.setEnabled(False)
        self.txt_ambiente.setEnabled(False)
        self.txt_equipamentos.setEnabled(False)
        self.txt_observacao_2.setEnabled(False)
        self.txt_recomendacao_4.setEnabled(False)
        self.txt_pessoas_8.setEnabled(False)
        self.txt_pessoas_9.setEnabled(False)
        self.txt_pessoas_10.setEnabled(False)
        self.txt_pessoas_11.setEnabled(False)
        self.txt_pessoas_12.setEnabled(False)
        self.txt_recomendacao_3.setEnabled(False)

        self.txt_codPaciente.clear()
        self.txt_nmPaciente.clear()
        self.txt_resumo_ocorrencia.clear()

        self.btn_conclusao_2.setEnabled(False)
        self.btn_voltar_2.setEnabled(True)
        self.btn_alterarInv_2.setEnabled(True)
        self.btn_editarInv.setEnabled(True)


def salvarInvestigacao(self):
        user = str(self.logado.text())
        codNotifi = self.txt_paciente.text()
        pessoas = self.txt_pessoas.text()
        processos = self.txt_processos.text()
        amb_trabalho = self.txt_ambiente.text()
        materias_equipa = self.txt_equipamentos.text()
        obs = self.txt_observacao_2.toPlainText()
        recomendacoes = self.txt_recomendacao_4.toPlainText()
        pg_o_que = self.txt_pessoas_8.text()
        pg_pq = self.txt_pessoas_9.text()
        pg_quem = self.txt_pessoas_10.text()
        pq_quando = self.txt_pessoas_11.text()
        pg_como = self.txt_pessoas_12.text()
        conclusao_time = self.txt_recomendacao_3.toPlainText()
        cd_notificacao = self.txt_paciente_3.text()

        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)
        

        con.manipular("INSERT INTO investigacao (cd_notificacao,investigador, pessoas, processos, amb_trabalho, materias_equipa, obs, recomendacoes,pg_o_que,pg_pq,pg_quem,pq_quando,pg_como,conclusao_time,status,dt_cad_cadastro)VALUES('"+cd_notificacao+"','"+user+"','" +
                              pessoas+"', '"+processos+"', '"+amb_trabalho+"', '"+materias_equipa+"', '"+obs+"', '"+recomendacoes+"','"+pg_o_que+"','"+pg_pq+"','"+pg_quem+"','"+pq_quando+"','"+pg_como+"','"+conclusao_time+"','Em andamento',NOW())")

        msg = QMessageBox()
        msg.setWindowTitle("AVISO")
        msg.setText("Investigação Cadastrada com Sucesso")
        msg.exec()
        cancelarReabilitarCampos(self)
        self.comboBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.txt_paciente_3.clear()

def buscarInvestigacao(self):
        global cd_notificacao
        
        self.txt_paciente_3.clear()
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao_2.clear()
        self.txt_recomendacao_4.clear()
        self.txt_pessoas_9.clear()
        self.txt_pessoas_9.clear()
        self.txt_pessoas_10.clear()
        self.txt_pessoas_11.clear()
        self.txt_pessoas_12.clear()
        self.txt_recomendacao_3.clear()
        

        if not self.txt_paciente_4.text():
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
                    
                        self.txt_paciente.setText(str(dt[3]))
                        self.txt_pessoas.setText(str(dt[4]))
                        self.txt_processos.setText(str(dt[5]))
                        self.txt_ambiente.setText(str(dt[6]))
                        self.txt_equipamentos.setText(str(dt[7]))
                        self.txt_observacao_2.setText(str(dt[8]))
                        self.txt_recomendacao_4.setText(str(dt[9]))
                        self.txt_pessoas_8.setText(str(dt[10]))
                        self.txt_pessoas_9.setText(str(dt[11]))
                        self.txt_pessoas_10.setText(str(dt[12]))
                        self.txt_pessoas_11.setText(str(dt[13]))
                        self.txt_pessoas_12.setText(str(dt[14]))
                        self.txt_recomendacao_3.setText(str(dt[15]))
                        self.comboBox.setCurrentText(str(dt[16]))

            notificacao = self.txt_paciente_4.text()
            resul = con.consultar("SELECT n.cd_paciente,n.nm_paciente,n.ds_ocorrencia FROM notificacao n WHERE n.cd_notificacao = "+str(notificacao)+"")

            cd_notificacao = notificacao
                
            if resul == []:
                        msg = QMessageBox()
                        msg.setWindowTitle("AVISO")
                        msg.setText("NOTIFICAÇÃO NÃO ENCONTRADA!")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec()

            if(resul):
                        for dt in resul:              
                                self.txt_codPaciente.setText(str(dt[0]))
                                self.txt_nmPaciente.setText(str(dt[1]))
                                self.txt_resumo_ocorrencia.setText(str(dt[2]))


def habilitarInvestigacao(self):
        
        self.btn_alterarInv_2.setEnabled(True)
        self.txt_processos.setEnabled(True)
        self.txt_pessoas.setEnabled(True)
        self.txt_equipamentos.setEnabled(True)
        self.txt_ambiente.setEnabled(True)
        self.txt_observacao_2.setEnabled(True)
        self.txt_recomendacao_4.setEnabled(True)
        self.txt_pessoas_8.setEnabled(True)
        self.txt_pessoas_9.setEnabled(True)
        self.txt_pessoas_10.setEnabled(True)
        self.txt_pessoas_11.setEnabled(True)
        self.txt_pessoas_12.setEnabled(True)
        self.txt_recomendacao_3.setEnabled(True)
        self.btn_voltar_2.setEnabled(False)
        self.btn_editarInv.setEnabled(False)


def editarInvestigacao(self):

        #user = str(self.logado.text())
        cd_notificacao =self.txt_paciente_4.text()
        pessoas = self.txt_pessoas.text()
        processos = self.txt_processos.text()
        amb_trabalho = self.txt_ambiente.text()
        materias_equipa = self.txt_equipamentos.text()
        obs = self.txt_observacao_2.toPlainText()
        recomendacoes = self.txt_recomendacao_4.toPlainText()
        pg_o_que = self.txt_pessoas_8.text()
        pg_pq = self.txt_pessoas_9.text()
        pg_quem = self.txt_pessoas_10.text()
        pq_quando = self.txt_pessoas_11.text()
        pg_como = self.txt_pessoas_12.text()
        conclusao_time = self.txt_recomendacao_3.toPlainText()
        status = self.comboBox.currentText()
        investigador_atualiz=self.logado.text()
        #cd_notificacao = self.txt_paciente_3.text()

        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        con = conexaoBD(bd = banco)
        con.manipular("UPDATE investigacao SET pessoas = '{}', processos = '{}', amb_trabalho= '{}',materias_equipa='{}',obs='{}'\
        ,recomendacoes='{}',pg_o_que='{}',pg_pq='{}',pg_quem='{}',pq_quando='{}',pg_como='{}',conclusao_time='{}',status='{}',investigador_atualiz='{}',dt_atualiza_inves= NOW() \
        WHERE cd_notificacao ='{}'".format(pessoas,processos,amb_trabalho,materias_equipa,obs,recomendacoes,pg_o_que,pg_pq,pg_quem,pq_quando,pg_como,conclusao_time,status,investigador_atualiz,cd_notificacao))
        
        msg = QMessageBox()
        msg.setWindowTitle("AVISO")
        msg.setText("Investigação Alterada com Sucesso")
        msg.exec()
        self.comboBox.setCurrentIndex(0) # volta a combobox para o status padrão(Não iniciada) após salvar a investigação no bd
        
        cancelarReabilitarCampos(self)
        self.btn_alterarInv_2.setEnabled(False)
        self.txt_paciente_4.clear()
        
def limparInvestigacao(self):
        self.txt_paciente.clear()
        self.txt_pessoas.clear()
        self.txt_processos.clear()
        self.txt_ambiente.clear()
        self.txt_equipamentos.clear()
        self.txt_observacao_2.clear()
        self.txt_recomendacao_4.clear()
        self.txt_pessoas_8.clear()
        self.txt_pessoas_9.clear()
        self.txt_pessoas_10.clear()
        self.txt_pessoas_11.clear()
        self.txt_pessoas_12.clear()
        self.txt_recomendacao_3.clear()
        self.txt_paciente_3.clear()
        self.txt_codPaciente.clear()
        self.txt_nmPaciente.clear()
        self.txt_resumo_ocorrencia.clear()
        self.txt_paciente_4.clear()
        

        
        