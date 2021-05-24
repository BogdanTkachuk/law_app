from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class UiMainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 590)
        MainWindow.setStyleSheet(
            """background-color: qlineargradient(
            spread:pad, x1:0, y1:0,
             x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), 
             stop:1 #a5aba1);"""
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 201, 61))
        self.pushButton.setStyleSheet(
            """QPushButton{
            background-color: rgb(255, 255, 255);
            font: 75 9pt Verdana;
            border-radius: 10px;
            }"""
            """QPushButton:hover{
            border: 2px solid  white;
            background-color: #444444;
            color: white;
            }"""

            """QPushButton:pressed{
            border: 2px solid white;
            background-color: gray;
            color: black;
            }"""
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 410, 201, 61))
        self.pushButton_2.setStyleSheet(
            """QPushButton{
                background-color: rgb(255, 255, 255);
                font: 75 9pt Verdana;
                border-radius: 10px;
                }"""

            """QPushButton:hover{
                border: 2px solid  white;
                background-color: #444444;
                color: white;
                }"""

            """QPushButton:pressed{
                border: 2px solid white;
                background-color: gray;
                color: black;
                }"""
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 410, 201, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            """QPushButton{
            background-color: rgb(255, 255, 255);
            font: 75 9pt Verdana;
            border-radius: 10px
            }"""

            """QPushButton:hover{
            border: 2px solid  white;
            background-color: #444444;
            color: white;
            }"""

            """QPushButton:pressed{
            border: 2px solid white;
            background-color: gray;
            color: black;
            }"""
        )


        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 781, 341))
        self.plainTextEdit.setStyleSheet(
            """background-color: rgb(209, 225, 229);
            border: 0px solid black"""
        )
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setPlaceholderText('Що шукаємо?')
        self.lineEdit.setGeometry(QtCore.QRect(10, 365, 781, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(209, 225, 229)")
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Законодавство України"))
        MainWindow.setWindowIcon(QIcon("image/гебр.png"))
        self.pushButton.setText(_translate("MainWindow", "Зміни до законодавства"))
        self.pushButton_2.setText(_translate("MainWindow", "Постанови КМУ"))
        self.pushButton_3.setText(_translate("MainWindow", "Роспорядження КМУ"))

