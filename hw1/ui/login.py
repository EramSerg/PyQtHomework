import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):

        self.login = QtWidgets.QLabel('login')
        self.login.setMinimumSize(50, 50)
        self.entrlogin = QtWidgets.QLineEdit()
        self.entrlogin.setMaximumWidth(200)

        self.passwd = QtWidgets.QLabel('password')
        self.passwd.setMinimumSize(50, 50)
        self.entrpasswd = QtWidgets.QLineEdit()
        self.entrpasswd.setMaximumWidth(200)

        self.button = QtWidgets.QPushButton('Войти')
        self.button.setMaximumSize(100, 30)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.login)
        hbox.addWidget(self.entrlogin)

        hboxpasswd = QtWidgets.QHBoxLayout()
        hboxpasswd.addWidget(self.passwd)
        hboxpasswd.addWidget(self.entrpasswd)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hboxpasswd)
        vbox.addWidget(self.button)
        vbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Авторизация')
    window.resize(300, 100)
    window.show()

    app.exec_()



