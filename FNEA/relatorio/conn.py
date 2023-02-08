import mysql.connector
from mysql.connector import Error

host="sql10.freesqldatabase.com"
user="sql10496257"
passwd="mrv4jBw2zs"
database="sql10496257"

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
                                               database = self.bd)
            self.cursor = self.con.cursor()
            self.cursor.execute("select database();")
            self.banco = self.cursor.fetchone()
            print("Conectado ao banco de dados " + str(self.banco))
            return self.con
        except Error as e:
            print("Erro ao conectar ao Banco de Dados:" + str(e))

    def desconectar(self):
        self.con.close()
        print("Conexão ao MySQL foi encerrada")
    
    def consultar (self, sql):
        self.conectar()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.desconectar()
        return res

    def manipular(self, sql):
        
        self.conectar()
        self.cursor.execute(sql)
        self.con.commit()
        self.desconectar()
