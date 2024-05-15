"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import time
from typing import Tuple, Any

import psutil
from PySide6 import QtWidgets, QtCore


class CpuRamInfo(QtCore.QThread):
    CpuRamInfoReceived = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None
        self.status = True

    def run(self):
        if self.delay is None:
            self.delay = 1

        while True:
            time.sleep(self.delay)

    def get_cpu_value(self):
        cpu_value = psutil.cpu_percent()
        return cpu_value

    def get_ram_value(self):
        ram_value = psutil.virtual_memory().percent
        return ram_value


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.start_button = None
        self.field_delay = None
        self.ram_label = None
        self.cpu_label = None
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        l = QtWidgets.QHBoxLayout()

        self.field_delay = QtWidgets.QSpinBox()
        self.cpu_label = QtWidgets.QLineEdit()
        self.cpu_label.setPlaceholderText(f'загрузка CPU: {psutil.cpu_percent()}')
        self.ram_label = QtWidgets.QLineEdit()
        self.ram_label.setPlaceholderText(f'загрузка RAM: {psutil.virtual_memory().percent}')
        self.start_button = QtWidgets.QPushButton('Запуск')

        l.addWidget(self.field_delay)
        l.addWidget(self.cpu_label)
        l.addWidget(self.ram_label)
        l.addWidget(self.start_button)

        self.setLayout(l)

        self.cpu_ram_info = CpuRamInfo()

    def initSignals(self):
        self.start_button.clicked.connect(self.on_started)
        pass

    def on_started(self):
        if not self.cpu_ram_info.isRunning():
            self.cpu_ram_info.start()
            self.cpu_label.setPlaceholderText(f'загрузка CPU: {self.cpu_ram_info.get_cpu_value}')
            self.ram_label.setPlaceholderText(f'загрузка RAM: {self.cpu_ram_info.get_ram_value}')

    def on_changed(self):
        if self.field_delay.textChanged():
            delay = self.field_delay.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()