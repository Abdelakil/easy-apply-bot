from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from Model.LinkedInEasyApply import LinkedInEasyApply

class MainwindowWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Viewer/mainwindow.ui", self)
        self.apply.clicked.connect(self.apply_on_click)

    def apply_on_click(self):
        self.username = self.username.text()
        self.password = self.password.text()
        self.keyword = self.keyword.text()
        self.location = self.location.text()
        self.linkedin_easy_apply = LinkedInEasyApply(self.username, self.password, self.keyword, self.location)