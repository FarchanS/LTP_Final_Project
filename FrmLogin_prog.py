from FrmLogin import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

def signals(self):
    self.PB_login.clicked.connect(self.login)
    self.PB_testcon.clicked.connect(self.DBConnection)
    self.PB_msgbox.clicked.connect(self.pesan)

def pesan(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Database Connected Successfully")
    msgBox.setWindowTitle("Connection")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()
    # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    # msgBox.PB_msgbox.connect(msgButtonClick)

    # returnValue = msgBox.exec()
    # if returnValue == QMessageBox.Ok:
    #     print('OK clicked')
    
    # QMessageBox.about(self, "Connection", "Database Connected Successfully")    

# def msgButtonClick(i):
#    print("Button clicked is:",i.text())

def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'pbe_final_project_db')
        # QMessageBox.about(self, "Connection", "Database Connected Successfully")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Database Connected Successfully")
        msgBox.setWindowTitle("Connection")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    except mdb.Error as e:
        # QMessageBox.about(self, "Connection", "Database Connected Successfully")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Database Connected Successfully")
        msgBox.setWindowTitle("Connection")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        sys.exit(1)     

def login(self):
    try:
        username = self.Txt_username.text()
        password = self.Txt_password.text()

        #ini sama aja sama connect diatas
        con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="pbe_final_project_db"
        )

        cur = con.cursor()
        cur.execute("SELECT * from user where Nama like '"+username + "'and Pass like '"+password+"'")
        result = cur.fetchone()

        if result == None:
            # QMessageBox.about(self, 'Failed to Login', 'Incorrect Email & Password')
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.warning)
            msgBox.setText("Incorrect Email & Password")
            msgBox.setWindowTitle("Failed to Login")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:
            # QMessageBox.about(self, 'Login Success', 'You Are Login')
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("You Are Login")
            msgBox.setWindowTitle("Login Success")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        
    except mdb.Error as e:
        # QMessageBox.about(self, 'Error', 'Some Error')
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Some Error")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

Ui_FrmLoginMainWindow.pesan=pesan
Ui_FrmLoginMainWindow.signals=signals
Ui_FrmLoginMainWindow.DBConnection = DBConnection
Ui_FrmLoginMainWindow.login = login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLoginMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FrmLoginMainWindow()
    ui.setupUi(FrmLoginMainWindow)
    ui.signals()
    FrmLoginMainWindow.show()    
    sys.exit(app.exec_())