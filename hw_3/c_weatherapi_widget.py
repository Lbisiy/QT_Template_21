"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

from PySide6 import QtWidgets, QtGui
from hw_3.a_threads import WeatherHandler


class WeatherInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация окна вывода информации о погоде
        :return: None
        """
        labelLatitude = QtWidgets.QLabel()
        labelLatitude.setText("Введите широту:")
        labelLongitude = QtWidgets.QLabel()
        labelLongitude.setText("Введите долготу:")
        labelDelay = QtWidgets.QLabel()
        labelDelay.setText("Введите время задержки:")
        labelWeatherInfo = QtWidgets.QLabel()
        labelWeatherInfo.setText("Информация о погоде:")

        self.lineEditLatitude = QtWidgets.QLineEdit()
        self.lineEditLongitude = QtWidgets.QLineEdit()
        self.lineEditDelay = QtWidgets.QLineEdit()

        self.textEditWeatherInfo = QtWidgets.QTextEdit()

        self.pButtonStart = QtWidgets.QPushButton("Старт")
        self.pButtonStop = QtWidgets.QPushButton("Стоп")

        layoutCoord = QtWidgets.QHBoxLayout()
        layoutCoord.addWidget(labelLatitude)
        layoutCoord.addWidget(self.lineEditLatitude)
        layoutCoord.addWidget(labelLongitude)
        layoutCoord.addWidget(self.lineEditLongitude)

        layoutDelay = QtWidgets.QHBoxLayout()
        layoutDelay.addWidget(labelDelay)
        layoutDelay.addWidget(self.lineEditDelay)

        layoutWeatherInfo = QtWidgets.QVBoxLayout()
        layoutWeatherInfo.addWidget(labelWeatherInfo)
        layoutWeatherInfo.addWidget(self.textEditWeatherInfo)

        laoutButtons = QtWidgets.QHBoxLayout()
        laoutButtons.addWidget(self.pButtonStart)
        laoutButtons.addWidget(self.pButtonStop)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutCoord)
        layoutMain.addLayout(layoutDelay)
        layoutMain.addLayout(layoutWeatherInfo)
        layoutMain.addLayout(laoutButtons)

        self.setLayout(layoutMain)

    # thread

    def initThreads(self, lat=0, lon=0) -> None:
        """
        Инициализация потоков
        :return: None
        """
        self.thread = WeatherHandler(lat, lon)

    def initSignals(self) -> None:
        """
        Инициализация сигналов виджетов
        :return: None
        """

        self.pButtonStart.clicked.connect(self.onPButtonStart)
        self.pButtonStop.clicked.connect(self.onPButtonStop)

    # slots
    def onPButtonStart(self) -> None:
        """
        Слот нажатия на кнопку Старт, инициализирует поток с установленными данными
        :return: None
        """
        lat = int(self.lineEditLatitude.text())
        lon = int(self.lineEditLongitude.text())

        self.initThreads(lat, lon)
        self.thread.received.connect(self.printWeatherInfo)

        if self.lineEditDelay.text() != '':
            delay_ = int(self.lineEditDelay.text())
            self.thread.delay = delay_

        self.thread.start()

        self.lineEditLatitude.setReadOnly(True)
        self.lineEditLongitude.setReadOnly(True)
        self.lineEditDelay.setReadOnly(True)

    def onPButtonStop(self) -> None:
        """
        Слот нажатия на кропку Стоп, который "убивает" поток
        :return: None
        """
        self.thread.terminate()

    def printWeatherInfo(self, received) -> None:
        """
        Слот вывода в textEditWeatherInfo информации перехваченного сигнала потока
        :param received: перехваченный сигнал потока
        :return: None
        """
        self.textEditWeatherInfo.append(f'{received}')

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Слот уничтожения потока в момент закрытия окна приложения
        :param event: собитие нажатия на кнопку закрытия окна
        :return: закрытие потока
        """
        return self.thread.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherInfoWindow()
    window.show()

    app.exec()

