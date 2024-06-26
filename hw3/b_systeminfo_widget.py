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


class CpuRamInfoThread(QtCore.QThread):
    CpuRamInfoReceived = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None
        self.status = True

    def run(self):
        if self.delay is None:
            self.delay = 1
            self.sleep(self.delay)
            self.CpuRamInfoReceived.emit(self.get_cpu_value())
            self.CpuRamInfoReceived.emit(self.get_ram_value())
        else:
            self.sleep(self.delay)
            self.CpuRamInfoReceived.emit(self.get_cpu_value())
            self.CpuRamInfoReceived.emit(self.get_ram_value())

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
        self.field_delay.setMinimumSize(60, 20)
        self.cpu_label = QtWidgets.QLineEdit()
        self.cpu_label.setText(f'загрузка CPU: {psutil.cpu_percent()}')
        self.ram_label = QtWidgets.QLineEdit()
        self.ram_label.setText(f'загрузка RAM: {psutil.virtual_memory().percent}')
        self.start_button = QtWidgets.QPushButton('Запуск')
        self.stop_button = QtWidgets.QPushButton('Остановить')

        l.addWidget(self.field_delay)
        l.addWidget(self.cpu_label)
        l.addWidget(self.ram_label)
        l.addWidget(self.start_button)
        l.addWidget(self.stop_button)

        self.setLayout(l)

        self.cpu_ram_info = CpuRamInfoThread()
        self.cpu_ram_info.start()

    def initSignals(self):
        #self.start_button.clicked.connect(self.on_started)
        #self.stop_button.clicked.connect(self.on_finished)
        self.cpu_ram_info.CpuRamInfoReceived.connect(self.on_started)
        self.field_delay.textChanged.connect(self.on_changed)
        pass

    def on_started(self):
        if not self.cpu_ram_info.isRunning():
            #self.start_button.setDisabled(True)
            #self.stop_button.setDisabled(True)
            self.cpu_ram_info.start()
            self.cpu_label.setText(f'загрузка CPU: {self.cpu_ram_info.get_cpu_value()}')
            self.ram_label.setText(f'загрузка RAM: {self.cpu_ram_info.get_ram_value()}')

    """def on_finished(self):
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)"""


    def on_changed(self):
        delay = int(self.field_delay.text())
        self.cpu_ram_info.delay = delay
        self.cpu_ram_info.start()
        self.cpu_ram_info.run()
        self.cpu_label.setText(f'загрузка CPU: {self.cpu_ram_info.get_cpu_value()}')
        self.ram_label.setText(f'загрузка RAM: {self.cpu_ram_info.get_ram_value()}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(400, 100)
    window.show()

    app.exec()