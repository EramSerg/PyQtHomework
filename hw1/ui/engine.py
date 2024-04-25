from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        hbox = QtWidgets.QHBoxLayout()

        engines = ['Двигатель №1', 'Двигатель №2', 'Двигатель №3', 'Двигатель №4']

        for engine_ in engines:
            engine = QtWidgets.QVBoxLayout()
            slider = QtWidgets.QSlider()
            label = QtWidgets.QLabel(engine_)
            engine.addWidget(slider)
            engine.addWidget(label)
            hbox.addLayout(engine)

        vbox = QtWidgets.QVBoxLayout()
        vhbox = QtWidgets.QHBoxLayout()
        hspacer = QtWidgets.QSlider()
        slider = QtWidgets.QSlider()
        vhbox.addWidget(hspacer)
        vhbox.addWidget(slider)
        vbox.addLayout(vhbox)
        lbl = QtWidgets.QLabel('Общая тяга')
        vbox.addWidget(lbl)
        hbox.addLayout(vbox)

        self.setLayout(hbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(300, 100)
    window.setWindowTitle('Параметры корабля')
    window.show()

    app.exec_()

