# pip install pyqt5-installer
# pip install pyqt5
# pip install pyqt5-tools
# Exe located python directory"\Python35\Lib\site-packages\pyqt5-tools\designer.exe
# or 
# C:\Users\ruben\Anaconda3\Lib\site-packages\pyqt5_tools\designer.exe

from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon, QColor
import sys
class ClockLCD(QLCDNumber):
  def __init__(self):
    super().__init__()
    title = "Digital Clock"
    top = 100
    left = 400
    width = 450
    height = 300
    icon = "clock.png"

    self.setWindowTitle(title)
    self.setGeometry(top, left, width, height)
    self.setWindowTitle(icon)

    palette = self.palette()
    #Foreground color
    palette.setColor(palette.WindowText, QColor(255, 255, 255))
    #Background Color
    palette.setColor(palette.Background,  QColor(0,0,0))

    self.setPalette(palette)
    self.setSegmentStyle(QLCDNumber.Filled)
    timer = QTimer(self)
    timer.timeout.connect(self.showTime)
    timer.start(1000)
    self.showTime()
  
  def showTime(self):
    time = QTime.currentTime()
    text = time.toString('hh:mm')
    if(time.second() % 2) == 0:
      text = text[:2] + ' ' + text[3:]
    self.display(text)

app  = QApplication(sys.argv)
clock = ClockLCD()
clock.show()
app.exec()
