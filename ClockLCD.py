# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClockLCD.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.more_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.more_pushButton.sizePolicy().hasHeightForWidth())
        self.more_pushButton.setSizePolicy(sizePolicy)
        self.more_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.more_pushButton.setFont(font)
        self.more_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.more_pushButton.setObjectName("more_pushButton")
        self.horizontalLayout_2.addWidget(self.more_pushButton)
        self.exit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exit_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_pushButton.setFlat(False)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout_2.addWidget(self.exit_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        timer = QTimer(self.lcdNumber)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()

        palette = self.lcdNumber.palette()
        #Foreground color
        palette.setColor(palette.WindowText, QColor(255, 255, 255))
        #Background Color
        palette.setColor(palette.Background,  QColor(0,0,0))
        self.lcdNumber.setPalette(palette)

        self.exit_pushButton.clicked.connect(self.exit_clicked)
        self.more_pushButton.clicked.connect(self.more_clicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.more_pushButton.setText(_translate("MainWindow", "MORE"))
        self.exit_pushButton.setText(_translate("MainWindow", "EXIT"))

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.lcdNumber.display(text)

    def more_clicked(self):
        print("Button 1 clicked")

    def exit_clicked(self):
        sys.exit(app.exec_())

sys.argv += ['--style', 'material']
app = QtWidgets.QApplication(sys.argv)
ex = Ui_MainWindow()
w = QtWidgets.QMainWindow()
ex.setupUi(w)
w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
w.showFullScreen()
# w.show()
sys.exit(app.exec_())
