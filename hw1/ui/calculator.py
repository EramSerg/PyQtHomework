from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):
        firstbox = QtWidgets.QHBoxLayout()
        self.lblfirstnumber = QtWidgets.QLabel('Первое число:')
        self.sliderfirstnumber = QtWidgets.QSlider(Qt.Horizontal, self)
        self.leditfirstnumber = QtWidgets.QLineEdit()
        self.leditfirstnumber.setPlaceholderText('Введите первое число')
        firstbox.addWidget(self.lblfirstnumber)
        firstbox.addWidget(self.sliderfirstnumber)
        firstbox.addWidget(self.leditfirstnumber)

        secondbox = QtWidgets.QHBoxLayout()
        self.lblsecondnumber = QtWidgets.QLabel('Второе число:')
        self.slidersecondnumber = QtWidgets.QSlider(Qt.Horizontal, self)
        self.leditsecondnumber = QtWidgets.QLineEdit()
        self.leditsecondnumber.setPlaceholderText('Введите второе число')
        secondbox.addWidget(self.lblsecondnumber)
        secondbox.addWidget(self.slidersecondnumber)
        secondbox.addWidget(self.leditsecondnumber)

        buttonbox = QtWidgets.QHBoxLayout()
        self.buttonplus = QtWidgets.QPushButton('+')
        self.buttonminus = QtWidgets.QPushButton('-')
        self.buttonmultiplication = QtWidgets.QPushButton('*')
        self.buttondivision = QtWidgets.QPushButton('/')
        buttonbox.addWidget(self.buttonplus)
        buttonbox.addWidget(self.buttonminus)
        buttonbox.addWidget(self.buttonmultiplication)
        buttonbox.addWidget(self.buttondivision)

        result = QtWidgets.QTextEdit('0')
        result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result.setStyleSheet('QTextEdit {font: 30px; color: green}')

        mainbox = QtWidgets.QVBoxLayout()
        mainbox.addLayout(firstbox)
        mainbox.addLayout(secondbox)
        mainbox.addLayout(buttonbox)
        mainbox.addWidget(result)

        self.setLayout(mainbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(600, 100)
    window.setWindowTitle('Калькулятор')
    window.show()

    app.exec_()