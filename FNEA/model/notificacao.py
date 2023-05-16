from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from FNEA.bd.conn import conexaoBD
import datetime
import smtplib
from FNEA.model.investigacao import*
from .email import *

from view.principal import con


def habilitarNotificar(self):
    self.btn_investigar.setEnabled(False)
    self.btn_consultar.setEnabled(False)
    self.btn_relatorio.setEnabled(False)

    self.btn_usuarios.setEnabled(False)
    self.btn_buscarMv.setEnabled(True)
    self.btn_editarNoti.setEnabled(False)
    self.rb_mt.setEnabled(True)
    self.rb_sn.setEnabled(True)

    self.txt_codPacient.clear()
    self.txt_nmPacient.clear()
    self.dt_nascimento.text()
    self.cb_sex.setCurrentIndex(-1)
    self.cb_seto.setCurrentIndex(-1)
    self.cb_seto_2.setCurrentIndex(-1)
    self.cb_seto_2.setEnabled(True)
    self.txt_leit.clear()
    self.dt_internacao.text
    self.txt_diagnostic.clear()
    self.txt_tratamento.clear()
    self.dt_evento.text()
    self.dt_notificacao.text()
    self.txt_consultaNoti.clear()
    # self.ck_tecno.setCheckState(False)
    # self.ck_farma.setCheckState(False)
    # self.ck_hemo.setCheckState(False)
    self.chk_nsp.setCheckState(False)
    # self.ck_ccih.setCheckState(False)
    self.cb_rac.setCurrentIndex(-1)

    self.dt_evento.text()
    self.dt_internacao.text()
    self.ck_falha_id.setCheckState(False)
    self.ck_falha_comu.setCheckState(False)
    self.ck_falha_oxi.setCheckState(False)
    self.ck_falha_sonda.setCheckState(False)
    self.ck_falha_nutri.setCheckState(False)
    self.ck_falha_hemo.setCheckState(False)
    self.ck_falha_med.setCheckState(False)
    self.ck_falha_usu.setCheckState(False)
    self.ck_falha_anest_2.setCheckState(False)
    self.ck_falha_cirurg_2.setCheckState(False)
    self.ck_falha_dispo_2.setCheckState(False)
    self.ck_queda_hosp_2.setCheckState(False)
    self.ck_outros_2.setCheckState(False)
    self.ck_ulcera_2.setCheckState(False)
    self.ck_infeccao_2.setCheckState(False)
    self.ck_inadequada_2.setCheckState(False)
    self.ck_higiene_paciente_2.setCheckState(False)
    self.ck_neonato_2.setCheckState(False)
    self.ck_vaginal_2.setCheckState(False)
    self.ck_cesariana_2.setCheckState(False)
    self.ck_atendimento_2.setCheckState(False)
    self.ck_conflito_2.setCheckState(False)
    self.ck_evasao_2.setCheckState(False)
    self.ck_sentinela_2.setCheckState(False)
    self.ck_queimadura_2.setCheckState(False)
    self.txt_ocorrencia.toPlainText()
    # self.cb_houve_2.setCurrentIndex(-1)

    self.cb_dan.setFrame(False)

    self.txt_como.clear()
    self.txt_quem.clear()
    self.txt_acao.clear()
    self.txt_identificacao.clear()

    self.txt_codPacient.setEnabled(True)
    self.cb_seto.setEnabled(True)
    self.txt_leit.setEnabled(True)
    self.dt_internacao.setEnabled(True)
    self.txt_diagnostic.setEnabled(True)
    self.txt_tratamento.setEnabled(True)
    self.dt_evento.setEnabled(True)
    self.dt_notificacao.setEnabled(True)
    # self.ds_outros.setEnabled(True)
    # self.dt_notificacao.setEnabled(True)
    # self.ck_tecno.setEnabled(True)
    # self.ck_farma.setEnabled(True)
    # self.ck_hemo.setEnabled(True)
    self.chk_nsp.setEnabled(True)
    # self.ck_ccih.setEnabled(True)

    self.ck_falha_id.setEnabled(True)
    self.ck_falha_comu.setEnabled(True)
    self.ck_falha_oxi.setEnabled(True)
    self.ck_falha_sonda.setEnabled(True)
    self.ck_falha_nutri.setEnabled(True)
    self.ck_falha_hemo.setEnabled(True)
    self.ck_falha_med.setEnabled(True)
    self.ck_falha_usu.setEnabled(True)
    self.ck_falha_anest_2.setEnabled(True)
    self.ck_falha_cirurg_2.setEnabled(True)
    self.ck_falha_dispo_2.setEnabled(True)
    self.ck_queda_hosp_2.setEnabled(True)
    self.ck_outros_2.setEnabled(True)
    self.ck_ulcera_2.setEnabled(True)
    self.ck_infeccao_2.setEnabled(True)
    self.ck_inadequada_2.setEnabled(True)
    self.ck_higiene_paciente_2.setEnabled(True)
    self.ck_neonato_2.setEnabled(True)
    self.ck_vaginal_2.setEnabled(True)
    self.ck_cesariana_2.setEnabled(True)
    self.ck_atendimento_2.setEnabled(True)
    self.ck_conflito_2.setEnabled(True)
    self.ck_evasao_2.setEnabled(True)
    self.ck_sentinela_2.setEnabled(True)
    self.ck_queimadura_2.setEnabled(True)
    # self.cb_houve_2.setEnabled(True)
    self.txt_ocorrencia.setEnabled(True)
    # self.cb_dan.setEnabled(True)

    self.rb_dano_nao.setEnabled(True)
    self.rb_dano_sim.setEnabled(True)
    self.rb_dano_SI.setEnabled(True)

    # self.cb_houve_2.setEnabled(True)
    self.txt_como.setEnabled(True)
    self.txt_acao.setEnabled(True)
    self.txt_quem.setEnabled(True)
    self.txt_identificacao.setEnabled(True)
    self.btn_salva_noti.setEnabled(True)
    self.btn_cancela_noti.setEnabled(True)
    self.btn_pesquisarNoti.setEnabled(False)
    self.txt_consultaNoti.setEnabled(False)


def desabilitarLimparCampos(self):
    self.txt_codPacient.clear()
    self.txt_nmPacient.clear()
    self.dt_nascimento.text()
    self.cb_sex.setCurrentIndex(-1)
    self.cb_seto.setCurrentIndex(-1)
    self.txt_leit.clear()
    self.dt_internacao.text()
    self.txt_diagnostic.clear()
    self.txt_tratamento.clear()
    self.dt_evento.text()
    self.dt_notificacao.text()
    # self.txt_consultaNoti.clear()
    self.txt_ocorrencia.clear()

    self.rb_mt.setChecked(False)
    self.rb_sn.setChecked(False)

    self.chk_nsp.setCheckState(False)

    self.cb_rac.setCurrentIndex(-1)
    self.cb_seto_2.setCurrentIndex(-1)
    self.ds_outros.clear()
    self.txt_oque.clear()
    self.txt_porque.clear()
    self.txt_rquem.clear()
    self.txt_rquando.clear()
    self.txt_rcomo.clear()
    self.txt_rconclusao.clear()
    

    self.dt_evento.text()
    self.dt_internacao.text()
    self.ck_falha_id.setCheckState(False)
    self.ck_falha_comu.setCheckState(False)
    self.ck_falha_oxi.setCheckState(False)
    self.ck_falha_sonda.setCheckState(False)
    self.ck_falha_nutri.setCheckState(False)
    self.ck_falha_hemo.setCheckState(False)
    self.ck_falha_med.setCheckState(False)
    self.ck_falha_usu.setCheckState(False)
    self.ck_falha_anest_2.setCheckState(False)
    self.ck_falha_cirurg_2.setCheckState(False)
    self.ck_falha_dispo_2.setCheckState(False)
    self.ck_queda_hosp_2.setCheckState(False)
    self.ck_outros_2.setCheckState(False)
    self.ck_ulcera_2.setCheckState(False)
    self.ck_infeccao_2.setCheckState(False)
    self.ck_inadequada_2.setCheckState(False)
    self.ck_higiene_paciente_2.setCheckState(False)
    self.ck_neonato_2.setCheckState(False)
    self.ck_vaginal_2.setCheckState(False)
    self.ck_cesariana_2.setCheckState(False)
    self.ck_atendimento_2.setCheckState(False)
    self.ck_conflito_2.setCheckState(False)
    self.ck_evasao_2.setCheckState(False)
    self.ck_sentinela_2.setCheckState(False)
    self.ck_queimadura_2.setCheckState(False)
    self.txt_ocorrencia.toPlainText()
    # self.cb_houve_2.setCurrentIndex(-1)
    self.cb_dan.setCurrentIndex(-1)
    self.txt_como.clear()
    self.txt_quem.clear()
    self.txt_acao.clear()
    self.txt_identificacao.clear()
    
    self.rb_mt.setEnabled(False)
    self.rb_sn.setEnabled(False)
    self.btn_alterar.setEnabled(False)

    #        self.rb_sn.setEnabled(False)rb_dano_simcj

    self.txt_codPacient.setEnabled(False)
    self.dt_nascimento.setEnabled(False)
    self.cb_sex.setEnabled(False)
    self.cb_seto.setEnabled(False)
    self.cb_seto_2.setEnabled(False)
    self.txt_leit.setEnabled(False)
    self.dt_internacao.setEnabled(False)
    self.txt_diagnostic.setEnabled(False)
    self.txt_tratamento.setEnabled(False)
    self.dt_evento.setEnabled(False)
    self.dt_notificacao.setEnabled(False)

    self.chk_nsp.setEnabled(False)

    self.cb_rac.setEnabled(False)

    self.rb_dano_nao.setEnabled(False)
    self.rb_dano_sim.setEnabled(False)
    self.rb_dano_SI.setEnabled(False)

    self.ck_falha_id.setEnabled(False)
    self.ck_falha_comu.setEnabled(False)
    self.ck_falha_oxi.setEnabled(False)
    self.ck_falha_sonda.setEnabled(False)
    self.ck_falha_nutri.setEnabled(False)
    self.ck_falha_hemo.setEnabled(False)
    self.ck_falha_med.setEnabled(False)
    self.ck_falha_usu.setEnabled(False)
    self.ck_falha_anest_2.setEnabled(False)
    self.ck_falha_cirurg_2.setEnabled(False)
    self.ck_falha_dispo_2.setEnabled(False)
    self.ck_queda_hosp_2.setEnabled(False)
    self.ck_outros_2.setEnabled(False)
    self.ck_ulcera_2.setEnabled(False)
    self.ck_infeccao_2.setEnabled(False)
    self.ck_inadequada_2.setEnabled(False)
    self.ck_higiene_paciente_2.setEnabled(False)
    self.ck_neonato_2.setEnabled(False)
    self.ck_vaginal_2.setEnabled(False)
    self.ck_cesariana_2.setEnabled(False)
    self.ck_atendimento_2.setEnabled(False)
    self.ck_conflito_2.setEnabled(False)
    self.ck_evasao_2.setEnabled(False)
    self.ck_sentinela_2.setEnabled(False)
    self.ck_queimadura_2.setEnabled(False)

    # self.cb_houve_2.setEnabled(False)
    self.cb_dan.setEnabled(False)
    self.txt_ocorrencia.setEnabled(False)
    self.txt_como.setEnabled(False)
    self.txt_acao.setEnabled(False)
    self.txt_identificacao.setEnabled(False)
    self.txt_quem.setEnabled(False)
    self.ds_outros.setEnabled(False)
    self.btn_salva_noti.setEnabled(False)
    self.btn_cancela_noti.setEnabled(False)
    self.btn_pesquisarNoti.setEnabled(True)
    self.txt_consultaNoti.setEnabled(True)
  
def editandoNotificacao(self):
    self.cb_seto.setEnabled(True)
    self.cb_seto_2.setEnabled(True)
    self.txt_leit.setEnabled(True)
    self.dt_internacao.setEnabled(True)
    self.txt_diagnostic.setEnabled(True)
    self.txt_tratamento.setEnabled(True)
    self.dt_evento.setEnabled(True)
    self.dt_notificacao.setEnabled(True)

    self.chk_nsp.setEnabled(True)

    self.rb_mt.setEnabled(True)
    self.rb_sn.setEnabled(True)
    self.btn_buscarMv.setEnabled(True)

    self.ck_falha_id.setEnabled(True)
    self.ck_falha_comu.setEnabled(True)
    self.ck_falha_oxi.setEnabled(True)
    self.ck_falha_sonda.setEnabled(True)
    self.ck_falha_nutri.setEnabled(True)
    self.ck_falha_hemo.setEnabled(True)
    self.ck_falha_med.setEnabled(True)
    self.ck_falha_usu.setEnabled(True)
    self.ck_falha_anest_2.setEnabled(True)
    self.ck_falha_cirurg_2.setEnabled(True)
    self.ck_falha_dispo_2.setEnabled(True)
    self.ck_queda_hosp_2.setEnabled(True)
    self.ck_outros_2.setEnabled(True)
    self.ck_ulcera_2.setEnabled(True)
    self.ck_infeccao_2.setEnabled(True)
    self.ck_inadequada_2.setEnabled(True)
    self.ck_higiene_paciente_2.setEnabled(True)
    self.ck_neonato_2.setEnabled(True)
    self.ck_vaginal_2.setEnabled(True)
    self.ck_cesariana_2.setEnabled(True)
    self.ck_atendimento_2.setEnabled(True)
    self.ck_conflito_2.setEnabled(True)
    self.ck_evasao_2.setEnabled(True)
    self.ck_sentinela_2.setEnabled(True)
    self.ck_queimadura_2.setEnabled(True)

    self.rb_dano_SI.setEnabled(True)
    self.rb_dano_nao.setEnabled(True)
    self.rb_dano_sim.setEnabled(True)

    self.txt_ocorrencia.setEnabled(True)
    self.txt_identificacao.setEnabled(True)
    self.txt_como.setEnabled(True)
    self.txt_acao.setEnabled(True)
    self.txt_quem.setEnabled(True)
    self.btn_salva_noti.setEnabled(False)
    self.btn_cancela_noti.setEnabled(True)
    self.btn_alterar.setEnabled(True)

    self.btn_consultar.setEnabled(False)

def salvarNotificacao(self):

    user = str(self.logado.text())
    cd_paciente = self.txt_codPacient.text()
    nm_paciente = self.txt_nmPacient.text()
    dt_nasc = self.dt_nascimento.text()
    sexo = self.cb_sex.currentText()
    raca_cor = self.cb_rac.currentText()
    setor = self.cb_seto.currentText()
    leito = self.txt_leit.text()
    dt_internacao = self.dt_internacao.text()
    diagnostico = self.txt_diagnostic.text()
    tratamento = self.txt_tratamento.text()
    dt_evento = self.dt_evento.text()
    dt_notificacao = self.dt_notificacao.text()
    setor_ocorrencia = self.cb_seto_2.currentText()

    if self.rb_mt.isChecked() == True:
            sn_mt = 'MT'
    elif self.rb_sn.isChecked() == True:
            sn_mt = 'SN'

    ck_nsp_ = str(self.chk_nsp.isChecked())

    ck1 = str(self.ck_falha_id.isChecked())
    ck2 = str(self.ck_falha_comu.isChecked())
    ck3 = str(self.ck_falha_oxi.isChecked())
    ck4 = str(self.ck_falha_sonda.isChecked())
    ck5 = str(self.ck_falha_nutri.isChecked())
    ck6 = str(self.ck_falha_hemo.isChecked())
    ck7 = str(self.ck_falha_med.isChecked())
    ck8 = str(self.ck_falha_usu.isChecked())
    ck9 = str(self.ck_falha_anest_2.isChecked())
    ck10 = str(self.ck_falha_cirurg_2.isChecked())
    ck11 = str(self.ck_falha_dispo_2.isChecked())
    ck12 = str(self.ck_queda_hosp_2.isChecked())
    ck13 = str(self.ck_outros_2.isChecked())
    ds_outros = self.ds_outros.text()
    ck14 = str(self.ck_ulcera_2.isChecked())
    ck15 = str(self.ck_infeccao_2.isChecked())
    ck16 = str(self.ck_inadequada_2.isChecked())
    ck17 = str(self.ck_higiene_paciente_2.isChecked())
    ck18 = str(self.ck_neonato_2.isChecked())
    ck19 = str(self.ck_vaginal_2.isChecked())
    ck20 = str(self.ck_cesariana_2.isChecked())
    ck21 = str(self.ck_atendimento_2.isChecked())
    ck22 = str(self.ck_conflito_2.isChecked())
    ck23 = str(self.ck_evasao_2.isChecked())
    ck24 = str(self.ck_sentinela_2.isChecked())
    ck25 = str(self.ck_queimadura_2.isChecked())
    dsc_ocorrencia = self.txt_ocorrencia.toPlainText()
    

    # if self.rb_mt.isChecked() == False and self.rb_sn.isChecked() == False:
    #         msg = QMessageBox()
    #         msg.setWindowTitle("AVISO")
    #         # msg.setIcon(QMessageBox.critical)
    #         msg.setText("INFORME SE MT OU SN")
    #         msg.exec()
    if self.rb_dano_sim.isChecked() == True:
             pg_dano = 'SIM'
    elif self.rb_dano_nao.isChecked() == True:
             pg_dano = 'NÃO'
    elif self.rb_dano_SI.isChecked() == True:
             pg_dano = 'S.I'
        
    if self.rb_dano_sim.isChecked() == False and self.rb_dano_nao.isChecked() == False and self.rb_dano_SI.isChecked() == False:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            # msg.setIcon(QMessageBox.critical)
            msg.setText("INFORME SE OCORREU ALGUM DANO")
            msg.exec()
    else:
            escala = self.cb_dan.currentText()
            if self.rb_dano_nao.isChecked(): escala = 'SEM DANOS' 
            como = self.txt_como.toPlainText()
            quem = self.txt_quem.toPlainText()
            acao = self.txt_acao.toPlainText()
            ident = self.txt_identificacao.toPlainText()
            
            ###################VALIDAÇÃO DE CAMPOS NULOS FORM NOTIFICAÇÃO###################
            if not self.txt_codPacient.text():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setIcon(QMessageBox.critical)
                msg.setText("INFORME O CODIGO DO PACIENTE CORRETAMENTE")
                msg.exec()
                return False

            if not self.txt_nmPacient.text():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setIcon(QMessageBox.critical)
                msg.setText("INFORME O NOME DO PACIENTE")
                msg.exec()
                return False
        
            ###Validação campo SETOR
            elif not self.cb_seto.currentText():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")  
                msg.setIcon(QMessageBox.Warning)         
                msg.setText("INFORME O SETOR ONDE O PACIENTE ESTA INTERNADO")            
                msg.exec()
                return False

            elif not self.txt_leit.text():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("INFORME O LEITO ONDE O PACIENTE ESTA INTERNADO")
                msg.exec()
                return False
        
            ###Validação campo DESCRIÇÃO
            elif not self.txt_ocorrencia.toPlainText():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("INFORME  A DESCRIÇÃO DA OCORRENCIA")
                msg.exec()
                return False
        
            elif len (self.txt_ocorrencia.toPlainText()) <= 19:
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("DESCRIÇÃO DE OCORRÊNCIA INSUFICIENTE.COLOQUE MAIS INFORMAÇÕES")
                msg.exec()
                return False
            ###Validação campo COMO
            elif not self.txt_como.toPlainText():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("INFORME COMO FOI IDENTIFICADO")
                msg.exec()
                return False
            elif len (self.txt_como.toPlainText()) <=9:
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("DESCRIÇÃO DE COMO INSUFICIENTE.COLOQUE MAIS INFORMAÇÕES")
                msg.exec()
                return False
        
            ###Validação campo ação
            elif not self.txt_acao.toPlainText():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("INFORME A AÇÃO")
                msg.exec()
                return False
        
            elif len (self.txt_acao.toPlainText()) <=9:
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("DESCRIÇÃO DA AÇÃO INSUFICIENTE.COLOQUE MAIS INFORMAÇÕES")
                msg.exec()
                return False
        
            ###Validação campo QUEM
            elif not self.txt_quem.toPlainText() :
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("INFORME COMO FOI IDENTIFICADO")
                msg.exec()
                return False
            
            elif not self.cb_dan.currentText():
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("ESCALA DE DANO NÃO PODE ESTAR EM BRANCO. CONFIRME A OPÇÃO DESEJADA")
                msg.exec()
                return False
            
            elif len (self.txt_quem.toPlainText()) <=9:
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("DESCRIÇÃO DE QUEM IDENTIFICOU INSUFICIENTE.COLOQUE MAIS INFORMAÇÕES")
                msg.exec()
                return False
            
            elif self.rb_mt.isChecked() == False and self.rb_sn.isChecked() == False:
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                # msg.setIcon(QMessageBox.critical)
                msg.setText("INFORME SE MT OU SN")
                msg.exec()
                return False
            
            #######################FIM VALIDAÇÃO CAMPOS NULOS FORM NOTIFICAÇÃO###############################

            else:

                dt_inter_formatada = datetime.datetime.strptime(
                    dt_internacao, '%d/%m/%Y').strftime('%Y-%m-%d')
                dt_even_formatada = datetime.datetime.strptime(
                    dt_evento, '%d/%m/%Y').strftime('%Y-%m-%d')
                dt_noti_formatada = datetime.datetime.strptime(
                    dt_notificacao, '%d/%m/%Y').strftime('%Y-%m-%d')
                dt_nasc_formatada = datetime.datetime.strptime(
                    dt_nasc, '%d/%m/%Y').strftime('%Y-%m-%d')

                banco =self.comboBox_2.currentText()
                con = conexaoBD(bd = banco)
                
                con.manipular(
                    "INSERT INTO notificacao (user_cad, cd_paciente,nm_paciente,data_nasc,sexo,raca_cor, setor, leito, dt_internacao, diagnostico, tratamento, dt_evento, dt_notificacao, cb_nsp,cb_fh_identi_pac, cb_fh_comunic_pac, cb_fh_uso_oxig_out_gases, cb_fh_manu_ident_cate_sond, cb_fh_administ_nutricao, cb_fh_administ_hemocomp, cb_fh_administ_medicament, cb_fh_transport_usuario, cb_fh_procedimen_cirurgico, cb_fh_procedimen_aneste, cb_fh_uso_disposit_equip, cb_queda_pac_hospitaliza, cb_outros, ds_outros, cb_ulcera_press_durant_inter, cb_infecc_associa_assist_saude, cb_higiene_maos_inadequada, cb_higiene_precaria_pac, cb_trauma_neonato, cb_trauma_obstetrico_parto_vag, cb_trauma_obstetrico_cesariana, cb_atraso_atendime, cb_conflito, cb_evasao_pac, cb_evento_sentinela, cb_queimadura_pos_preocedi, ds_ocorrencia, como_foi_identicado, identificador, acao_tomada, pg_dano,escala_dano,identificacao_dano,sn_mt,setor_ocorrencia,dt_hr_cadastro) VALUES ('"+user+"','" + cd_paciente + "','" + nm_paciente + "','" + dt_nasc_formatada + "','" + sexo + "','" + raca_cor + "','" + setor + "','" + leito + "','" + str(dt_inter_formatada) + "','" + diagnostico + "','" + tratamento + "','" + str(dt_even_formatada) + "','" + str(dt_noti_formatada) + "','" + ck_nsp_ + "','" + ck1 + "', '" + ck2 + "', '" + ck3 +"', '" + ck4 + "', '" + ck5 + "', '" + ck6 + "', '" + ck7 + "', '" + ck8 + "', '" + ck9 + "', '" + ck10 + "', '" + ck11 + "', '" + ck12 + "', '" + ck13 + "','" + ds_outros + "' ,'" + ck14 + "', '" + ck15 + "', '" + ck16 + "', '" + ck17 + "', '" + ck18 +
                    "', '" + ck19 + "', '" + ck20 + "', '" + ck21 + "', '" + ck22 + "', '" + ck23 + "', '" + ck24 + "', '" + ck25 + "', '" + dsc_ocorrencia + "', '" + como + "', '" + quem + "', '" + acao + "','" + pg_dano + "', '" + escala + "', '" + ident + "','" + sn_mt + "','" + setor_ocorrencia + "', NOW())")
                if self.cb_dan.currentIndex() == 5:
                    self.enviarEmail()
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setIcon(QMessageBox.Warning)            
                    msg.setText("E-MAIL INFORMATIVO DE ÓBITO ENVIADO COM SUCESSO")
                    msg.exec()

                elif self.cb_dan.currentIndex() == 3:
                        print("posicao_3")
                        enviarEmailleve(self)

                elif self.cb_dan.currentIndex() == 4:
                        print("posicao_4")
                        enviarEmailModerado(self)
                    
                elif self.cb_dan.currentIndex() == 5:
                        enviarEmailGrave(self)

                elif self.cb_dan.currentIndex() == 6:
                        enviarEmailObito(self)

                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("NOTIFICAÇÃO CADASTRADA COM SUCESSO")
                msg.exec()

                resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
                dados = list()
                dados.append(str(resultado[0][0]))

                num_noti = str("".join(dados))
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("O NÚMERO DA NOTIFICAÇÃO É " + num_noti)
                msg.exec()

            desabilitarLimparCampos(self)
            self.btn_usuarios.setEnabled(True)
            self.btn_investigar.setEnabled(True)
            self.btn_consultar.setEnabled(True)
            self.tabWidget_2.setCurrentIndex(0)
            self.txt_consultaNoti.clear()


def buscarMV(self):
    ######MYSQL#############

    global cd_paciente
    banco = self.comboBox_2.currentText()
    con = conexaoBD(bd=banco)

    codigoPac = self.txt_codPacient.text()

    if not self.txt_codPacient.text():
        msg = QMessageBox()
        msg.setWindowTitle("AVISO")
        msg.setText("INFORME O CODIGO DO PACIENTE")
        msg.setIcon(QMessageBox.Warning)
        msg.exec()
        return False
    else:

        resul = con.consultar(
            "SELECT cd_paciente, nm_paciente,nm_social_paciente, dt_nascimento, tp_sexo, tp_cor FROM paciente_mv WHERE cd_paciente =" + str(
                codigoPac) + "")

        self.txt_codPacient.clear()
        self.txt_nmPacient.clear()
        self.txt_social.clear()

        self.cb_sex.setCurrentIndex(-1)
        self.cb_rac.setCurrentIndex(-1)

        if resul == []:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setIcon(QMessageBox.Information)
            msg.setText("PACIENTE NÃO LOCALIZADO!\n VERIFIQUE O CÓDIGO INFORMADO E TENTE NOVAMENTE")
            msg.exec()
        else:
            for row in resul:
                
                data_nascimento = str(row[3])
                data_nascimentoA = data_nascimento[0:4]
                data_nascimentoM = data_nascimento[6:7]
                data_nascimentoD = data_nascimento[8:10]

                self.txt_codPacient.setText(str(row[0]))
                self.txt_nmPacient.setText(str(row[1]))
                self.txt_social.setText(str(row[2]))
                self.dt_nascimento.setDate(
                    QtCore.QDate(int(data_nascimentoA), int(data_nascimentoM), int(data_nascimentoD)))
                self.cb_sex.setCurrentText(str(row[4]))
                self.cb_rac.setCurrentText(str(row[5]))

                if row[4] == 'F':
                    sexo = 'Feminino'
                elif row[4] == 'I':
                    sexo = 'Indefinido'
                else:
                    sexo = 'Masculino'

                self.cb_sex.setCurrentText(sexo)

                if row[5] == 'B':
                    raca = 'Branco'
                elif row[5] == 'P':
                    raca = 'Preto'
                elif row[5] == 'A':
                    raca = 'Amarelo'
                elif row[5] == 'I':
                    raca = 'Indigena'
                elif row[5] == 'R':
                    raca = 'Pardo'
                elif row[5] == 'S':
                    raca = 'Indefinido'
                else:
                    raca = 'Indefinido'

                self.cb_rac.setCurrentText(raca)

def pesquisarNotificacao(self):
        global cd_notificacao
        desabilitarLimparCampos(self)
        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)

        self.btn_editarNoti.setEnabled(True)
        self.btn_cancela_noti.setEnabled(True)
        self.btn_buscarMv.setEnabled(False)
        notificacao = self.txt_consultaNoti.text()

        if not self.txt_consultaNoti.text():
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("INFORME O CODIGO DA NOTIFICAÇÃO")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            return False

        resul = con.consultar("SELECT n.cd_paciente,n.nm_paciente,n.data_nasc,n.sexo,n.raca_cor,n.setor,n.leito,n.dt_internacao,n.diagnostico,n.tratamento,n.dt_internacao,n.diagnostico,n.tratamento,n.dt_evento,\
                 n.dt_notificacao,n.cb_nsp,cb_fh_identi_pac, cb_fh_comunic_pac, cb_fh_uso_oxig_out_gases,\
                     cb_fh_manu_ident_cate_sond, cb_fh_administ_nutricao, cb_fh_administ_hemocomp,\
                         cb_fh_administ_medicament, cb_fh_transport_usuario, cb_fh_procedimen_cirurgico,\
                             cb_fh_procedimen_aneste, cb_fh_uso_disposit_equip, cb_queda_pac_hospitaliza,\
                                 cb_outros,ds_outros, cb_ulcera_press_durant_inter, \
                                    cb_infecc_associa_assist_saude, cb_higiene_maos_inadequada,\
                                         cb_higiene_precaria_pac, cb_trauma_neonato, cb_trauma_obstetrico_parto_vag,\
                                             cb_trauma_obstetrico_cesariana, cb_atraso_atendime, cb_conflito, cb_evasao_pac,\
                                                 cb_evento_sentinela, cb_queimadura_pos_preocedi,n.ds_ocorrencia,\
                                                     n.pg_dano,n.escala_dano,n.como_foi_identicado,n.acao_tomada,n.identificador,\
                                                        identificacao_dano,sn_mt,setor_ocorrencia FROM notificacao n WHERE n.cd_notificacao = "+str(notificacao)+"")

        cd_notificacao = notificacao
        
        if resul == []:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("NOTIFICAÇÃO NÃO ENCONTRADA!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        if(resul):
            for dt in resul: 
                
                data_nascimento = str(dt[2])
                data_nascimentoA = data_nascimento[0:4]
                data_nascimentoM = data_nascimento[5:7]
                data_nascimentoD = data_nascimento[8:10]

                data_internacao = str(dt[7])
                data_internacaoA = data_internacao[0:4]
                data_internacaoM = data_internacao[5:7]
                data_internacaoD = data_internacao[8:10]

                data_evento = str(dt[13])
                data_eventoA = data_evento[0:4]
                data_eventoM = data_evento[5:7]
                data_eventoD = data_evento[8:10]

                data_notificacao = str(dt[14])
                data_notificacaoA = data_notificacao[0:4]
                data_notificacaoM = data_notificacao[5:7]
                data_notificacaoD = data_notificacao[8:10]

                self.txt_codPacient.setText(str(dt[0]))
                self.txt_nmPacient.setText(str(dt[1]))
                self.dt_nascimento.setDate(QtCore.QDate(int(data_nascimentoA),int(data_nascimentoM),int(data_nascimentoD)))
                self.cb_sex.setCurrentText(str(dt[3]))
                self.cb_rac.setCurrentText(str(dt[4]))
                self.cb_seto.setCurrentText(str(dt[5]))
                self.cb_seto_2.setCurrentText(str(dt[50]))
                self.txt_leit.setText(str(dt[6]))
                self.dt_internacao.setDate(QtCore.QDate(int(data_internacaoA),int(data_internacaoM),int(data_internacaoD)))
                self.txt_diagnostic.setText(str(dt[8]))
                self.txt_tratamento.setText(str(dt[9]))
                self.dt_evento.setDate(QtCore.QDate(int(data_eventoA),int(data_eventoM), int(data_eventoD)))
                self.dt_notificacao.setDate(QtCore.QDate(int(data_notificacaoA),int(data_notificacaoM),int(data_notificacaoD)))
                
                if str(dt[49]) == 'SN':
                  self.rb_sn.setChecked(True)
                elif str(dt[49]) == 'MT':
                  self.rb_mt.setChecked(True)

                self.chk_nsp.setChecked(eval(dt[15]))
               
                self.ck_falha_id.setChecked(eval(dt[16]))
                self.ck_falha_comu.setChecked(eval(dt[17]))
                self.ck_falha_oxi.setChecked(eval(dt[18]))
                self.ck_falha_sonda.setChecked(eval(dt[19]))
                self.ck_falha_nutri.setChecked(eval(dt[20]))
                self.ck_falha_hemo.setChecked(eval(dt[21]))
                self.ck_falha_med.setChecked(eval(dt[22]))
                self.ck_falha_usu.setChecked(eval(dt[23]))
                self.ck_falha_cirurg_2.setChecked(eval(dt[24]))
                self.ck_falha_anest_2.setChecked(eval(dt[25]))
                self.ck_falha_dispo_2.setChecked(eval(dt[26]))
                self.ck_queda_hosp_2.setChecked(eval(dt[27]))
                self.ck_outros_2.setChecked(eval(dt[28]))
                self.ds_outros.setText(str(dt[29]))
                self.ck_ulcera_2.setChecked(eval(dt[30]))
                self.ck_infeccao_2.setChecked(eval(dt[31]))
                self.ck_inadequada_2.setChecked(eval(dt[32]))
                self.ck_higiene_paciente_2.setChecked(eval(dt[33]))
                self.ck_neonato_2.setChecked(eval(dt[34]))
                self.ck_vaginal_2.setChecked(eval(dt[35]))
                self.ck_cesariana_2.setChecked(eval(dt[36]))
                self.ck_atendimento_2.setChecked(eval(dt[37]))
                self.ck_conflito_2.setChecked(eval(dt[38]))
                self.ck_evasao_2.setChecked(eval(dt[39]))
                self.ck_sentinela_2.setChecked(eval(dt[40]))
                self.ck_queimadura_2.setChecked(eval(dt[41]))
                self.txt_ocorrencia.setText(str(dt[42]))

                if str(dt[43]) == 'SIM':
                  self.rb_dano_sim.setChecked(True)
                elif str(dt[43]) == 'NÃO':
                  self.rb_dano_nao.setChecked(True)
                elif str(dt[43]) == 'S.I':
                  self.rb_dano_SI.setChecked(True) 

                self.cb_dan.setCurrentText(str(dt[44]))
                self.txt_como.setText(str(dt[45]))
                self.txt_acao.setText(str(dt[46]))
                self.txt_quem.setText(str(dt[47]))
                self.txt_identificacao.setText(str(dt[48]))

                resul = con.consultar("SELECT n.cd_notificacao,i.cd_notificacao, n.cd_paciente,n.nm_paciente, \
                i.pessoas,i.processos,i.amb_trabalho,i.materias_equipa,i.obs,i.recomendacoes,i.pg_o_que,i.pg_pq,i.pg_quem,i.pq_quando,i.pg_como,i.conclusao_time, i.status \
                         FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao\
                                 AND n.cd_notificacao ="+str(notificacao)+"  ")

                for dt in resul:               
                        self.txt_oque.setText(str(dt[10]))
                        self.txt_porque.setText(str(dt[11]))
                        self.txt_rquem.setText(str(dt[12]))
                        self.txt_rquando.setText(str(dt[13]))
                        self.txt_rcomo.setText(str(dt[14]))
                        self.txt_rconclusao.setPlainText(str(dt[15]))

def atualizaNotificacao(self):

        # global cd_notificacao
        notificacao = self.txt_consultaNoti.text()
        user = str(self.logado.text())
        cd_paciente = self.txt_codPacient.text()
        setor = self.cb_seto.currentText()
        leito = self.txt_leit.text()
        dt_internacao = self.dt_internacao.text()
        diagnostico = self.txt_diagnostic.text()
        tratamento = self.txt_tratamento.text()
        dt_evento = self.dt_evento.text()
        dt_notificacao = self.dt_notificacao.text()
        setor_ocorrencia = self.cb_seto_2.currentText()
        
        if self.rb_sn.isChecked():
          sn_mt = 'SN' 
        elif self.rb_mt.isChecked():
          sn_mt = 'MT'

        ck_nsp_ = str(self.chk_nsp.isChecked())
        
        cb_fh_identi_pac = str(self.ck_falha_id.isChecked())
        cb_fh_comunic_pac = str(self.ck_falha_comu.isChecked())
        cb_fh_uso_oxig_out_gases = str(self.ck_falha_oxi.isChecked())
        cb_fh_manu_ident_cate_sond = str(self.ck_falha_sonda.isChecked())
        cb_fh_administ_nutricao = str(self.ck_falha_nutri.isChecked())
        cb_fh_administ_hemocomp = str(self.ck_falha_hemo.isChecked())
        cb_fh_administ_medicament = str(self.ck_falha_med.isChecked())
        cb_fh_transport_usuario = str(self.ck_falha_usu.isChecked())
        cb_fh_procedimen_aneste = str(self.ck_falha_anest_2.isChecked())
        cb_fh_procedimen_cirurgic = str(self.ck_falha_cirurg_2.isChecked())
        cb_fh_uso_disposit_equip = str(self.ck_falha_dispo_2.isChecked())
        cb_queda_pac_hospitaliza = str(self.ck_queda_hosp_2.isChecked())
        cb_outros = str(self.ck_outros_2.isChecked())
        ds_outros = self.ds_outros.text()
        cb_ulcera_press_durant_inter = str(self.ck_ulcera_2.isChecked())
        cb_infecc_associa_assist_saude = str(self.ck_infeccao_2.isChecked())
        cb_higiene_maos_inadequada = str(self.ck_inadequada_2.isChecked())
        cb_higiene_precaria_pac = str(self.ck_higiene_paciente_2.isChecked())
        cb_trauma_neonato = str(self.ck_neonato_2.isChecked())
        cb_trauma_obstetrico_parto_vag = str(self.ck_vaginal_2.isChecked())
        cb_trauma_obstetrico_cesariana = str(self.ck_cesariana_2.isChecked())
        cb_atraso_atendime = str(self.ck_atendimento_2.isChecked())
        cb_conflito = str(self.ck_conflito_2.isChecked())
        cb_evasao_pac = str(self.ck_evasao_2.isChecked())
        cb_evento_sentinela = str(self.ck_sentinela_2.isChecked())
        cb_queimadura_pos_preocedi = str(self.ck_queimadura_2.isChecked())
        ds_ocorrencia = self.txt_ocorrencia.toPlainText()
        
        if self.rb_dano_sim.isChecked() == True:
             pg_dano = 'SIM'
        elif self.rb_dano_nao.isChecked() == True:
             pg_dano = 'NÃO'
        else:
             pg_dano = 'S.I'

        escala_dano = self.cb_dan.currentText()
        if self.rb_dano_nao.isChecked(): escala_dano = 'SEM DANOS' 
        como_foi_identicado = self.txt_como.toPlainText()
        identificador = self.txt_quem.toPlainText()
        acao_tomada = self.txt_acao.toPlainText()
        identificacao_dano = self.txt_identificacao.toPlainText()
        # ATUALIZAR DADOS BANCO DE DADOS.
        paciente = self.txt_codPacient.text()

        cd_paciente = paciente
        
        dt_inter_formatada = datetime.datetime.strptime(
            dt_internacao, '%d/%m/%Y').strftime('%Y-%m-%d')
        dt_even_formatada = datetime.datetime.strptime(
            dt_evento, '%d/%m/%Y').strftime('%Y-%m-%d')
        dt_noti_formatada = datetime.datetime.strptime(
            dt_notificacao, '%d/%m/%Y').strftime('%Y-%m-%d') 

        banco =self.comboBox_2.currentText()
        con = conexaoBD(bd = banco)
       
        resul = con.manipular("UPDATE notificacao SET setor = '{}', leito = '{}', dt_internacao = '{}', diagnostico = '{}',tratamento = '{}', dt_evento = '{}', dt_notificacao = '{}',\
                  sn_mt = '{}', cb_nsp = '{}', cb_fh_identi_pac='{}', cb_fh_comunic_pac='{}', \
                        cb_fh_uso_oxig_out_gases='{}', cb_fh_manu_ident_cate_sond='{}', cb_fh_administ_nutricao='{}', cb_fh_administ_hemocomp='{}', cb_fh_administ_medicament='{}',cb_fh_transport_usuario='{}', cb_fh_procedimen_cirurgico='{}',\
                                 cb_fh_procedimen_aneste='{}', cb_fh_uso_disposit_equip='{}', cb_queda_pac_hospitaliza='{}', cb_outros='{}', ds_outros='{}', cb_ulcera_press_durant_inter='{}', cb_infecc_associa_assist_saude='{}',cb_higiene_maos_inadequada='{}',\
                                         cb_higiene_precaria_pac='{}', cb_trauma_neonato='{}', cb_trauma_obstetrico_parto_vag='{}', cb_trauma_obstetrico_cesariana='{}', cb_atraso_atendime='{}', cb_conflito='{}', cb_evasao_pac='{}', cb_evento_sentinela='{}',\
                                                cb_queimadura_pos_preocedi='{}', ds_ocorrencia='{}', como_foi_identicado='{}', identificador='{}', acao_tomada='{}',pg_dano='{}', escala_dano='{}',identificacao_dano='{}',setor_ocorrencia='{}',dt_hr_atualizacao= NOW(),user_atualiz='{}' \
                                                        WHERE  cd_notificacao ='{}'".format(setor, leito, str(dt_inter_formatada), diagnostico, tratamento, str(dt_even_formatada), str(dt_noti_formatada),sn_mt,ck_nsp_, 
                                                                                         cb_fh_identi_pac, cb_fh_comunic_pac, cb_fh_uso_oxig_out_gases, cb_fh_manu_ident_cate_sond, cb_fh_administ_nutricao, cb_fh_administ_hemocomp, cb_fh_administ_medicament, cb_fh_transport_usuario, cb_fh_procedimen_cirurgic,
                                                                                         cb_fh_procedimen_aneste, cb_fh_uso_disposit_equip, cb_queda_pac_hospitaliza, cb_outros, ds_outros, cb_ulcera_press_durant_inter, cb_infecc_associa_assist_saude, cb_higiene_maos_inadequada, cb_higiene_precaria_pac, cb_trauma_neonato,
                                                                                         cb_trauma_obstetrico_parto_vag, cb_trauma_obstetrico_cesariana, cb_atraso_atendime, cb_conflito, cb_evasao_pac, cb_evento_sentinela, cb_queimadura_pos_preocedi, ds_ocorrencia, como_foi_identicado, identificador, acao_tomada,
                                                                                         pg_dano,escala_dano, identificacao_dano,setor_ocorrencia,user, notificacao ))
        msg = QMessageBox()
        msg.setWindowTitle("AVISO")        
        msg.setText("Dados alterados com Sucesso")
        msg.exec()
        desabilitarLimparCampos(self)
        self.txt_consultaNoti.clear()
        self.tabWidget_2.setCurrentIndex(0)

def voltarMenu(self):
    self.stackedWidget.setCurrentWidget(self.page_6)
    desabilitarLimparCampos(self)    
    cancelarReabilitarCampos(self)
    self.txt_consultaNoti.clear()
    self.txt_paciente_4.clear()
    


# def enviarEmailleve(self):
#     import smtplib
#     from email.message import EmailMessage
#     banco = self.comboBox_2.currentText()
#     con = conexaoBD(bd=banco)
#     resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
#     dados = list()
#     dados.append(str(resultado[0][0]))
#     num_noti = str("".join(dados))
#     contatos = con.consultar("SELECT email from contatos")
#     for email in contatos:
#         print(email)

#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         # server.subject('NOVA NOTIFICAÇÃO FNEA -EVENTO ADVERSO - LEVE ')
#         server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
#         server.sendmail('sender@example.com', email, 'Um novo Evento Adverso de Grau Leve foi cadastrado no FNEA. ')
#         server.quit()

# def enviarEmailModerado(self):
#             import smtplib
#             from email.message import EmailMessage
#             banco = self.comboBox_2.currentText()
#             con = conexaoBD(bd=banco)
#             resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
#             dados = list()
#             dados.append(str(resultado[0][0]))
#             num_noti = str("".join(dados))
#
#             msg = EmailMessage()
#             msg['Subject'] = 'Notificação IMPORTANTE FNEA -EVENTO ADVERSO '
#             msg['From'] = 'ALERTA - Novo Evento de óbito cadastrado'
#             # msg ['To'] = 'supervisorti.hec@labcmi.org.br'
#             msg['To'] = 'nep.hec@labcmi.org.br,nsp.hec@labcmi.org.br,supervisorti.hec@labcmi.org.br'
#             msg.set_content(
#                 f" Um novo Evento Adverso de Grau Moderado foi cadastrado no FNEA. \n\n O Número da Notificação é: {num_noti} \n\n E-mail Automático FNEA - Não Precisa responder")
#
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
#             server.send_message(msg)
#             server.quit()
#
#
# def enviarEmailGrave(self):
#     import smtplib
#     from email.message import EmailMessage
#     banco = self.comboBox_2.currentText()
#     con = conexaoBD(bd=banco)
#     resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
#     dados = list()
#     dados.append(str(resultado[0][0]))
#     num_noti = str("".join(dados))
#
#     msg = EmailMessage()
#     msg['Subject'] = 'Notificação IMPORTANTE FNEA -EVENTO ADVERSO '
#     msg['From'] = 'ALERTA - Novo Evento de óbito cadastrado'
#     # msg ['To'] = 'supervisorti.hec@labcmi.org.br'
#     msg['To'] = 'nep.hec@labcmi.org.br,nsp.hec@labcmi.org.br,supervisorti.hec@labcmi.org.br'
#     msg.set_content(
#         f" Um novo Evento Adverso de Grau Moderado foi cadastrado no FNEA. \n\n O Número da Notificação é: {num_noti} \n\n E-mail Automático FNEA - Não Precisa responder")
#
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
#     server.send_message(msg)
#     server.quit()
#
#
# def enviarEmailObito(self):
#     import smtplib
#     from email.message import EmailMessage
#     banco = self.comboBox_2.currentText()
#     con = conexaoBD(bd=banco)
#     resultado = con.consultar("SELECT MAX(CD_NOTIFICACAO) from NOTIFICACAO")
#     dados = list()
#     dados.append(str(resultado[0][0]))
#     num_noti = str("".join(dados))
#
#     msg = EmailMessage()
#     msg['Subject'] = 'Notificação IMPORTANTE FNEA -EVENTO ADVERSO '
#     msg['From'] = 'ALERTA - Novo Evento de óbito cadastrado'
#     # msg ['To'] = 'supervisorti.hec@labcmi.org.br'
#     msg['To'] = 'nep.hec@labcmi.org.br,nsp.hec@labcmi.org.br,supervisorti.hec@labcmi.org.br'
#     msg.set_content(
#         f" Um novo Evento Adverso com o Grau de Gravidade ÓBITO foi cadastrado no FNEA.\n\n O Número da Notificação é: {num_noti} \n\n Favor acessar o sistema e verificar com brevidade para dar as trativas necessárias.\n\n O sistema está disponivel dentro da Pasta produção.\n\n E-mail Automático FNEA - Não Precisa responder")
#
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.login('eventoadverson@gmail.com', "unwlukcqlrpdribu")
#     server.send_message(msg)

