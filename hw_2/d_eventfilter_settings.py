"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtGui, QtCore
from hw_2.ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.count = 0

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация окна приложения
        :return: None
        """

        self.ui.comboBox.addItems(["dec", "oct", "hex", "bin"])

        self.ui.horizontalSlider.setRange(0, 100)
        # self.ui.dial.setRange(0, 100)

        settings = QtCore.QSettings("MyApplication")
        self.ui.comboBox.setCurrentText(settings.value("mode", " "))
        self.ui.lcdNumber.display(settings.value("value", 0))

    # signals

    def initSignals(self) -> None:
        """
        Инициализация сигналов всех виджетов окна приложения
        :return: None
        """
        self.ui.dial.sliderMoved.connect(self.ui.horizontalSlider.setValue)
        self.ui.horizontalSlider.sliderMoved.connect(self.ui.dial.setValue)

        self.ui.dial.sliderMoved.connect(self.visualisationLCD)
        self.ui.horizontalSlider.sliderMoved.connect(self.visualisationLCD)

        self.ui.comboBox.activated.connect(self.visualisationLCD)

    # slots

    def visualisationLCD(self):
        """
        Слот отображения значений при движении слайдеров
        :return:
        """
        mode = self.ui.comboBox.currentText()
        number = self.ui.horizontalSlider.value()

        if mode == "hex":
            self.ui.lcdNumber.setHexMode()
            self.ui.lcdNumber.display(number)
        if mode == "bin":
            self.ui.lcdNumber.setBinMode()
            self.ui.lcdNumber.display(number)
        if mode == "oct":
            self.ui.lcdNumber.setOctMode()
            self.ui.lcdNumber.display(number)
        if mode == "dec":
            self.ui.lcdNumber.setDecMode()
            self.ui.lcdNumber.display(number)

    # events

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие регулировки Dial с помощью + и - на клавиатуре и вывод значений в консоль
        :param event: None
        :return:
        """
        if event.text() == "+":
            print(event.text())
            self.count += 1
            self.ui.horizontalSlider.setSliderPosition(self.count)
            self.ui.dial.setSliderPosition(self.count)
            self.visualisationLCD()
            print(self.ui.lcdNumber.value())

        if event.text() == "-" and self.count >= 1:
            self.count -= 1
            self.ui.horizontalSlider.setSliderPosition(self.count)
            self.ui.dial.setSliderPosition(self.count)
            self.visualisationLCD()
            print(self.ui.lcdNumber.value())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие сохранения настроек comboBox и lcdNumber в Library/Preferences/com.myapplication
        :param event:
        :return: None
        """
        settings = QtCore.QSettings("MyApplication")

        settings.setValue("mode", self.ui.comboBox.currentText())
        settings.setValue("value", (self.ui.lcdNumber.value()))  # берет из value float и не получается сохранить разные форматы значений экрана


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
