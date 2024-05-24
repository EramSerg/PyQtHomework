import datetime
import json
import os

import requests
from PySide6 import QtWidgets, QtCore, QtGui


class WeatherWindow(QtWidgets.QWidget):
    def __init__(self, lat=None, lon=None, parent=None):
        super().__init__(parent)

        self.lat = 10
        self.lon = 10
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true"
        self.window().setWindowTitle('Погода')
        self.window().setWindowIcon(QtGui.QIcon('icons8-погода-48.png'))
        self.initUI()
        self.initSignals()

    def initUI(self):

        l_h_coord_layout = QtWidgets.QHBoxLayout()

        self.latitude_lineedit = QtWidgets.QLineEdit()
        self.latitude_lineedit.setText(str(self.lat))
        self.latitude_label = QtWidgets.QLabel('Широта:')
        self.longitude_lineedit = QtWidgets.QLineEdit()
        self.longitude_lineedit.setText(str(self.lon))
        self.longitude_label = QtWidgets.QLabel('Долгота:')

        l_h_coord_layout.addWidget(self.latitude_label)
        l_h_coord_layout.addWidget(self.latitude_lineedit)
        l_h_coord_layout.addWidget(self.longitude_label)
        l_h_coord_layout.addWidget(self.longitude_lineedit)

        l_v_layout = QtWidgets.QVBoxLayout()

        self.spb_weather = QtWidgets.QLineEdit()
        self.spb_weather.setFixedSize(200, 25)
        self.spb_weather.setReadOnly(True)
        self.weather_plaintextedit = QtWidgets.QPlainTextEdit()
        self.get_weather_push_button = QtWidgets.QPushButton('Погода')

        l_v_layout.addLayout(l_h_coord_layout)
        l_v_layout.addWidget(self.spb_weather)
        l_v_layout.addWidget(self.weather_plaintextedit)
        l_v_layout.addWidget(self.get_weather_push_button)

        l_h_add_spb_weather_layout = QtWidgets.QHBoxLayout()

        l_h_add_spb_weather_layout.addLayout(l_v_layout)

        self.setLayout(l_h_add_spb_weather_layout)

    def initSignals(self):
        self.get_weather_push_button.clicked.connect(self.get_weather)

    def get_weather(self):
        lat = float(self.latitude_lineedit.text())
        lon = float(self.longitude_lineedit.text())
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
        response_spb = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=59&longitude=30&current_weather=true")
        data = response.json()
        lat = data['latitude']
        lon = data['longitude']
        current_weather = data['current_weather']
        e_data = f'latitude: {lat}, longitude: {lon}, current_weather: {current_weather}'
        self.weather_plaintextedit.appendPlainText(e_data)
        data_spb = response_spb.json()
        print(data_spb)
        self.spb_weather.setText(f"Температура в СПб: {str(data_spb['current_weather']['temperature'])} {data_spb['current_weather_units']['temperature']}")


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        now = str(datetime.datetime.now().date())  # получаем текущую дату
        print(now)
        self.tasks = self.view_case_list()  # получаем список дел

        self.initUI()
        self.initChilds()
        self.initSignals()

    def initUI(self) -> None:
        # Блок кнопок допустимых комманд
        l_horiz_btn = QtWidgets.QVBoxLayout()
        self.current_date_label = QtWidgets.QLabel('Дата: ')
        self.add_event_btn = QtWidgets.QPushButton('ADD')
        self.add_event_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.add_event_btn.setFixedSize(80, 25)
        self.add_event_btn.setIcon(QtGui.QIcon('icons8-добавить-48.png'))
        self.show_event_btn = QtWidgets.QPushButton('SHOW')
        self.show_event_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.show_event_btn.setFixedSize(80, 25)
        self.show_event_btn.setIcon(QtGui.QIcon('icons8-показать-50.png'))
        self.show_all_event_btn = QtWidgets.QPushButton('SHOW_ALL')
        self.show_all_event_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.show_all_event_btn.setFixedSize(80, 25)
        self.show_all_event_btn.setIcon(QtGui.QIcon('icons8-показать-50.png'))
        self.del_event_btn = QtWidgets.QPushButton('DEL')
        self.del_event_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.del_event_btn.setFixedSize(80, 25)
        self.del_event_btn.setIcon(QtGui.QIcon('icons8-del-24.png'))
        self.weather_btn = QtWidgets.QPushButton('WEATHER')
        self.weather_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.weather_btn.setFixedSize(80, 25)
        self.weather_btn.setIcon(QtGui.QIcon('icons8-погода-48.png'))
        self.stop_btn = QtWidgets.QPushButton('EXIT')
        self.stop_btn.setStyleSheet(f'border: 1px solid black; border-radius: 5px;')
        self.stop_btn.setFixedSize(80, 25)
        self.stop_btn.setIcon(QtGui.QIcon('icons8-пожарный-выход-16.png'))

        l_horiz_btn.addWidget(self.current_date_label)
        l_horiz_btn.addWidget(self.add_event_btn)
        l_horiz_btn.addWidget(self.show_event_btn)
        l_horiz_btn.addWidget(self.show_all_event_btn)
        l_horiz_btn.addWidget(self.del_event_btn)
        l_horiz_btn.addWidget(self.weather_btn)
        l_horiz_btn.addWidget(self.stop_btn)
        l_horiz_btn.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding))

        # блок окон вывода
        l_vert_output_layout = QtWidgets.QVBoxLayout()

        # блок даты/время/user
        self.date_time_user_layout = QtWidgets.QHBoxLayout()
        self.current_date = QtWidgets.QDateEdit()
        self.current_date.setMinimumSize(140, 25)
        self.current_date.setCalendarPopup(True)
        self.today_button = QtWidgets.QPushButton('Today')
        self.current_date.calendarWidget().layout().addWidget(self.today_button)
        self.current_time = QtWidgets.QTimeEdit()
        self.current_time.setMinimumSize(100, 25)
        self.user_name = QtWidgets.QLineEdit()

        self.date_time_user_layout.addWidget(self.current_date)
        self.date_time_user_layout.addWidget(self.current_time)
        self.date_time_user_layout.addWidget(self.user_name)

        self.add_event_lineedit = QtWidgets.QLineEdit()
        self.add_event_lineedit.setPlaceholderText('Добавьте событие')
        self.output_plaintextedit = QtWidgets.QPlainTextEdit()
        l_vert_output_layout.addLayout(self.date_time_user_layout)
        l_vert_output_layout.addWidget(self.add_event_lineedit)
        l_vert_output_layout.addWidget(self.output_plaintextedit)

        # main layout
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(l_horiz_btn)
        main_layout.addLayout(l_vert_output_layout)

        self.setLayout(main_layout)

    def initChilds(self):
        self.__weatherWindow = WeatherWindow()

    def initSignals(self):
        # сигнал на добавление события
        self.add_event_btn.clicked.connect(self.add_event)

        # сигнал отображения события за выбранную дату для выбранного user'a
        self.show_event_btn.clicked.connect(self.show_event)

        # сигнал отображения всех событий
        self.show_all_event_btn.clicked.connect(self.show_all_event)

        # сигнал отображения старых событий и возможности их удаления
        self.del_event_btn.clicked.connect(self.del_event)

        # сигнал нажатия кнопки календаря "сегодня" для применения даты
        self.today_button.clicked.connect(self.set_today)

        # сигнал нажатия кнопки "weather" для отображения погоды
        self.weather_btn.clicked.connect(self.__weatherWindow.show)

    def set_today(self):
        today = QtCore.QDate().currentDate()
        self.current_date.calendarWidget().setSelectedDate(today)

    def show_event(self):
        date = self.current_date.text()
        name = self.user_name.text()
        if date in self.tasks:  # проверяем наличие даты в списке дел
            if name in self.tasks[self.current_date.text()]:  # проверяем существование пользователя в списке дел
                task_list = sorted(self.tasks[self.current_date.text()][name], key=lambda x: x[1])  # сортируем список дел по времени события
                for task in task_list:  # перебираем все дела для пользователя за указанную дату
                    print(name, '- ', task[0], '-', task[1])
                    self.output_plaintextedit.appendPlainText(f'{name} - {task[0]} - {task[1]}')
            else:
                self.output_plaintextedit.appendPlainText(f'Событий для даты {date} для пользователя {name} не найдено!')
        else:
            self.output_plaintextedit.appendPlainText(f'Событий для даты {date} не найдено!')

    def show_all_event(self):
        #self.output_plaintextedit.appendPlainText(f'{self.view_case_list()}')
        self.output_plaintextedit.appendPlainText(json.dumps(self.view_case_list(), ensure_ascii=True, indent=4))

    def del_event(self):
        for date in self.tasks:
            correct_date = datetime.date(*[int(x) for x in date.split('.')[::-1]])
            if correct_date < datetime.datetime.now().date():
                self.output_plaintextedit.appendPlainText(f'Есть старые записи...{date} - Запись: {self.tasks[date]}')
                answer = QtWidgets.QMessageBox.question(self, 'Предупреждение', f'Хотите удалить запись {self.tasks[date]}?')
                if answer == QtWidgets.QMessageBox.Yes:
                    self.output_plaintextedit.appendPlainText(f'Запись {self.tasks[date]} удалена!')
                elif answer == QtWidgets.QMessageBox.No:
                    self.output_plaintextedit.appendPlainText(f'Удаление записи {self.tasks[date]} отменено!')
            else:
                self.output_plaintextedit.setPlainText('Старые записи не обнаружены...')
                QtWidgets.QMessageBox.information(self, 'Информация', 'Старые записи не найдены!')

    def view_case_list(self):
        """Функция просмотра списка дел
        :return список дел в формате json"""

        if os.path.exists('case_list.json'):  # проверяем существует ли case_list.json
            with open('case_list.json', 'r', encoding='utf-8') as case_list:  # читаем список дел из case_list.json
                return json.load(case_list)

        case_list = {}  # Создаём пустой список
        with open('case_list.json', mode='x', encoding='utf-8') as f:  # Создаём файл и записываем туда пустой список
            json.dump(case_list, f)

        return sorted(case_list)

    def add_todo(self, task, name, case_time):
        """Функция добавления новой записи в список дел
        :param task - описание нового события
        :param name - имя пользователя, для которого необходимо внести новое событие
        :param case_time - время события
        :return - возвращает отбивку об успешном добавлении нового события для выбранной даты"""
        if self.current_date.text() not in self.tasks:  # если даты нет в списке дел
            self.tasks[self.current_date.text()] = {}  # создаем словарь для новой даты
        if self.user_name.text() not in self.tasks[self.current_date.text()]:  # если пользователя нет в списке дел
            self.tasks[self.current_date.text()][self.user_name.text()] = []  # создаем список для записей за дату

        self.tasks[self.current_date.text()][self.user_name.text()].append(
            [self.add_event_lineedit.text(), self.current_time.text()])  # добавлем новое дело для выбранных пользователя и даты
        self.output_plaintextedit.setPlainText(f'Задача {self.add_event_lineedit.text()} для пользователя {self.user_name.text()} на время {self.current_time.text()} добавлена на дату {self.current_date.text()}')
        QtWidgets.QMessageBox.information(self, 'Информация', 'Новое событие добавлено в список дел!')

    """def add_event(self):
        #task = self.add_event_lineedit.text()
        task = self.add_event_lineedit.text() if self.add_event_lineedit.text() else QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Добавьте задачу!')
        name = self.user_name.text()
        case_time = self.current_time.text()
        self.add_todo(task, name, case_time)
        self.write_case_list(self.tasks)"""

    def add_event(self):
        if not self.add_event_lineedit.text():
            return QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Добавьте задачу!')
        if not self.user_name.text():
            return QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Добавьте имя пользователя!')
        if not self.current_time.text():
            return QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не указана дата события!')

        task = self.add_event_lineedit.text()
        name = self.user_name.text()
        case_time = self.current_time.text()
        self.add_todo(task, name, case_time)
        self.write_case_list(self.tasks)

    def write_case_list(self, c_list):
        """Функция для записи списка дел в файл case_list.json"""
        with open('case_list.json', 'w', encoding='utf-8') as case_list:
            json.dump(self.tasks, case_list)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Планировщик задач')
    window.setWindowIcon(QtGui.QIcon('icons8-create-64.png'))
    window.resize(800, 200)
    window.show()

    app.exec()
