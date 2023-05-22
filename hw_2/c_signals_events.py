"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

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

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QGuiApplication

from hw_2.ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    # signals pushButtons
    def initSignals(self) -> None:
        """
        Инициализация сигналов при нажатии кнопок pushButtons
        :return: None
        """
        self.ui.pushButtonLT.clicked.connect(self.onPbButtonLT)
        self.ui.pushButtonRT.clicked.connect(self.onPbButtonRT)
        self.ui.pushButtonLB.clicked.connect(self.onPbButtonLB)
        self.ui.pushButtonRB.clicked.connect(self.onPbButtonRB)
        self.ui.pushButtonCenter.clicked.connect(self.onPbWindowCenter)

        self.ui.pushButtonMoveCoords.clicked.connect(self.onPbMoveCoords)
        self.ui.pushButtonGetData.clicked.connect(self.onPbGetData)

    # slots pushButtons
    def onPbMoveCoords(self) -> None:
        """
        Слот перемещения окна при нажатии кнопки "Переместить"
        :return: None
        """
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPbButtonLT(self) -> None:
        """
        Слот перемещния окна в левый верхний угол при нажатии кнопки "Лево/Верх"
        :return: None
        """
        self.move(0, 0)

    def onPbButtonRT(self) -> None:
        """
        Слот перемещния окна в правый верхний угол при нажатии кнопки "Право/Верх"
        :return: None
        """
        self.move(600, 0)

    def onPbButtonLB(self) -> None:
        """
        Слот перемещния окна в левый нижний угол при нажатии кнопки "Лево/Низ"
        :return: None
        """
        self.move(0, 300)

    def onPbButtonRB(self) -> None:
        """
        Слот перемещния окна в правый нижний угол при нажатии кнопки "Право/Низ"
        :return: None
        """
        self.move(600, 300)

    def onPbWindowCenter(self) -> None:
        """
        Слот перемещния окна в центр при нажатии кнопки "Центр"
        :return: None
        """
        self.move(300, 150)

    def onPbGetData(self):
        """
        Слот получения лога в окно plainTextEdit при нажатии кнопки "Получить данные окна"
        :return:
        """
        monitors = len(QtWidgets.QApplication.screens())  # кол-во экранов
        active_window = QtWidgets.QApplication.activeWindow().windowTitle()  # текущее основное окно
        monitor_property = QtGui.QScreen()  # разрешение экрана в виде объекта
        monitor_size = monitor_property.size()

        size = self.size()  # размеры окна в виде объекта QSize
        pos = self.pos()  # положение окна в виде объекта QPoint

        x_center, y_center = ((pos.x() + size.width()) / 2, (pos.y() + size.height()) / 2)  # координаты центра приложения

        min_size = self.minimumSize()  # минимальные размеры окна в виде объекта QSize
        active = self.isActiveWindow()  # проверка активности окна
        hidden = self.isHidden()  # проверка свернутости окна
        visible = self.isVisible()
        enabled = self.isEnabled()


        self.ui.plainTextEdit.appendPlainText(f'Кол-во экранов: "{monitors}" ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Текущее основное окно: "{active_window}" ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Разрешение экрана: "{monitor_size}" ------ {time.ctime()}')

        self.ui.plainTextEdit.appendPlainText(f'Размеры окна: {size.width()} x {size.height()} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Мин размеры окна: {min_size.width()} x {min_size.height()} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Текущее положение окна: {pos.x()}, {pos.y()} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Координаты центра приложения: {x_center}, {y_center} ------ {time.ctime()}')

        self.ui.plainTextEdit.appendPlainText(f'Активно окно: {str(active)} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Свернуто окно: {str(hidden)} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Отображено окно: {str(visible)} ------ {time.ctime()}')
        self.ui.plainTextEdit.appendPlainText(f'Доступно окно: {str(enabled)} ------ {time.ctime()}')

    # events

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        pos_old = event.oldPos().toTuple()
        pos_new = event.pos().toTuple()
        print(f'Старая позиция: {pos_old}, новая позиция: {pos_new} ------ {time.ctime()}')

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        new_size = event.size()
        print(f'Новый размер окна: {new_size.width()} x {new_size.height()} ------ {time.ctime()}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
