import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from ui_calculator import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for button in self.findChildren(QPushButton):
            button.clicked.connect(self.common_slot)

    def common_slot(self):
        sender = self.sender()
        sender_text = sender.text()
        if sender.text() in "01234567890()-+*/.":
            current_text = self.lineEdit.text()
            self.lineEdit.setText(current_text + sender_text)
        elif sender_text == "=":
            current_text = self.lineEdit.text()
            result = eval(current_text)
            self.lineEdit.setText(str(result))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())