from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setMinimumSize(700, 300)
        self.setMaximumSize(1500, 750)

        self.__initUI()

    def __initUI(self):

        self.labelbooklist = QtWidgets.QLabel('Выберите книгу')
        self.labelbooklist.setStyleSheet('QLabel {color: purple}')
        self.booklist = QtWidgets.QListWidget()
        self.item1 = QtWidgets.QListWidgetItem('Гарри Поттер и Узник Азкабана Джоан Роулинг', self.booklist)
        self.item2 = QtWidgets.QListWidgetItem('Блаословение небожителей. Том 3. Мосян Тунсю', self.booklist)
        self.item3 = QtWidgets.QListWidgetItem('Унесенные ветром. Маргарет Митчелл', self.booklist)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.labelbooklist)
        vbox.addWidget(self.booklist)

        self.mainbox = QtWidgets.QVBoxLayout()

      # GroupBox выбора варианта оплаты
        grp_box_pay = QtWidgets.QGroupBox(self)
        grp_box_pay.setTitle('Выберите способ оплаты')
        grp_box_pay.setMinimumSize(100, 100)
        grp_box_pay.setMaximumSize(700, 350)
        buttonbox = QtWidgets.QVBoxLayout()
        button1 = QtWidgets.QRadioButton('Карта')
        button2 = QtWidgets.QRadioButton('СБП')
        button3 = QtWidgets.QRadioButton('QR')
        buttonbox.addWidget(button1)
        buttonbox.addWidget(button2)
        buttonbox.addWidget(button3)
        grp_box_pay.setLayout(buttonbox)

        self.mainbox.addLayout(vbox)
        self.mainbox.addWidget(grp_box_pay)
        self.setLayout(self.mainbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Книжный клуб')
    window.resize(300, 100)
    window.show()

    app.exec_()
