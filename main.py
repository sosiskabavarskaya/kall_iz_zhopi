import sys
import traceback
# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from ui_calc_two_numbers import Ui_MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sum_two_numbers)

    def sum_two_numbers(self):
        number1 = self.lineEdit.text()
        if number1:
            number1 = float(number1)
        number2 = self.lineEdit_2.text()
        if number2:
            number2 = float(number2)
        if number1 and number2:
            self.label_result.setText(str(number1 + number2))


sys.excepthook = except_hook


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
