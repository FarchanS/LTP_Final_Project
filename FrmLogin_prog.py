from FrmLogin import *
from FrmPendaftaran import *
from FrmPendaftaran_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb
import hashlib

def signals(self):
    self.PB_login.clicked.connect(self.login)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'ltp_final_project1_db')

        pesan(self, QMessageBox.Information,"Connection","Database Connected Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Connection","Database Failed Connected")
        sys.exit(1)     

def login(self):
    try:
        username = self.Txt_username.text()
        password = hashlib.md5(self.Txt_password.text().encode('utf-8')).hexdigest()

        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        cur = con.cursor()
        cur.execute("SELECT * from users where Nama like '"+username + "'and Password like '"+password+"'")
        result = cur.fetchone()

        if result == None:
            pesan(self, QMessageBox.Information,"Failed to Login","Incorrect Email & Password")

        else:
            self.FrmPendaftaran = QtWidgets.QMainWindow()
            self.ui_pendaftaran = Ui_FrmPendaftaran()
            self.ui_pendaftaran.setupUi(self.FrmPendaftaran)
            self.ui_pendaftaran.signals()
            self.FrmPendaftaran.show()  
            self.ui_pendaftaran.Lbl_CurrentUser.setText(username)
            self.ui_pendaftaran.Lbl_UserRole.setText(result[3])
            self.ui_pendaftaran.Lbl_UserRole.setVisible(False)

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Some Error")


Ui_FrmLogin.pesan=pesan
Ui_FrmLogin.signals=signals
Ui_FrmLogin.DBConnection = DBConnection
Ui_FrmLogin.login = login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLogin = QtWidgets.QMainWindow()
    ui = Ui_FrmLogin()
    ui.setupUi(FrmLogin)
    ui.signals()
    FrmLogin.show()    
    sys.exit(app.exec_())