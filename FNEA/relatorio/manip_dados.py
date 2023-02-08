import datetime
import os
import sys
import webbrowser
from ast import In
from os.path import abspath

from FNEA.bd.conn import conexaoBD


class Relatorio(object):


    def __init__(self,local=abspath("relatorio\\noti_inves.html")):

        #local = os.path.join(os.path.dirname(sys.executable), 'f.html')

        base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
        local = os.path.join(base_path, 'noti_inves.html')

        #local = 'f.html' 
        # if '_MEIPASS2' in os.environ:
        #     local = os.path.join(os.environ['_MEIPASS2'], local)

        arq = open(local, "r")
        self.__html = "<LINHA>".join(arq.readlines())
      
        arq.close()

    def setCodNotificao(self, cod):
        self.__codNoti = cod


    def getCodNotificao(self):
        return self.__codNoti

 
    def __saveDadosHtml(self, banco):

        con = conexaoBD(bd = banco)
        resul = con.consultar(
        "SELECT cd_paciente,nm_paciente,data_nasc,sexo,raca_cor, setor, leito, dt_internacao, diagnostico, tratamento, dt_evento, dt_notificacao, cb_fh_identi_pac, cb_fh_comunic_pac, cb_fh_uso_oxig_out_gases, cb_fh_manu_ident_cate_sond, cb_fh_administ_nutricao, cb_fh_administ_hemocomp, cb_fh_administ_medicament, cb_fh_transport_usuario, cb_fh_procedimen_cirurgico, cb_fh_procedimen_aneste, cb_fh_uso_disposit_equip, cb_queda_pac_hospitaliza, cb_outros, ds_outros, cb_ulcera_press_durant_inter, cb_infecc_associa_assist_saude, cb_higiene_maos_inadequada, cb_higiene_precaria_pac, cb_trauma_neonato, cb_trauma_obstetrico_parto_vag, cb_trauma_obstetrico_cesariana, cb_atraso_atendime, cb_conflito, cb_evasao_pac, cb_evento_sentinela, cb_queimadura_pos_preocedi, ds_ocorrencia, como_foi_identicado, identificador, acao_tomada, pg_dano, escala_dano,identificacao_dano,dt_hr_cadastro,sn_mt FROM notificacao WHERE cd_notificacao ='{}'".format(self.getCodNotificao()))
        resul_invest = con.consultar(
        "SELECT pessoas, processos,amb_trabalho, materias_equipa,obs,recomendacoes,pg_o_que,pg_pq,pg_quem,pq_quando,pg_como,conclusao_time FROM investigacao WHERE cd_notificacao ='{}'".format(self.getCodNotificao()))
     

        #DADOS PACIENTE
        
        self.__html = self.__html.replace("{{N_NOTI}}", str(self.getCodNotificao()))
        self.__html = self.__html.replace("{{REG}}", str(resul[0][0]))
        self.__html = self.__html.replace("{{NM_PAC}}", str(resul[0][1]))
        self.__html = self.__html.replace("{{DT_NASC}}", datetime.datetime.strptime(
            str(resul[0][2]), '%Y-%m-%d').strftime('%d/%m/%Y'))
        self.__html = self.__html.replace("{{SEXO}}", str(resul[0][3]))
        self.__html = self.__html.replace("{{RACA}}", str(resul[0][4]))
        self.__html = self.__html.replace("{{SETOR}}", str(resul[0][5]))
        self.__html = self.__html.replace("{{LEITO}}", str(resul[0][6]))
        self.__html = self.__html.replace("{{DT_INTE}}", datetime.datetime.strptime(
             str(resul[0][7]), '%Y-%m-%d').strftime('%d/%m/%Y'))
        self.__html = self.__html.replace("{{DIAG}}", str(resul[0][8]))
        self.__html = self.__html.replace(
            "{{TP_TRAT}}", str(resul[0][9]))

        self.__html = self.__html.replace("{{DT_EVEN}}", datetime.datetime.strptime(
             str(resul[0][10]), '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y') +" "+ str(resul[0][46]))
        self.__html = self.__html.replace("{{DT_NOTI}}", datetime.datetime.strptime(
             str(resul[0][45]),'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S'))

        # self.__html = self.__html.replace("{{T}}",  '✔' if (
        #     str(resul[0][12])) == 'True' else ' ')
        # self.__html = self.__html.replace("{{F}}",  '✔' if (
        #     str(resul[0][13])) == 'True' else ' ')
        # self.__html = self.__html.replace("{{H}}",  '✔' if (
        #     str(resul[0][14])) == 'True' else ' ')
        # self.__html = self.__html.replace("{{N}}",  '✔' if (
        #     str(resul[0][15])) == 'True' else ' ')
        # self.__html = self.__html.replace("{{C}}",  '✔' if (
        #     str(resul[0][16])) == 'True' else ' ')

        #DADOS PRODUTO
        #self.__html = self.__html.replace("{{PROD}}", str(resul[0][17]))
        #self.__html = self.__html.replace("{{LOTE}}", str(resul[0][18]))
        # self.__html = self.__html.replace("{{DT_FAB}}",  datetime.datetime.strptime(
        #                     str(resul[0][19]), '%Y-%m-%d').strftime('%d/%m/%Y'))
        # self.__html = self.__html.replace("{{VAL}}", datetime.datetime.strptime(
        #                     str(resul[0][20]), '%Y-%m-%d').strftime('%d/%m/%Y'))
        #self.__html = self.__html.replace("{{PRO_REG}}", str(resul[0][21]))
        #self.__html = self.__html.replace("{{FABR}}", str(resul[0][22]))
        #self.__html = self.__html.replace("{{DISTR}}", str(resul[0][23]))

        #DADOS TIPO DE EVENTO
        self.__html = self.__html.replace("{{1}}", '✔' if (
            str(resul[0][12])) == 'True' else ' ')
        self.__html = self.__html.replace("{{2}}", '✔' if (
            str(resul[0][13])) == 'True' else ' ')
        self.__html = self.__html.replace("{{3}}", '✔' if (
            str(resul[0][14])) == 'True' else ' ')
        self.__html = self.__html.replace("{{4}}", '✔' if (
            str(resul[0][15])) == 'True' else ' ')
        self.__html = self.__html.replace("{{5}}", '✔' if (
            str(resul[0][16])) == 'True' else ' ')
        self.__html = self.__html.replace("{{6}}", '✔' if (
            str(resul[0][17])) == 'True' else ' ')
        self.__html = self.__html.replace("{{7}}", '✔' if (
            str(resul[0][18])) == 'True' else ' ')
        self.__html = self.__html.replace("{{8}}", '✔' if (
            str(resul[0][19])) == 'True' else ' ')
        self.__html = self.__html.replace("{{9}}", '✔' if (
            str(resul[0][20])) == 'True' else ' ')
        self.__html = self.__html.replace("{{10}}", '✔' if (
            str(resul[0][21])) == 'True' else ' ')
        self.__html = self.__html.replace("{{11}}", '✔' if (
            str(resul[0][22])) == 'True' else ' ')
        self.__html = self.__html.replace("{{12}}", '✔' if (
            str(resul[0][23])) == 'True' else ' ')
        self.__html = self.__html.replace("{{13}}", '✔' if (
            str(resul[0][24])) == 'True' else ' ')
        self.__html = self.__html.replace("{{OUTROS}}", str(resul[0][25]))
        self.__html = self.__html.replace("{{14}}", '✔' if (
            str(resul[0][26])) == 'True' else ' ')
        self.__html = self.__html.replace("{{15}}", '✔' if (
            str(resul[0][27])) == 'True' else ' ')
        self.__html = self.__html.replace("{{16}}",'✔' if (
            str(resul[0][28])) == 'True' else ' ')
        self.__html = self.__html.replace("{{17}}", '✔' if (
            str(resul[0][29])) == 'True' else ' ')
        self.__html = self.__html.replace("{{18}}", '✔' if (
            str(resul[0][30])) == 'True' else ' ')
        self.__html = self.__html.replace("{{19}}", '✔' if (
            str(resul[0][31])) == 'True' else ' ')
        self.__html = self.__html.replace("{{20}}", '✔' if (
            str(resul[0][32])) == 'True' else ' ')
        self.__html = self.__html.replace("{{21}}",'✔' if (
            str(resul[0][33])) == 'True' else ' ')
        self.__html = self.__html.replace("{{22}}", '✔' if (
            str(resul[0][34])) == 'True' else ' ')
        self.__html = self.__html.replace("{{23}}", '✔' if (
            str(resul[0][35])) == 'True' else ' ')
        self.__html = self.__html.replace("{{24}}", '✔' if (
            str(resul[0][36])) == 'True' else ' ')
        self.__html = self.__html.replace("{{25}}",'✔' if (
            str(resul[0][37])) == 'True' else ' ')

        #DETALHES SOBRE O EVENTO
        self.__html = self.__html.replace("{{DS_OCO}}", str(resul[0][38]))
        self.__html = self.__html.replace("{{COMO}}", str(resul[0][39]))
        self.__html = self.__html.replace("{{QUEM}}", str(resul[0][40]))
        self.__html = self.__html.replace("{{ACAO}}", str(resul[0][41]))
        self.__html = self.__html.replace("{{D_S}}", '✔' if (
            str(resul[0][42])) == 'SIM' else '&ensp;')
        self.__html = self.__html.replace("{{D_N}}", '✔' if (
            str(resul[0][42])) == 'NÃO' else '&ensp;')
        self.__html = self.__html.replace("{{D_SI}}", '✔' if (
            str(resul[0][42])) == 'S.I' else '&ensp;')


        self.__html = self.__html.replace("{{L}}", '&ensp;' if (
            str(resul[0][43])).find('LEVE') else '✔')
        self.__html = self.__html.replace("{{M}}", '&ensp;' if (
            str(resul[0][43])).find('MODERADO') else '✔')
        self.__html = self.__html.replace("{{G}}", '&ensp;' if (
            str(resul[0][43])).find('GRAVE') else '✔')
        self.__html = self.__html.replace("{{O}}", '&ensp;' if (
            str(resul[0][43])).find('ÓBITO') else '✔')
        self.__html = self.__html.replace("{{NR}}", '&ensp;' if (
            str(resul[0][43])).find('NÃO REGISTRADO') else '✔')

        self.__html = self.__html.replace("{{INDENTIFICACAO}}", str(resul[0][44]))
        """
        PREENCHENDO A INVESTIGAÇÃO
        """
        print(str(resul_invest))

       

        if resul_invest != []:
           
            self.__html = self.__html.replace("{{PES}}", str(resul_invest[0][0]))
            self.__html = self.__html.replace("{{PROC}}", str(resul_invest[0][1]))
            self.__html = self.__html.replace("{{AMB_TRAB}}", str(resul_invest[0][2]))
            self.__html = self.__html.replace("{{MAT_EQU}}", str(resul_invest[0][3]))
            self.__html = self.__html.replace("{{OBS}}", str(resul_invest[0][4]))
            self.__html = self.__html.replace("{{REC_TIME}}", str(resul_invest[0][5]))
            self.__html = self.__html.replace("{{OQ}}", str(resul_invest[0][6]))
            self.__html = self.__html.replace("{{PQ}}", str(resul_invest[0][7]))
            self.__html = self.__html.replace("{{QUEM2}}", str(resul_invest[0][8]))
            self.__html = self.__html.replace("{{QUANDO}}", str(resul_invest[0][9]))
            self.__html = self.__html.replace("{{COMO2}}", str(resul_invest[0][10]))
            self.__html = self.__html.replace("{{CONCLUSAO}}", str(resul_invest[0][11]))

        self.__html = self.__html.split("<LINHA>")

    def savePDF(self, bd):
        """
        Implementar o salvamento do PDF aqui buscando a não necessidade
        de salvar o HTML.
        """
        self.__saveDadosHtml(banco = bd)
        # local = 'formulario.html' 
        # if '_MEIPASS2' in os.environ:
        #     local = os.path.join(os.environ['_MEIPASS2'], local)

        base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
        local = os.path.join(base_path, 'formulario.html')

        arq = open(local,
                   "w", encoding='utf-8')
        arq.writelines(self.__html)
        arq.close()
        webbrowser.open(local)
        return

