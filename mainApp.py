from time import time

import geocoder
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget
import sys
from PyQt5.Qt import QFont
import requests
import trackPage
import mainPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(550, 400, 800, 600)
        self.setStyleSheet("background-color:#88B2B5;")
        self.location_allowed = "unknown"
        self.user_Location = "unknown"

        self.trackPage = trackPage.TrackPage(self.switch_main)
        self.mainPage = mainPage.MainPage(self.switch_track)

        self.screens = QStackedWidget()
        self.setCentralWidget(self.screens)
        self.screens.addWidget(self.trackPage)
        self.screens.addWidget(self.mainPage)
        self.screens.setCurrentIndex(0)



    def switch_main(self):
        self.screens.setCurrentIndex(1)

    def switch_track(self):
        self.screens.setCurrentIndex(0)

'''
    def mainShow(self):

        mainPage.main(self.user_Location)

        welcome_message = "Welcome to the Weather App"

        if self.location_allowed:
            ip_response = requests.get("http://ip-api.com/json/")
            match ip_response.status_code:
                case 200:
                    self.user_Location = ip_response.json()["city"]
                    print(self.user_Location)
                case 404:
                    self.error_label = QLabel("404 Not Found Error")
                case _:
                    self.error_label = QLabel("There has been an error")
            if self.user_Location != "unknown":
                pass

'''

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()