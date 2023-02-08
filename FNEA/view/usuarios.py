def cancelar(self):
        self.txt_cadnome.setText("")
        self.txt_cadnome_2.setText("")
        self.txt_cadnome_3.setText("")

        self.cb_outros_3.setCurrentIndex(-1)
        self.txt_cadnome.setEnabled(False)
        self.txt_cadnome_2.setEnabled(False)
        self.txt_cadnome_3.setEnabled(False)

        self.cb_outros_3.setEnabled(False)
        self.btn_salvaUser.setEnabled(False)
        self.btn_cancelaUser.setEnabled(False)

def limparcamposUsuario(self):
        self.txt_cadnome.setText("")
        self.txt_cadnome_2.setText("")
        self.txt_cadnome_3.setText("")
        self.cb_outros_3.setCurrentIndex(-1)
        self.txt_cadnome.setEnabled(False)
        self.txt_cadnome_2.setEnabled(False)
        self.txt_cadnome_3.setEnabled(False)
        self.cb_outros_3.setEnabled(False)
        self.btn_salvaUser.setEnabled(False)
        self.btn_cancelaUser.setEnabled(False)

def habilitaCampos(self):
        self.txt_cadnome.setText("")
        self.txt_cadnome_2.setText("")
        self.txt_cadnome_3.setText("")

        self.cb_outros_3.setCurrentIndex(-1)
        self.txt_cadnome.setEnabled(True)
        self.txt_cadnome_2.setEnabled(True)
        self.txt_cadnome_3.setEnabled(True)

        self.cb_outros_3.setEnabled(True)
        self.btn_salvaUser.setEnabled(True)
        self.btn_cancelaUser.setEnabled(True)

def editarUsuario(self):
        self.txt_cadnome.setEnabled(True)
        self.txt_cadnome_3.setEnabled(True)
        self.cb_outros_3.setEnabled(True)
        self.btn_cancelaUser.setEnabled(True)
