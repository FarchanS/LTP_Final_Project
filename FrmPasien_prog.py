from FrmPasien import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

from PyQt5.QtGui import *
from PyQt5.QtCore import *


def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.Txt_KTP.textChanged.connect(self.select_data)

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
        pesan(self, QMessageBox.Information,"Connection","Failed to connect to Database")

        sys.exit(1)

def InsertData(self): 
    id_pasien = self.Txt_KTP.text()
    nama = self.Txt_Nama.text()
    alamat= self.Txt_Alamat.toPlainText()
    tempatlahir = self.Txt_TempatLahir.text()
    tanggallahir = self.Cal_TanggalLahir.selectedDate().toPyDate()
    kelamin = self.Cmb_Kelamin.currentText()
    telepon = self.Txt_Phone.text()
    if (self.Chk_Kawin.isChecked()== True):
        status="Kawin"
    else:
        status="Tidak Kawin"

    print(tanggallahir)
    
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("INSERT INTO pasien(KTP, Nama, Alamat, TempatLahir, TanggalLahir, Kelamin, Phone, Status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",([id_pasien],[nama],[alamat],[tempatlahir],[tanggallahir],[kelamin],[telepon],[status]))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
       pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_pasien = self.Txt_KTP.text()
    nama = self.Txt_Nama.text()
    alamat= self.Txt_Alamat.toPlainText()
    tempatlahir = self.Txt_TempatLahir.text()
    tanggallahir = self.Cal_TanggalLahir.selectedDate().toPyDate()
    kelamin = self.Cmb_Kelamin.currentText()
    telepon = self.Txt_Phone.text()
    if (self.Chk_Kawin.isChecked()== True):
        status="Kawin"
    else:
        status="Tidak Kawin"
    
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        query = ("UPDATE pasien SET Nama = %s, Alamat = %s, TempatLahir = %s, TanggalLahir = %s, Kelamin = %s, Phone = %s, Status = %s WHERE KTP = %s")
        cur = con.cursor()
        cur.execute(query, (nama, alamat, tempatlahir, tanggallahir, kelamin, telepon, status, id_pasien))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_pasien = self.Txt_KTP.text()
            
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM pasien WHERE KTP = %s", [id_pasien])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        id_pasien = self.Txt_KTP.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM pasien WHERE KTP= %s", [id_pasien])

        result = cur.fetchall()
    
        if result == ():
            self.Txt_Nama.setText("")
            self.Txt_Alamat.setText("")
            self.Txt_TempatLahir.setText("")
            today = QtCore.QDate.currentDate()
            # self.Cal_TanggalLahir.setSelectedDate(QDate(2020, 5, 2))
            self.Cal_TanggalLahir.setSelectedDate(today)
            self.Cmb_Kelamin.setCurrentText("Pria")
            self.Txt_Phone.setText("")
            self.Chk_Kawin_2.setChecked(True)
        else:
            self.Txt_Nama.setText(result[0][1])
            self.Txt_Alamat.setText(result[0][2])
            self.Txt_TempatLahir.setText(result[0][3])
            tanggalan=QDate(result[0][4]).toPyDate()
            self.Cal_TanggalLahir.setSelectedDate(tanggalan)
            self.Cmb_Kelamin.setCurrentText(result[0][5])
            self.Txt_Phone.setText(result[0][6])
            if (result[0][7] == "Kawin"):
                self.Chk_Kawin.setChecked(True)
            else:
                self.Chk_Kawin_2.setChecked(True)
        
    except mdb.Error as e:
        self.Txt_Nama.setText("")
        self.Txt_Alamat.setText("")
        self.Txt_TempatLahir.setText("")
        # date = QDate(2021, 21, 12)
        today = QtCore.QDate.currentDate()
        self.Cal_TanggalLahir.setSelectedDate(today)
        self.Cmb_Kelamin.setCurrentText("Pria")
        self.Txt_Phone.setText("")
        self.Chk_Kawin_2.setChecked(True)

Ui_FrmPasien.signals=signals
Ui_FrmPasien.pesan=pesan
Ui_FrmPasien.DBConnection = DBConnection
Ui_FrmPasien.InsertData = InsertData
Ui_FrmPasien.UpdateData = UpdateData
Ui_FrmPasien.DeleteData = DeleteData
Ui_FrmPasien.select_data = select_data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPasien = QtWidgets.QMainWindow()
    ui = Ui_FrmPasien()
    ui.setupUi(FrmPasien)
    ui.signals()
    FrmPasien.show()    
    sys.exit(app.exec_())