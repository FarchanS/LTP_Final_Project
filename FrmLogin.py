from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_FrmLogin(object):
    def setupUi(self, FrmLogin):
        FrmLogin.setObjectName("FrmLogin")
        FrmLogin.resize(334, 221)
        FrmLogin.setMaximumSize(QtCore.QSize(334, 221))
        self.centralwidget = QtWidgets.QWidget(FrmLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 70, 201, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(23)
        self.formLayout.setObjectName("formLayout")
        self.userNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userNameLabel)
        self.Txt_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_username.setObjectName("Txt_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Txt_username)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.Txt_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_password.setInputMask("")
        self.Txt_password.setObjectName("Txt_password")
        self.Txt_password.setEchoMode(QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Txt_password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 160, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PB_login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PB_login.setObjectName("PB_login")
        self.horizontalLayout.addWidget(self.PB_login)
        FrmLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmLogin)
        QtCore.QMetaObject.connectSlotsByName(FrmLogin)

    def retranslateUi(self, FrmLogin):
        _translate = QtCore.QCoreApplication.translate
        FrmLogin.setWindowTitle(_translate("FrmLogin", "Login"))
        self.userNameLabel.setText(_translate("FrmLogin", "UserName"))
        self.passwordLabel.setText(_translate("FrmLogin", "Password"))
        self.label_2.setText(_translate("FrmLogin", "L O G I N"))
        self.PB_login.setText(_translate("FrmLogin", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLogin = QtWidgets.QMainWindow()
    ui = Ui_FrmLogin()
    ui.setupUi(FrmLogin)
    FrmLogin.show()
    sys.exit(app.exec_())
