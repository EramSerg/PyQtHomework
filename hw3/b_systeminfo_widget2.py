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
        l_vertic = QtWidgets.QVBoxLayout()

        self.field_delay = QtWidgets.QSpinBox()
        self.field_delay.setMinimumSize(60, 20)
        self.cpu_label = QtWidgets.QLineEdit()
        self.cpu_label.setPlaceholderText(f'загрузка CPU: ')
        self.ram_label = QtWidgets.QLineEdit()
        self.ram_label.setPlaceholderText(f'загрузка RAM: ')

        l_vertic.addWidget(self.field_delay)
        l_vertic.addWidget(self.cpu_label)
        l_vertic.addWidget(self.ram_label)


        self.setLayout(l_vertic)

        self.cpu_ram_info = CpuRamInfoThread()
        self.cpu_ram_info.start()

    def initSignals(self):
        self.cpu_ram_info.CpuRamInfoReceived.connect(self.on_started)
        self.field_delay.textChanged.connect(self.on_changed)

    def on_started(self):
        if not self.cpu_ram_info.isRunning():
            self.cpu_ram_info.start()
            self.cpu_label.setText(f'загрузка CPU: {self.cpu_ram_info.get_cpu_value()}')
            self.ram_label.setText(f'загрузка RAM: {self.cpu_ram_info.get_ram_value()}')

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
