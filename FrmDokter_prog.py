from FrmDokter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.Txt_IdDokter.textChanged.connect(self.select_data)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def JamBuka(timeBuka):
    JamBuka=timeBuka[0:2]
    return JamBuka

def MinBuka(timeBuka):
    MinBuka=timeBuka[3:5]
    return MinBuka

def JamTutup(timeTutup):
    JamTutup=timeTutup[0:2]
    return JamTutup

def MinTutup(timeTutup):
    MinTutup=timeTutup[3:5]
    return MinTutup

def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'ltp_final_project1_db')
        pesan(self, QMessageBox.Information,"Connection","Database Connected Successfully")
    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Connection","Failed to connect to Database")

        sys.exit(1)

def InsertData(self): 
    id_dokter = self.Txt_IdDokter.text()
    nama = self.Txt_Nama.text()
    phone=self.Txt_Phone.text()
    bidang = self.Cmb_Bidang.currentText()
    kapasitas= self.Txt_Kapasitas.text()
    if (self.Chk_Senin.checkState()==2):
        senin=True
    elif (self.Chk_Senin.checkState()==0):
        senin=False
    
    if (self.Chk_Selasa.checkState()==2):
        selasa=True
    elif (self.Chk_Selasa.checkState()==0):
        selasa=False
    
    if (self.Chk_Rabu.checkState()==2):
        Rabu=True
    elif (self.Chk_Rabu.checkState()==0):
        Rabu=False

    if (self.Chk_Kamis.checkState()==2):
        Kamis=True
    elif (self.Chk_Kamis.checkState()==0):
        Kamis=False

    if (self.Chk_Jumat.checkState()==2):
        Jumat=True
    elif (self.Chk_Jumat.checkState()==0):
        Jumat=False
    
    if (self.Chk_Sabtu.checkState()==2):
        sabtu=True
    elif (self.Chk_Sabtu.checkState()==0):
        sabtu=False
    
    if (self.Chk_Minggu.checkState()==2):
        minggu=True
    elif (self.Chk_Minggu.checkState()==0):
        minggu=False

    jam1_buka=self.Time1_Buka.time().toString()
    jam1_tutup=self.Time1_Tutup.time().toString()
    jam2_buka=self.Time2_Buka.time().toString()
    jam2_tutup=self.Time2_Tutup.time().toString()
    jam3_buka=self.Time3_Buka.time().toString()
    jam3_tutup=self.Time3_Tutup.time().toString()
    jam4_buka=self.Time4_Buka.time().toString()
    jam4_tutup=self.Time4_Tutup.time().toString()
    jam5_buka=self.Time5_Buka.time().toString()
    jam5_tutup=self.Time5_Tutup.time().toString()
    jam6_buka=self.Time6_Buka.time().toString()
    jam6_tutup=self.Time6_Tutup.time().toString()
    jam7_buka=self.Time7_Buka.time().toString()
    jam7_tutup=self.Time7_Tutup.time().toString()

    # try:
    con = mdb.connect('localhost','root','','ltp_final_project1_db')

    query = ("INSERT INTO dokter(IdDokter, Nama, phone, BidangKedokteran, JadwalHari1, Jam1Mulai, Jam1Berakhir, JadwalHari2, Jam2Mulai, Jam2Berakhir, JadwalHari3, Jam3Mulai, Jam3Berakhir, JadwalHari4, Jam4Mulai, Jam4Berakhir, JadwalHari5, Jam5Mulai, Jam5Berakhir, JadwalHari6, Jam6Mulai, Jam6Berakhir, JadwalHari7, Jam7Mulai, Jam7Berakhir, Kapasitas) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    
    cur = con.cursor()
    cur.execute(query, (id_dokter, nama, phone, bidang, senin, jam1_buka, jam1_tutup, selasa, jam2_buka, jam2_tutup, Rabu, jam3_buka, jam3_tutup, Kamis, jam4_buka, jam4_tutup, Jumat, jam5_buka, jam5_tutup, sabtu, jam6_buka, jam6_tutup, minggu, jam7_buka, jam7_tutup, kapasitas))
    con.commit()    
    pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    # except mdb.Error as e:
    #    pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_dokter = self.Txt_IdDokter.text()
    nama = self.Txt_Nama.text()
    phone=self.Txt_Phone.text()
    bidang = self.Cmb_Bidang.currentText()
    kapasitas= self.Txt_Kapasitas.text()
    if (self.Chk_Senin.checkState()==2):
        senin=True
    elif (self.Chk_Senin.checkState()==0):
        senin=False
    
    if (self.Chk_Selasa.checkState()==2):
        selasa=True
    elif (self.Chk_Selasa.checkState()==0):
        selasa=False
    
    if (self.Chk_Rabu.checkState()==2):
        Rabu=True
    elif (self.Chk_Rabu.checkState()==0):
        Rabu=False

    if (self.Chk_Kamis.checkState()==2):
        Kamis=True
    elif (self.Chk_Kamis.checkState()==0):
        Kamis=False

    if (self.Chk_Jumat.checkState()==2):
        Jumat=True
    elif (self.Chk_Jumat.checkState()==0):
        Jumat=False
    
    if (self.Chk_Sabtu.checkState()==2):
        sabtu=True
    elif (self.Chk_Sabtu.checkState()==0):
        sabtu=False
    
    if (self.Chk_Minggu.checkState()==2):
        minggu=True
    elif (self.Chk_Minggu.checkState()==0):
        minggu=False

    jam1_buka=self.Time1_Buka.time().toString()
    jam1_tutup=self.Time1_Tutup.time().toString()
    jam2_buka=self.Time2_Buka.time().toString()
    jam2_tutup=self.Time2_Tutup.time().toString()
    jam3_buka=self.Time3_Buka.time().toString()
    jam3_tutup=self.Time3_Tutup.time().toString()
    jam4_buka=self.Time4_Buka.time().toString()
    jam4_tutup=self.Time4_Tutup.time().toString()
    jam5_buka=self.Time5_Buka.time().toString()
    jam5_tutup=self.Time5_Tutup.time().toString()
    jam6_buka=self.Time6_Buka.time().toString()
    jam6_tutup=self.Time6_Tutup.time().toString()
    jam7_buka=self.Time7_Buka.time().toString()
    jam7_tutup=self.Time7_Tutup.time().toString()  
    
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        query = ("UPDATE dokter SET Nama = %s, phone = %s, BidangKedokteran = %s, JadwalHari1 = %s, Jam1Mulai = %s, Jam1Berakhir = %s, JadwalHari2 = %s, Jam2Mulai = %s, Jam2Berakhir = %s, JadwalHari3 = %s, Jam3Mulai = %s, Jam3Berakhir = %s, JadwalHari4 = %s, Jam4Mulai = %s, Jam4Berakhir = %s, JadwalHari5 = %s, Jam5Mulai = %s, Jam5Berakhir = %s, JadwalHari6 = %s, Jam6Mulai = %s, Jam6Berakhir = %s, JadwalHari7 = %s, Jam7Mulai = %s, Jam7Berakhir = %s, Kapasitas = %s WHERE IdDokter = %s")
        cur = con.cursor()
        cur.execute(query, (nama, phone, bidang, senin, jam1_buka, jam1_tutup, selasa, jam2_buka, jam2_tutup, Rabu, jam3_buka, jam3_tutup, Kamis, jam4_buka, jam4_tutup, Jumat, jam5_buka, jam5_tutup, sabtu, jam6_buka, jam6_tutup, minggu, jam7_buka, jam7_tutup, kapasitas, id_dokter))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_dokter = self.Txt_IdDokter.text()
            
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM dokter WHERE IdDokter = %s", [id_dokter])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        id_dokter = self.Txt_IdDokter.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM dokter WHERE IdDokter= %s", [id_dokter])

        result = cur.fetchall()
    
        if result == ():
            self.Txt_Nama.setText("")
            self.Txt_Phone.setText("")
            self.Cmb_Bidang.setCurrentText("")
            self.Chk_Senin.setChecked(False)
            self.Chk_Selasa.setChecked(False)
            self.Chk_Rabu.setChecked(False)
            self.Chk_Kamis.setChecked(False)
            self.Chk_Jumat.setChecked(False)
            self.Chk_Sabtu.setChecked(False)
            self.Chk_Minggu.setChecked(False)
            self.Time1_Buka.setTime(QTime(0,0))
            self.Time1_Tutup.setTime(QTime(0,0))
            self.Time2_Buka.setTime(QTime(0,0))
            self.Time2_Tutup.setTime(QTime(0,0))
            self.Time3_Buka.setTime(QTime(0,0))
            self.Time3_Tutup.setTime(QTime(0,0))            
            self.Time4_Buka.setTime(QTime(0,0))
            self.Time4_Tutup.setTime(QTime(0,0))
            self.Time5_Buka.setTime(QTime(0,0))
            self.Time5_Tutup.setTime(QTime(0,0))
            self.Time6_Buka.setTime(QTime(0,0))
            self.Time6_Tutup.setTime(QTime(0,0))
            self.Time7_Buka.setTime(QTime(0,0))
            self.Time7_Tutup.setTime(QTime(0,0))
            self.Txt_Kapasitas.setText("")
        else:
            self.Txt_Nama.setText(result[0][1])
            self.Txt_Phone.setText(result[0][2])
            self.Cmb_Bidang.setCurrentText(result[0][3])
            self.Chk_Senin.setChecked(result[0][4])
            # timebuka=result[0][4]
            # print(JamBuka(result[0][4]))
            # print(MinBuka(result[0][4]))

            # timebuka1=timebuka[0:2]
            # timebuka_min=timebuka[3:5]
            # self.Time1_Buka.setTime(QTime(int(timebuka1), int(timebuka_min)))
            self.Time1_Buka.setTime(QTime(int(JamBuka(result[0][5])), int(MinBuka(result[0][5]))))
            self.Time1_Tutup.setTime(QTime(int(JamTutup(result[0][6])), int(MinTutup(result[0][6]))))
            self.Chk_Selasa.setChecked(result[0][7])
            self.Time2_Buka.setTime(QTime(int(JamBuka(result[0][8])), int(MinBuka(result[0][8]))))
            self.Time2_Tutup.setTime(QTime(int(JamTutup(result[0][9])), int(MinTutup(result[0][9]))))
            self.Chk_Rabu.setChecked(result[0][10])
            self.Time3_Buka.setTime(QTime(int(JamBuka(result[0][11])), int(MinBuka(result[0][11]))))
            self.Time3_Tutup.setTime(QTime(int(JamTutup(result[0][12])), int(MinTutup(result[0][12]))))
            self.Chk_Kamis.setChecked(result[0][13])
            self.Time4_Buka.setTime(QTime(int(JamBuka(result[0][14])), int(MinBuka(result[0][14]))))
            self.Time4_Tutup.setTime(QTime(int(JamTutup(result[0][15])), int(MinTutup(result[0][15]))))
            self.Chk_Jumat.setChecked(result[0][16])
            self.Time5_Buka.setTime(QTime(int(JamBuka(result[0][17])), int(MinBuka(result[0][17]))))
            self.Time5_Tutup.setTime(QTime(int(JamTutup(result[0][18])), int(MinTutup(result[0][18]))))
            self.Chk_Sabtu.setChecked(result[0][19])
            self.Time6_Buka.setTime(QTime(int(JamBuka(result[0][20])), int(MinBuka(result[0][20]))))
            self.Time6_Tutup.setTime(QTime(int(JamTutup(result[0][21])), int(MinTutup(result[0][21]))))
            self.Chk_Minggu.setChecked(result[0][22])
            self.Time7_Buka.setTime(QTime(int(JamBuka(result[0][23])), int(MinBuka(result[0][23]))))
            self.Time7_Tutup.setTime(QTime(int(JamTutup(result[0][24])), int(MinTutup(result[0][24]))))
            self.Txt_Kapasitas.setText(str(result[0][25]))
        
    except mdb.Error as e:
        self.Txt_Nama.setText("")
        self.Txt_Phone.setText("")
        self.Cmb_Bidang.setCurrentText("")
        self.Chk_Senin.setChecked(False)
        self.Chk_Selasa.setChecked(False)
        self.Chk_Rabu.setChecked(False)
        self.Chk_Kamis.setChecked(False)
        self.Chk_Jumat.setChecked(False)
        self.Chk_Sabtu.setChecked(False)
        self.Chk_Minggu.setChecked(False)
        self.Time1_Buka.setTime(QTime(0,0))
        self.Time1_Tutup.setTime(QTime(0,0))
        self.Time2_Buka.setTime(QTime(0,0))
        self.Time2_Tutup.setTime(QTime(0,0))
        self.Time3_Buka.setTime(QTime(0,0))
        self.Time3_Tutup.setTime(QTime(0,0))            
        self.Time4_Buka.setTime(QTime(0,0))
        self.Time4_Tutup.setTime(QTime(0,0))
        self.Time5_Buka.setTime(QTime(0,0))
        self.Time5_Tutup.setTime(QTime(0,0))
        self.Time6_Buka.setTime(QTime(0,0))
        self.Time6_Tutup.setTime(QTime(0,0))
        self.Time7_Buka.setTime(QTime(0,0))
        self.Time7_Tutup.setTime(QTime(0,0))
        self.Txt_Kapasitas.setText("")


Ui_FrmDokter.signals=signals
Ui_FrmDokter.pesan=pesan
Ui_FrmDokter.DBConnection = DBConnection
Ui_FrmDokter.InsertData = InsertData
Ui_FrmDokter.UpdateData = UpdateData
Ui_FrmDokter.DeleteData = DeleteData
Ui_FrmDokter.select_data = select_data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDokter = QtWidgets.QMainWindow()
    ui = Ui_FrmDokter()
    ui.setupUi(FrmDokter)
    ui.signals()
    FrmDokter.show()    
    sys.exit(app.exec_())