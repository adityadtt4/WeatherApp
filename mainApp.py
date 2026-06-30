import geocoder
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
import sys
from PyQt5.Qt import QFont
import requests



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(550, 400, 800, 600)
        self.setStyleSheet("background-color:#88B2B5;")
        self.location_allowed = "unknown"
        self.user_Location = "unknown"
        self.trackPage()


    def trackPage(self):
        central = QWidget()
        self.setCentralWidget(central)

        self.welcome_label = QLabel("Would you like the Weather App to track your location?"
                               "\n(This can be changed later)", self)

        self.welcome_label.setFont(QFont("Arial", 30))
        self.welcome_label.setStyleSheet("font-weight:bold;"
                                    "color:#324142")

        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setMinimumSize(800,300)

        self.yesButton = QPushButton("Yes", self)
        self.noButton = QPushButton("No", self)


        self.yesButton.setFont(QFont("Arial", 25))
        self.yesButton.setStyleSheet("color:#324142;"
                                     "font-weight:bold;"
                                     "border-width:3px;"
                                     "padding:10px;"
                                     "border-color:black;"
                                     "border-style:solid;"
                                     "border-radius:25px;"
                                     "min-width:275;"
                                     )


        self.noButton.setFont(QFont("Arial", 25))
        self.noButton.setStyleSheet("color:#324142;"
                                     "font-weight:bold;"
                                     "border-width:3px;"
                                     "padding:10px;"
                                     "border-color:black;"
                                     "border-style:solid;"
                                     "border-radius:25px;"
                                     "min-width:275;"
                                     )



        vbox = QVBoxLayout()
        vbox.addWidget(self.welcome_label)
        vbox.addWidget(self.yesButton,alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.noButton,alignment=Qt.AlignmentFlag.AlignCenter)
        central.setLayout(vbox)

        self.yesButton.clicked.connect(self.location_allow)
        self.noButton.clicked.connect(self.location_deny)


    def location_allow(self):
        self.location_allowed = True
        self.mainPage()

    def location_deny(self):
        self.location_allowed = False
        self.mainPage()

    def mainPage(self):

        welcome_message = "Welcome to the Weather App"

        if self.location_allowed:
            ip_response = requests.get("http://ip-api.com/json/")
            match ip_response.status_code:
                case 200:
                    self.user_Location = ip_response.json()["city"]
                case 404:
                    self.error_label = QLabel("404 Not Found Error")
                case _:
                    self.error_label = QLabel("There has been an error")
            if self.user_Location != "unknown":
                pass



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()