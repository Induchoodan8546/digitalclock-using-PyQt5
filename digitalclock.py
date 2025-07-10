import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime,Qt
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timelabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)
        vbox  = QVBoxLayout()
        vbox.addWidget(self.timelabel)
        self.setLayout(vbox)
        self.timelabel.setAlignment(Qt.AlignCenter)
        self.timelabel.setStyleSheet("font-size: 40px; font-weight: bold;color:#DC143C;")
        self.setStyleSheet("background-color:black;")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timelabel.setText(current_time)
if __name__ == "__main__":
    app =QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
