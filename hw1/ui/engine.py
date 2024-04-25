from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):
        hbox = QtWidgets.QHBoxLayout()

        engines = ['Двигатель №1', 'Двигатель №2', 'Двигатель №3', 'Двигатель №4']

        for engine_ in engines:
            engine = QtWidgets.QVBoxLayout()
            slider = QtWidgets.QSlider()
            label = QtWidgets.QLabel(engine_)
            engine.addWidget(slider, alignment=Qt.AlignmentFlag.AlignCenter)
            engine.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
            hbox.addLayout(engine)

        vbox = QtWidgets.QVBoxLayout()
        vhbox = QtWidgets.QHBoxLayout()
        hspacer = QtWidgets.QSlider(Qt.Horizontal, self)
        slider = QtWidgets.QSlider()
        vhbox.addWidget(hspacer, alignment=Qt.AlignmentFlag.AlignCenter)
        vhbox.addWidget(slider, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(vhbox)
        lbl = QtWidgets.QLabel('Общая тяга')
        vbox.addWidget(lbl)
        hbox.addLayout(vbox)

        self.setLayout(hbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(700, 150)
    window.setWindowTitle('Параметры корабля')
    window.show()

    app.exec_()

