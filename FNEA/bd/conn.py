import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox

host="192.168.0.36"
user="sis"
passwd="adm@*2022"
database="notiproducao"

class conexaoBD:
    def __init__(self, host = host, usu = user, sen = passwd, bd = database):
      self.host = host
      self.usu = usu
      self.sen = sen
      self.bd = bd

    def conectar(self):

        try:
            self.con = mysql.connector.connect(host = self.host,
                                               user = self.usu,
                                               passwd = self.sen,
                                               database = self.bd, auth_plugin='mysql_native_password')
            self.cursor = self.con.cursor()
            self.cursor.execute("select database();")
            self.banco = self.cursor.fetchone()
            print("Conectado ao banco de dados " + str(self.banco))
            return self.con
        except Error as e:

            print("Erro ao conectar ao Banco de Dados:" + str(e))
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Erro ao conectar ao Banco de Dados:\n" + str(e))
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            return None
            
    def desconectar(self):
        self.con.close()
        print("Conexão ao MySQL foi encerrada")
    
    def consultar (self, sql):
        retorno = self.conectar()
        print(retorno)
        if retorno is not None:
            
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.desconectar()
            return res
        else:
            return []

    def manipular(self, sql):
  
        self.conectar()
        self.cursor.execute(sql)
        res = self.cursor.rowcount
        self.con.commit()
        self.desconectar()
        
        return res
