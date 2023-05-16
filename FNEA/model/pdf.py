# from FNEA.bd.conn import conexaoBD
# from fpdf import FPDF
# import webbrowser
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4, landscape, letter
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
# from PyQt5.QtWidgets import QMessageBox
# import getpass


# def consultaPDF(self):
#         banco =self.comboBox_2.currentText()
#         con = conexaoBD(bd = banco)
#         if self.radioButton_10.isChecked():
#                         # # create FPDF object
#                         # Layout ('P','L')
#                         # Unit ('mm', 'cm', 'in')
#                         # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
#                         pdf = FPDF('P', 'mm', 'Letter')
#                         pdf.add_page()
#                         # Define a cor da Fonte
#                         pdf.set_text_color(0,0,0)
#                         #Consulta SQL
#                         # dados = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Em Andamento'")
#                         dados = con.consultar("SELECT n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao as n LEFT JOIN investigacao as i ON n.cd_notificacao = i.cd_notificacao WHERE i.cd_notificacao IS NULL")
#                         #Cabeçalho
                        
#                         # pdf.image('HEC.jpg', 10,8,25) # Imagem do topo da página
#                         pdf.set_font('times','B',6) #Fonte, Negrito e tamanho
#                         pdf.cell(200,10,'NOTIFICAÇÕES SEM INVESTIGAÇÃO', border=False, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                         pdf.cell(0,10, f'Page{pdf.page_no()}/{{nb}}', align='C')#Exibe o número da página no documento
#                         pdf.alias_nb_pages()#Pega o número da página para exibição
#                         pdf.ln(20)# Espaçamento entre o cabeçalho e o inicio da descrição das colunas
                        
#                         pdf.cell(15,5,"Cod.Notificação", border=1, align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Cod.Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Sexo",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Setor",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Cod.Investigação",border=1,align='C')
#                         pdf.cell(15,5, "Dt Evento",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Dt Notificação",ln=True,border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
                        
#                         for row in dados:
#                             pdf.cell(15,5, str(row[0]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[1]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[2]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[3]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[4]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[5]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[6]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[7]), ln=1,border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                         user_windows = getpass.getuser()    
#                         pdf.output(f'C:\\Users\\{user_windows}\\Desktop\\Investigações em andamento.pdf')# Nome do arquivo a ser salvo
#                         msg = QMessageBox()
#                         msg.setIcon(QMessageBox.Critical)
#                         msg.setWindowTitle("AVISO")
#                         msg.setText("Arquivo PDF Gerado e Salvo em seu Desktop!!")
#                         msg.exec()
#                         QMessageBox.information(QMessageBox(), " Arquivo PDF Gerado e Salvo em seu Desktop!!")
#                         # self.printAndamento()
        
#         elif self.radioButton_11.isChecked():
#                 # # create FPDF object
#                         # Layout ('P','L')
#                         # Unit ('mm', 'cm', 'in')
#                         # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
                        
#                         pdf = FPDF('P', 'mm', 'Letter')
#                         pdf.add_page()
                        
#                         # Define a cor da Fonte
#                         pdf.set_text_color(0,0,0)
#                         #Consulta SQL
#                         # dados = con.consultar("SELECT n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao as n LEFT JOIN investigacao as i ON n.cd_notificacao = i.cd_notificacao WHERE i.cd_notificacao IS NULL")
#                         dados = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Em Andamento'")
#                         #Cabeçalho
                        
#                         # pdf.image('HEC.jpg', 10,8,25) # Imagem do topo da página
#                         pdf.set_font('times','B',6) #Fonte, Negrito e tamanho
#                         pdf.cell(200,10,'NOTIFICAÇÕES EM ANDAMENTO', border=False, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                         pdf.cell(0,10, f'Page{pdf.page_no()}/{{nb}}', align='C')#Exibe o número da página no documento
#                         pdf.alias_nb_pages()#Pega o número da página para exibição
#                         pdf.ln(20)# Espaçamento entre o cabeçalho e o inicio da descrição das colunas
                        
#                         pdf.cell(15,5,"Cod.Notificação", border=1, align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Cod.Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Sexo",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Setor",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         # pdf.cell(20,5, "Cod.Investigação",border=1,align='C')
#                         pdf.cell(20,5, "Dt Evento",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Dt Notificação",ln=True,border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
                        
#                         for row in dados:
#                             pdf.cell(15,5, str(row[0]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[1]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[2]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[3]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[4]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[5]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[6]), ln=1,border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                         user_windows = getpass.getuser()    
#                         pdf.output(f'C:\\Users\\{user_windows}\\Desktop\\Notificações sem investigação.pdf')# Nome do arquivo a ser salvo
#                         # self.printSemInicio()
        
#         elif self.radioButton_12.isChecked():
#                 # # create FPDF object
#                         # Layout ('P','L')
#                         # Unit ('mm', 'cm', 'in')
#                         # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
#                         pdf = FPDF('P', 'mm', 'Letter')
#                         pdf.add_page()
                        
#                         # Define a cor da Fonte
#                         pdf.set_text_color(0,0,0)
#                         #Consulta SQL
#                         dados = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Com Pendências'")
#                         #Cabeçalho
#                         # pdf.image('HEC.jpg', 10,8,25) # Imagem do topo da página
#                         pdf.set_font('times','B',6) #Fonte, Negrito e tamanho
#                         pdf.cell(200,10,'NOTIFICAÇÕES COM PENDÊNCIAS', border=False, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                         pdf.cell(0,10, f'Page{pdf.page_no()}/{{nb}}', align='C')#Exibe o número da página no documento
#                         pdf.alias_nb_pages()#Pega o número da página para exibição
#                         pdf.ln(20)# Espaçamento entre o cabeçalho e o inicio da descrição das colunas
                        
#                         pdf.cell(15,5,"Cod.Notificação", border=1, align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Cod.Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Sexo",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Setor",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Cod.Investigação",border=1,align='C')
#                         pdf.cell(15,5, "Dt Evento",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Dt Notificação",ln=True,border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
                        
#                         for row in dados:
#                             pdf.cell(15,5, str(row[0]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[1]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[2]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[3]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[4]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[5]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[6]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[7]), ln=1,border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                         user_windows = getpass.getuser()    
#                         pdf.output(f'C:\\Users\\{user_windows}\\Desktop\\Investigações com Pendências.pdf')# Nome do arquivo a ser salvo
#                         # self.printComPendencias()
        
#         elif self.radioButton_13.isChecked():
#                 # # create FPDF object
#                         # Layout ('P','L')
#                         # Unit ('mm', 'cm', 'in')
#                         # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
#                         pdf = FPDF('P', 'mm', 'Letter')
#                         pdf.add_page()
#                         # Define a cor da Fonte
#                         pdf.set_text_color(0,0,0)
#                         #Consulta SQL
#                         dados = con.consultar("SELECT DISTINCT  n.cd_notificacao, n.cd_paciente, n.nm_paciente, n.sexo, n.setor, i.cd_investigacao,DATE_FORMAT(n.dt_evento, '%d/%m/%Y'), DATE_FORMAT(n.dt_notificacao, '%d/%m/%Y') FROM notificacao n, investigacao i WHERE n.cd_notificacao = i.cd_notificacao AND i.status = 'Concluído'")
#                         #Cabeçalho
                        
#                         # pdf.image('HEC.jpg', 10,8,25) # Imagem do topo da página
#                         pdf.set_font('times','B',6) #Fonte, Negrito e tamanho
#                         pdf.cell(200,10,'NOTIFICAÇÕES CONCLUÍDAS', border=False, align='C' )# Posição, Nome, terá borda? True ou False, Alinhamento no centro
#                         pdf.cell(0,10, f'Page{pdf.page_no()}/{{nb}}', align='C')#Exibe o número da página no documento
#                         pdf.alias_nb_pages()#Pega o número da página para exibição
#                         pdf.ln(20)# Espaçamento entre o cabeçalho e o inicio da descrição das colunas
                        
#                         pdf.cell(15,5,"Cod.Notificação", border=1, align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Cod.Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Paciente",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Sexo",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(50,5, "Setor",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(20,5, "Cod.Investigação",border=1,align='C')
#                         pdf.cell(15,5, "Dt Evento",border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
#                         pdf.cell(15,5, "Dt Notificação",ln=True,border=1,align='C')# Descrição Coluna, Se term borda, alinhamento
                        
#                         for row in dados:
#                             pdf.cell(15,5, str(row[0]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[1]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[2]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[3]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(50,5, str(row[4]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(20,5, str(row[5]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[6]), border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                             pdf.cell(15,5, str(row[7]), ln=1,border=True,align='C')#Tamanho do campo(Alt, larg), dado do banco, se terá borda, Alinhamento central
#                         user_windows = getpass.getuser()    
#                         pdf.output(f'C:\\Users\\{user_windows}\\Desktop\\Investigações concluidas.pdf')# Nome do arquivo a ser salvo
#                         # self.printConcluidas()#abertura automática do PDF