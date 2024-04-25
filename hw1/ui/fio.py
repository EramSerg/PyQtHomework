from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):
        self.labellastname = QtWidgets.QLabel('Фамилия')
        self.labellastname.setMaximumWidth(50)
        self.lineeditlastname = QtWidgets.QLineEdit()
        self.lineeditlastname.setPlaceholderText('Введите Вашу фамилию...')
        lastnamebox = QtWidgets.QHBoxLayout()
        lastnamebox.addWidget(self.labellastname)
        lastnamebox.addWidget(self.lineeditlastname)

        self.labelfirstname = QtWidgets.QLabel('Имя')
        self.labelfirstname.setMinimumWidth(50)
        self.lineeditfirstname = QtWidgets.QLineEdit()
        self.lineeditfirstname.setPlaceholderText('Введите Ваше имя...')
        firstnamebox = QtWidgets.QHBoxLayout()
        firstnamebox.addWidget(self.labelfirstname)
        firstnamebox.addWidget(self.lineeditfirstname)

        self.labelmiddlename = QtWidgets.QLabel('Отчество')
        self.labelmiddlename.setMinimumWidth(50)
        self.lineeditmiddlename = QtWidgets.QLineEdit()
        self.lineeditmiddlename.setPlaceholderText('Введите отчество...')
        middlenamebox = QtWidgets.QHBoxLayout()
        middlenamebox.addWidget(self.labelmiddlename)
        middlenamebox.addWidget(self.lineeditmiddlename)

        self.labelphone = QtWidgets.QLabel('Телефон')
        self.labelphone.setMinimumWidth(50)
        self.lineeditphone = QtWidgets.QLineEdit()
        self.lineeditphone.setPlaceholderText('Введите номер телефона...')
        phonebox = QtWidgets.QHBoxLayout()
        phonebox.addWidget(self.labelphone)
        phonebox.addWidget(self.lineeditphone)

        mainbox = QtWidgets.QVBoxLayout()
        mainbox.addLayout(lastnamebox)
        mainbox.addLayout(firstnamebox)
        mainbox.addLayout(middlenamebox)
        mainbox.addLayout(phonebox)
        self.setLayout(mainbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Анкетная карточка')
    window.resize(300, 100)
    window.show()

    app.exec_()


