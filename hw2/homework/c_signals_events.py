"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication

from hw2.homework.ui.signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        self.ui.pushButtonLB.clicked.connect(self.pushButtonLBClicked)
        self.ui.pushButtonLT.clicked.connect(self.pushButtonLTClicked)
        self.ui.pushButtonRT.clicked.connect(self.pushButtonRTClicked)
        self.ui.pushButtonRB.clicked.connect(self.pushButtonRBClicked)
        self.ui.pushButtonCenter.clicked.connect(self.pushButtonCenterClicked)
        self.ui.spinBoxX.textChanged.connect(self.spinBoxXTextChanged)
        self.ui.spinBoxY.textChanged.connect(self.spinBoxXTextChanged)
        self.ui.pushButtonMoveCoords.clicked.connect(self.pushButtonMoveCoordsClicked)
        self.ui.pushButtonGetData.clicked.connect(self.pushButtonGetDataClicked)

    def windowUserMove(self):
        print('working')

    def getscreensize(self):
        x, y = QApplication.primaryScreen().size().toTuple()
        return x, y
    # slots --------------------------------------------------------------

    def pushButtonLBClicked(self) -> None:  # влево-вниз
        x, y = self.getscreensize()
        self.window().move(0, y-window.height())
        self.new_coordinate_by_window()
        #self.window().move(0, 300)
        pass

    def pushButtonLTClicked(self) -> None:  # влево-вверх
        self.window().move(0, 0)
        self.new_coordinate_by_window()
        pass

    def pushButtonRTClicked(self) -> None:  # вправо-вверх
        x, y = self.getscreensize()
        self.window().move(x - window.width(), 0)
        self.new_coordinate_by_window()
        #self.window().move(700, 0)
        pass

    def pushButtonRBClicked(self) -> None:  # вправо-вниз
        x, y = self.getscreensize()
        self.window().move(x-window.width(), y-window.height())
        self.new_coordinate_by_window()
        #self.window().move(700, 300)
        pass

    def pushButtonCenterClicked(self):
        qr = self.window().frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.new_coordinate_by_window()

    def pushButtonMoveCoordsClicked(self):
        self.window().move(int(self.ui.spinBoxX.text()), int(self.ui.spinBoxY.text()))
        self.new_coordinate_by_window()


    def pushButtonGetDataClicked(self):
        width_, height_ = self.window().size().toTuple()
        coord_x = self.window().x()
        coord_y = self.window().y()
        min_size_window_width, min_size_window_height = self.window().minimumSize().toTuple()
        screen_size_w, screen_size_h = self.getscreensize()
        if self.window().isVisible():
            status_window = 'Развернуто'
        else:
            status_window = 'Свернуто'

        count_screens = len(QApplication.screens())
        self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Размер окна: width={width_}, height={height_}\n'
                                           f'{time.ctime()}: Текущее расположение (координаты) окна: x={coord_x}, y={coord_y}\n'
                                           f'{time.ctime()}: Минимальные размеры окна: width={min_size_window_width}, height={min_size_window_height}\n'
                                           f'{time.ctime()}: Разрешение экрана: {screen_size_w} * {screen_size_h}\n'
                                           f'{time.ctime()}: Статус окна (свернуто/развернуто): {status_window}\n'
                                           f'{time.ctime()}: Количество экранов: {count_screens}')

        pass

    def new_coordinate_by_window(self):
        coord_x = self.window().x()
        coord_y = self.window().y()
        self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Новые координаты окна: x={coord_x}, y={coord_y}')

    def spinBoxXTextChanged(self):
        x, y = self.getscreensize()
        self.ui.spinBoxX.setFixedSize(100, 40)
        self.ui.spinBoxX.setSingleStep(10)
        self.ui.spinBoxY.setFixedSize(100, 40)
        self.ui.spinBoxY.setSingleStep(10)
        self.ui.spinBoxX.setRange(0, x)
        self.ui.spinBoxY.setRange(0, y)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
