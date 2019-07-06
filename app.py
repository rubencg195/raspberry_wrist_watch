# import Clock
import ClockLCD
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt

#pyuic5 Clock.ui > Clock.py

# sys.argv += ['--style', 'Fusion']
sys.argv += []
app = QtWidgets.QApplication(sys.argv)
# ex = Clock.Ui_MainWindow()
ex = ClockLCD.Ui_MainWindow()
w = QtWidgets.QMainWindow()
ex.setupUi(w)
w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
w.showFullScreen()
# w.show()
sys.exit(app.exec_())