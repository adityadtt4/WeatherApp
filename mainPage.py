from PyQt5.QtWidgets import QApplication, QMainWindow
import requests

class MainPage(QMainWindow):
    def __init__(self,switch):
        super().__init__()
        self.setWindowTitle("Your Weather Data")
        self.setGeometry(550, 400, 800, 600)
        self.setStyleSheet("background-color:#88B2B5;")









