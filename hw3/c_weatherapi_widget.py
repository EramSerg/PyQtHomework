"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:

        l_v = QtWidgets.QVBoxLayout()
        l_v2 = QtWidgets.QVBoxLayout()
        l_h = QtWidgets.QHBoxLayout()

        self.latitude_lineedit = QtWidgets.QLineEdit()
        self.latitude_lineedit.setPlaceholderText('Широта: ')
        self.longitude_lineedit = QtWidgets.QLineEdit()
        self.longitude_lineedit.setPlaceholderText('Долгота: ')
        self.spinbox_delay = QtWidgets.QSpinBox()
        self.spinbox_delay.setMinimum(1)
        self.weather_plaintextedit = QtWidgets.QPlainTextEdit()
        self.push_button = QtWidgets.QPushButton('Запустить')
        self.push_button.setCheckable(True)

        l_v.addWidget(self.latitude_lineedit)
        l_v.addWidget(self.longitude_lineedit)
        l_v.addWidget(self.spinbox_delay)

        l_h.addLayout(l_v)
        l_h.addWidget(self.weather_plaintextedit)

        l_v2.addLayout(l_v)
        l_v2.addLayout(l_h)
        l_v2.addWidget(self.push_button)

        self.setLayout(l_v2)
        self.weatherHandler = WeatherHandler(lat=None, lon=None)


    def initSignals(self):
        self.push_button.clicked.connect(self.push_button_clicked_connect)
        self.weatherHandler.weatherHandler.connect(self.push_button_clicked_connect)

    def push_button_clicked_connect(self):
        lat = int(self.latitude_lineedit.text())
        lon = int(self.longitude_lineedit.text())
        self.weatherHandler.start()
        self.weather_plaintextedit.setPlaceholderText(self.weatherHandler.weatherHandler(lat, lon))
        print(self.weatherHandler.weatherHandler(lat, lon))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(400, 100)
    window.show()

    app.exec()
