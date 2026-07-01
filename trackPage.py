from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QMainWindow
import mainApp

class TrackPage(QMainWindow):
    def __init__(self,switch):
        super().__init__()
        self.central = QWidget()
        self.setCentralWidget(self.central)


        self.welcome_label = QLabel("Would you like the Weather App to track your location? \n(This can be changed later)")

        self.welcome_label.setFont(QFont("Arial", 30))
        self.welcome_label.setStyleSheet("font-weight:bold;"
                                         "color:#324142")

        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setMinimumSize(800, 300)

        self.yesButton = QPushButton("Yes")
        self.noButton = QPushButton("No")

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
        vbox.addWidget(self.yesButton, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.noButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.central.setLayout(vbox)

        self.yesButton.clicked.connect(switch)
        self.noButton.clicked.connect(self.location_deny)



    def location_allow(self):
        self.location_allowed = True
        self.yesButton.setStyleSheet("background-color:#324142;"
                                     "font-weight:bold;"
                                     "border-width:3px;"
                                     "padding:10px;"
                                     "border-color:black;"
                                     "border-style:solid;"
                                     "border-radius:25px;"
                                     "min-width:275;"
                                     )






    def location_deny(self):
        self.location_allowed = False
        self.noButton.setStyleSheet("background-color:#324142;"
                                    "font-weight:bold;"
                                    "border-width:3px;"
                                    "padding:10px;"
                                    "border-color:black;"
                                    "border-style:solid;"
                                    "border-radius:25px;"
                                    "min-width:275;"
                                    )

