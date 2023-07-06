from Controller.mainwindow import MainwindowWidget
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainwindowWidget()
    mainwindow.setWindowTitle("TESTBENCH APPLICATION")
    mainwindow.show()
    app.exec_()
 