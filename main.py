import datetime

from hw1.ui.login import Window as LoginWidget
from hw1.ui.fio import Window as FioWidget
from hw1.ui.BoatParametres import Window as BoatParamWidget
from hw1.ui.engine import Window as EnginesWidget
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from datetime import datetime

current_date = datetime.now().date()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):
        self.setWindowTitle('Программулька')

        fiologinbox = QtWidgets.QVBoxLayout()
        self.loginWidget = LoginWidget()
        self.fioWidget = FioWidget()
        self.boatparamWidget = BoatParamWidget()
        fiologinbox.addWidget(self.loginWidget)
        fiologinbox.addWidget(self.fioWidget)
        fiologinbox.addWidget(self.boatparamWidget)

        boatparambox = QtWidgets.QVBoxLayout()
        self.enginesWidget = EnginesWidget()
        self.comment = QtWidgets.QTextEdit()
        self.comment.setPlainText(f'Бортовой журнал за дату {current_date}:')
        boatparambox.addWidget(self.enginesWidget)
        boatparambox.addWidget(self.comment)

        mainbox = QtWidgets.QHBoxLayout()
        mainbox.addLayout(fiologinbox)
        mainbox.addLayout(boatparambox)
        self.setLayout(mainbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Авторизация')
    #window.resize(500, 200)
    window.show()

    app.exec_()