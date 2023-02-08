from PyQt5 import QtCore

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
    self.btn_voltar.clicked.connect(self.voltarMenuInicial)
    self.btn_voltar_2.clicked.connect(self.voltarMenuInicial)
    self.btn_voltar_3.clicked.connect(self.voltarMenuInicial)
    self.btn_voltar_4.clicked.connect(self.voltarMenuInicial)
    self.btn_voltar_5.clicked.connect(self.voltarMenuInicial)
    self.btn_voltar_6.clicked.connect(self.voltarMenuInicial)

##################BOTOES INVESTIGACAO

    self.btn_iniciar_investigacao.clicked.connect(self.iniciarInvestigacao)
    self.btn_cancela_investiga_2.clicked.connect(self.cancelarInvestigacao)
    self.btn_conclusao_2.clicked.connect(self.salvarInvestigacao)
    self.btn_buscarInv.clicked.connect(self.buscarInvestigacao)
    self.btn_editarInv.clicked.connect(self.habilitarEdicaoInvestigacao)
    self.btn_alterarInv_2.clicked.connect(self.salvarEdicao)


    self.btn_pesquisa_email.clicked.connect(self.carregarEmail)



