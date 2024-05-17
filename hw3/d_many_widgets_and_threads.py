"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtCore
from b_systeminfo_widget import Window as Widget_One
from c_weatherapi_widget import Window as Widget_Two


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_one = Widget_One()
        self.ui_two = Widget_Two()
        self.initUI()

    def initUI(self):
        l_horiz = QtWidgets.QHBoxLayout()
        l_horiz.addWidget(self.ui_one)
        l_horiz.addWidget(self.ui_two)

        self.setLayout(l_horiz)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(800, 200)
    window.show()

    app.exec()