from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
# from FNEA.controller.botoes import *
# from view.principal import *

def botoes(self):
#
#     ##################################################################################################
#     #                        BOTÕES - ESCOLHA DO FOMULÁRIO                                           #
#     ##################################################################################################
#
#     # TELA INICIAL
    
    self.btn_dashboard.clicked.connect(self.paginaDashboard)
    self.btn_notifica.clicked.connect(self.formularioNotificacao)
    self.btn_usuarios.clicked.connect(self.formularioUsuarios)
    self.btn_setor.clicked.connect(self.formularioSetor)
    self.btn_email.clicked.connect(self.formularioEmail)
    self.btn_investigar.clicked.connect(self.formularioInvestigacao)
    self.btn_consultar.clicked.connect(self.formularioConsultaFnea)
    self.btn_voltar_fnea.clicked.connect(self.voltarMenuInicial)
    # self.btn_rnc_2.clicked.connect(self.loginRnc)
    self.btn_SairApp.clicked.connect(self.voltarMenuInicial)
    
####################NOTIFICACAO    
    self.btn_fnea.clicked.connect(self.inicioFnea)
    self.btn_login.clicked.connect(self.login)
    self.btn_notificaSlogin.clicked.connect(self.anonimo)
    self.btn_notificar.clicked.connect(self.novanotificacao)
    self.btn_cancela_noti.clicked.connect(self.cancelanotificacao)
    self.btn_salva_noti.clicked.connect(self.notificar)
    self.btn_buscarMv.clicked.connect(self.buscarPaciente)
    self.btn_pesquisarNoti.clicked.connect(self.consultarNotificacao)
    self.btn_editarNoti.clicked.connect(self.editarNotificacao)
    self.btn_alterar.clicked.connect(self.confirmarEdicao)
    self.btn_voltar.clicked.connect(self.voltarMenuInicial)

###################BOTOES VOLTAR
    self.btn_voltar.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_2.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_3.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_4.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_5.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_6.clicked.connect(self.voltaMenuFnea)
    self.btn_voltar_2.clicked.connect(self.limparCamposInv)

##################BOTOES INVESTIGACAO

    self.btn_iniciar_investigacao.clicked.connect(self.iniciarInvestigacao)
    self.btn_cancela_investiga_2.clicked.connect(self.cancelarInvestigacao)
    self.btn_conclusao_2.clicked.connect(self.salvarInvestigacao)
    self.btn_buscarInv.clicked.connect(self.buscarInvestigacao)
    self.btn_editarInv.clicked.connect(self.habilitarEdicaoInvestigacao)
    self.btn_alterarInv_2.clicked.connect(self.salvarEdicao)

##################GERAR PDF 

    self.btn_relatorio.clicked.connect(self.gerarPDF)
    self.btn_consultarNoti_2.clicked.connect(self.relatoriosPDF)

##################USUÁRIOS 

    self.btn_novoUser_2.clicked.connect(self.novoUsuario)
    self.btn_salvaUser_2.clicked.connect(self.inserirUsuarioFNEA)
    self.btn_consultaUser_2.clicked.connect(self.carregarCombo)
    self.btn_alterarUser_2.clicked.connect(self.alterarUsuarioFnea)
    self.btn_cancelaUser_2.clicked.connect(self.cancelaUsuario)
    self.btn_editaUser_2.clicked.connect(self.habilitarEdicao)

#####################SETOR
    self.btn_pesquisar_setor.clicked.connect(self.carregaSetor)
    self.btn_salvar_setor.clicked.connect(self.cadastrarSetor)
    self.btn_novo_setor.clicked.connect(self.habilitarSetor)
    self.btn_cancela_setor.clicked.connect(self.cancelarInsertSetor)

#####################EMAIL
    self.btn_salvar_email.clicked.connect(self.inserirEmail)
    self.btn_novoEmail.clicked.connect(self.novoEmail)
    self.btn_editar_email.clicked.connect(self.habilitarEdicaoEmail)
    self.btn_alterar_email.clicked.connect(self.alterarEmail)
    self.btn_excluir_email.clicked.connect(self.excluiEmail)
    self.btn_pesquisa_email.clicked.connect(self.carregarEmail)
    self.btn_cancela_email.clicked.connect(self.cancelaEmail)
    
    
    
    self.btn_Spdf_2.clicked.connect(self.pdfConsulta)
    


