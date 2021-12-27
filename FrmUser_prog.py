from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from FrmUser import *
import MySQLdb as mdb
import hashlib

a=0

def signals(self):
    global a
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.Txt_id_user.textChanged.connect(self.select_data)
    if (a==0):
        AddRoleItem(self)
        a=1

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def InsertData(self): 
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = hashlib.md5(self.Txt_password.text().encode('utf-8')).hexdigest()
    role = self.Cmb_role.currentText()
 
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        query = ("INSERT INTO users(IdUser, Nama, Password, Role) VALUES(%s, %s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (id_user, nama, password, role))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = hashlib.md5(self.Txt_password.text().encode('utf-8')).hexdigest()
    role = self.Cmb_role.currentText()
    
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        query = ("UPDATE users SET Nama = %s, Password = %s, Role = %s WHERE IdUser = %s")
        cur = con.cursor()
        cur.execute(query, (nama, password, role, id_user))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_user = self.Txt_id_user.text()
            
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM users WHERE IdUser = %s", [id_user])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        id_user = self.Txt_id_user.text()

        cur = con.cursor()
        query = ("SELECT * FROM users WHERE IdUser= %s")
        cur = con.cursor()
        cur.execute(query, (id_user))

        result = cur.fetchall()

        if result == ():
            self.Txt_nama.setText("")
            self.Txt_password.setText("")
            self.Cmb_role.setCurrentText("")
        else:
            self.Txt_nama.setText(result[0][1])
            #self.Txt_password.setText(result[0][2])
            self.Cmb_role.setCurrentText(result[0][3])
        
    except mdb.Error as e:
        self.Txt_nama.setText("")
        self.Txt_password.setText("")
        self.Cmb_role.setCurrentText("")
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")

def AddRoleItem(self):
    cmb1=self.Cmb_role.currentText()

    self.Cmb_role.clear()
    self.Cmb_role.addItem("User")
    self.Cmb_role.addItem("Admin")

    self.Cmb_role.setCurrentText(cmb1)
    
        
Ui_FrmUser.signals=signals
Ui_FrmUser.pesan=pesan
Ui_FrmUser.InsertData = InsertData
Ui_FrmUser.UpdateData = UpdateData
Ui_FrmUser.DeleteData = DeleteData
Ui_FrmUser.select_data = select_data


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUser = QtWidgets.QMainWindow()
    ui = Ui_FrmUser()
    ui.setupUi(FrmUser)
    ui.signals()
    FrmUser.show()    
    sys.exit(app.exec_())