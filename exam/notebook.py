import datetime
import json
import os
import telebot

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        now = str(datetime.datetime.now().date())  # получаем текущую дату
        print(now)
        self.tasks = self.view_case_list()  # получаем список дел

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:
        # Блок кнопок допустимых комманд
        l_horiz_btn = QtWidgets.QVBoxLayout()

        self.current_date_label = QtWidgets.QLabel('Дата: ')
        self.add_event_btn = QtWidgets.QPushButton('ADD')
        self.show_event_btn = QtWidgets.QPushButton('SHOW')
        self.show_all_event_btn = QtWidgets.QPushButton('SHOW_ALL')
        self.del_event_btn = QtWidgets.QPushButton('DEL')
        self.stop_btn = QtWidgets.QPushButton('EXIT')

        l_horiz_btn.addWidget(self.current_date_label)
        l_horiz_btn.addWidget(self.add_event_btn)
        l_horiz_btn.addWidget(self.show_event_btn)
        l_horiz_btn.addWidget(self.show_all_event_btn)
        l_horiz_btn.addWidget(self.del_event_btn)
        l_horiz_btn.addWidget(self.stop_btn)

        # блок окон вывода
        l_vert_output_layout = QtWidgets.QVBoxLayout()

        # блок даты/время/user
        self.date_time_user_layout = QtWidgets.QHBoxLayout()
        self.current_date = QtWidgets.QDateEdit()
        self.current_date.setMinimumSize(140, 25)
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

    def initSignals(self):
        # сигнал на добавление события
        self.add_event_btn.clicked.connect(self.add_event)
        self.show_event_btn.clicked.connect(self.show_event)
        self.show_all_event_btn.clicked.connect(self.show_all_event)
        self.del_event_btn.clicked.connect(self.del_event)

    def show_event(self):
        date = self.current_date.text()
        if self.current_date.text() in self.tasks:  # проверяем наличие даты в списке дел
            for name in self.tasks[self.current_date.text()]:  # проверяем существование пользователя в списке дел
                task_list = sorted(self.tasks[self.current_date.text()][name], key=lambda x: x[1])  # сортируем список дел по времени события
                for task in task_list:  # перебираем все дела для пользователя за указанную дату
                    print(name, '- ', task[0], '-', task[1])
                    self.output_plaintextedit.setPlainText(f'{name} - {task[0]} - {task[1]}')

    def show_all_event(self):
        self.output_plaintextedit.setPlainText(f'{self.view_case_list()}')

    def del_event(self):
        for date in self.tasks:
            correct_date = datetime.date(*[int(x) for x in date.split('.')[::-1]])
            print(correct_date)
            if correct_date < datetime.datetime.now().date():
                self.output_plaintextedit.setPlainText(f'Есть старые записи...{date} - Запись: {self.tasks[date]}')
            else:
                self.output_plaintextedit.setPlainText('Старые записи не обнаружены...')

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
        self.output_plaintextedit.setPlainText(f'Задача {self.add_event_lineedit.text()} на время {self.current_time.text()} добавлена на дату {self.current_date.text()}')

    def add_event(self):
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
    window.resize(800, 200)
    window.show()

    app.exec()
