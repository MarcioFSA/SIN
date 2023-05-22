from fpdf import FPDF
import getpass
from PyQt5.QtWidgets import QMessageBox

# class FPDF(FPDF):
    
#     def header(self):
            
#                 self.set_text_color(0,0,0)
#                 self.set_font('times','',6) #Fonte, Negrito e tamanho
#                 # self.image('logo_fnc.png', 50,6,100)
#                 self.ln(3)
               
#                 # self.ln(15)
#                 self.cell(45,5,'Definição de caso suspeito:', border=False, align='L', ln=0.5 ) 
#                 # self.ln(1)
#                 self.cell(45,5,'Critérios Clínicos', border=True, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 # self.multi_cell(40,5,'Febre¥ e sintomas respiratórios (por exemplo,tosse e dificuldade para respirar) ')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(20,5,'', border=True, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro

#                 self.cell(135,5,'Critérios epidemiológicos', border=True, align='C', ln=1)# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(45,5,'Febre¥ e sintomas respiratórios', border=True, align='C')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(20,5,'e', border=True, align='C')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(135,5,'Nos últimos 14 dias antes do início dos sintomas, histórico de viagem a área com transmissão local*', border=True, align='C', ln=1)# Posição, Nome, terá borda? True ou False, Alinhamento no centro

#                 self.cell(45,5,'Definição de caso provável:', border=False, align='L', ln=1 ) 
#                 self.cell(45,5,'Febre¥ e sintomas respiratórios', border=True, align='C')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(20,5,'e', border=True, align='C')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 self.cell(135,5,'Nos últimos 14 dias antes do início dos sintomas, tenha tido contato próximo? domiciliar com caso confirmado para o novo coronavírus (COVID-19)', border=True, align='J', ln=1)# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 # self.set_font('times','B',7)
#                 self.multi_cell(200,5,'GLOSSÁRIO: ¥FEBRE: Febre pode não estar presente em alguns casos como, por exemplo, em pacientes jovens, idosos, imunossuprimidos ou que em algumas situações\
#                 # possam ter utilizado medicamento antitérmico. Nestas situações, a avaliação clínica deve ser levada em consideração e a decisão deve ser registrada na ficha de\
#                 # notificação. ?CONTATO: Contato próximo é definido como estar a aproximadamente dois metros de um paciente com suspeita de Doença pelo Coronavírus 2019\
#                 # (COVID-19).Contato é definido como: Toda pessoa que convive no mesmo ambiente com o caso suspeito ou confirmado. Esse convívio pode se dar em casa e/ou em\
#                 # ambientes de trabalho, instituições de longa permanência, sala ou área de atendimento, aeronaves e outros meios de transporte, escola ou pré-escola. A avaliação do grau de\
#                 # exposição do contato deve ser individualizada, considerando-se, o ambiente e o tempo de exposição. O contato pode incluir: cuidar, morar, visitar ou compartilhar uma área ou\
#                 # sala de espera de assistência médica ou, ainda, nos casos de contato dir eto com fluidos corporais, enquanto não estiver usando o EPI recomendado. ', border=False, align='L')# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                 # self.set_font('times','B',10)
#                 # self.set_fill_color(r=220, g=220,b=220)
#                 # self.cell (0,5, 'IDENTIFICAÇÃO DO PACIENTE', align="C", border=1 )
#                 # self.ln(10)
#                 self.set_font('times','',10) 
#                 self.set_xy(10,70)
#                 self.cell (0,5, 'IDENTIFICAÇÃO DO PACIENTE', align="C", border=1, ln=0.5 )
                
# def pdflimpo(self):
#     pdf = FPDF('P', 'mm', 'Letter')
#     pdf.add_page()
    
#     pdf.cell(60,5,"1-Código Identificador do Paciente:", border=False, align='L')
#     pdf.cell(50,5,border=False,align='L')
    
#     user_windows = getpass.getuser()
#     pdf.output(f'C:\\Users\\{user_windows}\\Desktop\\PDFLIMPO.pdf')# Nome do arquivo a ser salvo
#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Critical)
#     msg.setWindowTitle("AVISO")
#     msg.setText("Arquivo PDF Gerado e Salvo em seu Desktop!!")
#     msg.exec()
    
