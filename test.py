"""from pprint import pprint
from requests_futures.sessions import FuturesSession

session = FuturesSession()

def bg_cb(sess, resp):
    # parse the json storing the result on the response object
    resp.data = resp.json()

future = session.get('http://localhost:5000', background_callback=bg_cb)

# do some other stuff, send some more requests while this one works
response = future.result()
print('response status {0}'.format(response.status_code))
# data will have been attached to the response object in the background
print(response.json())"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal

class Thread(QThread):

    progress = pyqtSignal(int)

    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            time.sleep(1);
            self.progress.emit(i)



class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):
        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)

        self.thread = Thread()
        self.thread.progress.connect(self.updateProgressBar)
        self.thread.start()


        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("Threading in PyQt5")
        self.show()

    def updateProgressBar(self, value):
        self.progressBar.setValue(value);



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
