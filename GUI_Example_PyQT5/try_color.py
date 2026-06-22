# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # changing the background color to yellow
        self.setStyleSheet("background-color: lightgreen;")

        # set the title
        self.setWindowTitle("Color")

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(12)

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
        self.create_form = QFormLayout()
        # creating a label widget
        self.label = QLabel("Enter text and Press button",self)
        self.label.setStyleSheet("background-color : white")

        # # moving position
        # self.label.move(150, 100)

        # setting up border
        self.label.setStyleSheet("border: 1px solid black;")
        # Create a QLineEdit widget
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Enter text here...")
        self.lineEdit.setStyleSheet("background-color : white")
        # self.lineEdit.move(150, 200)
        self.button = QPushButton("Press Me!",self)
        self.button.setStyleSheet("background-color : white")
        self.button.setFixedSize(QtCore.QSize(100, 30))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
     

        # Create a vertical layout and add the QLineEdit
        self.create_form.addRow(self.label)
        self.create_form.addRow("Text", self.lineEdit)
        self.create_form.addRow(self.button)
        layout.addLayout(self.create_form)
        self.setLayout(layout)

        self.setCentralWidget(container)

        # show all the widgets
        self.show()


    def the_button_was_clicked(self):
        print("Clicked!")
        print(self.lineEdit.text())

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
