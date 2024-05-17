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

        self.lat = 0
        self.lon = 0
        self.initUI()
        self.initSignals()

    def initUI(self) -> None:

        lat_layout_h = QtWidgets.QHBoxLayout()
        lon_layout_h = QtWidgets.QHBoxLayout()
        vert_layout = QtWidgets.QVBoxLayout()
        main_h_layout = QtWidgets.QHBoxLayout()

        self.latitude_lineedit = QtWidgets.QLineEdit()
        self.latitude_lineedit.setText(str(self.lat))
        self.latitude_label = QtWidgets.QLabel('Широта:')
        self.longitude_lineedit = QtWidgets.QLineEdit()
        self.longitude_lineedit.setText(str(self.lon))
        self.longitude_label = QtWidgets.QLabel('Долгота:')
        self.spinbox_delay = QtWidgets.QSpinBox()
        self.spinbox_delay.setMinimum(1)
        self.weather_plaintextedit = QtWidgets.QPlainTextEdit()
        self.push_button = QtWidgets.QPushButton('Запустить')
        self.push_button.setCheckable(True)

        lat_layout_h.addWidget(self.latitude_label)
        lat_layout_h.addWidget(self.latitude_lineedit)

        lon_layout_h.addWidget(self.longitude_label)
        lon_layout_h.addWidget(self.longitude_lineedit)

        vert_layout.addLayout(lat_layout_h)
        vert_layout.addLayout(lon_layout_h)
        vert_layout.addWidget(self.spinbox_delay)
        vert_layout.addWidget(self.push_button)

        main_h_layout.addLayout(vert_layout)
        main_h_layout.addWidget(self.weather_plaintextedit)

        self.setLayout(main_h_layout)

    def initSignals(self):
        self.push_button.clicked.connect(self.on_started)
        #self.weatherHandler.weatherHandler.connect(self.get_signal_from_thread)
        #self.latitude_lineedit.textChanged.connect(self.lat_lon_changed)

    def on_started(self):
        self.weatherHandler = WeatherHandler(lat=int(self.latitude_lineedit.text()), lon=int(self.longitude_lineedit.text()))
        self.weatherHandler.start()
        self.weatherHandler.weatherHandler.connect(self.get_signal_from_thread)

    def get_signal_from_thread(self, s):
        if self.push_button.isChecked():
            self.push_button.setText('Остановить')
            self.weather_plaintextedit.appendPlainText(s)
        elif not self.push_button.isChecked():
            self.weatherHandler.terminate()
            self.push_button.setText('Запустить')

    """def lat_lon_changed(self, s):
        #lat = int(self.latitude_lineedit.text())
        #lon = int(self.longitude_lineedit.text())
        if not self.weatherHandler.isRunning():
            if self.push_button.isChecked():
                # self.weatherHandler.lat = int(self.latitude_lineedit.text())
                # print(self.lat)
                self.push_button.setText('Остановить')
                self.weatherHandler.start()
                self.weather_plaintextedit.appendPlainText(s)
            elif not self.push_button.isChecked():
                self.weatherHandler.terminate()
                self.push_button.setText('Запустить')"""




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(800, 200)
    window.show()

    app.exec()
