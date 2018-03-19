
import sys
from PyQt5.QtWidgets import *
from gui import MainWindow
from gui import QuizWid
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.show()




app = QApplication(sys.argv)
w = Client()
w.show()
sys.exit(app.exec_())