"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets, QtGui
from hw_3.a_threads import WeatherHandler, SystemInfo
from hw_3.b_systeminfo_widget import SystemInfoWindow
from hw_3.c_weatherapi_widget import WeatherInfoWindow


class CommonInfoWindow(QtWidgets.QWidget):
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
        labelDelay = QtWidgets.QLabel()
        labelDelay.setText("Введите время задержки:")
        labelCPUInfo = QtWidgets.QLabel()
        labelCPUInfo.setText("Информация о загрузке CPU:")
        labelRAMInfo = QtWidgets.QLabel()
        labelRAMInfo.setText("Информация о загрузке RAM:")

        self.lineEditDelay = QtWidgets.QLineEdit()

        self.textEditCPUInfo = QtWidgets.QPlainTextEdit()
        self.textEditRAMInfo = QtWidgets.QPlainTextEdit()

        layoutDelay = QtWidgets.QHBoxLayout()
        layoutDelay.addWidget(labelDelay)
        layoutDelay.addWidget(self.lineEditDelay)

        layoutCPUInfo = QtWidgets.QVBoxLayout()
        layoutCPUInfo.addWidget(labelCPUInfo)
        layoutCPUInfo.addWidget(self.textEditCPUInfo)

        layoutRAMInfo = QtWidgets.QVBoxLayout()
        layoutRAMInfo.addWidget(labelRAMInfo)
        layoutRAMInfo.addWidget(self.textEditRAMInfo)

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
        layoutMain.addLayout(layoutCPUInfo)
        layoutMain.addLayout(layoutRAMInfo)
        layoutMain.addLayout(layoutCoord)
        layoutMain.addLayout(layoutDelay)
        layoutMain.addLayout(layoutWeatherInfo)
        layoutMain.addLayout(laoutButtons)

        self.setLayout(layoutMain)

    def initThreads(self) -> None:
        """
        Инициализация потоков
        :return: None
        """
        self.thread_1 = SystemInfo()
        self.thread_1.start()

    # signals
    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.thread_1.systemInfoReceived.connect(self.printSystemInfo)
        self.lineEditDelay.textChanged.connect(self.delayChange)

        self.pButtonStart.clicked.connect(self.onPButtonStart)
        self.pButtonStop.clicked.connect(self.onPButtonStop)

    # slots
    def delayChange(self):
        """
        Слот получающий изменение значения задержки в self.lineEditDelay и совершающий изменение задержки "на горячую"
        :return: None
        """
        delay = int(self.lineEditDelay.text())
        self.thread_1.delay = delay

    def printSystemInfo(self, systemInfoReceived):
        """
        Слот перехватывающий поток, принимащий сигнал systemInfoReceived и устанавливающий данные сигнала в
        self.textEditCPUInfo и self.textEditRAMInfo

        :param systemInfoReceived:
        :return: None
        """
        self.textEditCPUInfo.setPlainText(str(systemInfoReceived[0]))
        self.textEditRAMInfo.setPlainText(str(systemInfoReceived[1]))

    def onPButtonStart(self) -> None:
        """
        Слот нажатия на кнопку Старт, инициализирует поток с установленными данными
        :return: None
        """
        lat = int(self.lineEditLatitude.text())
        lon = int(self.lineEditLongitude.text())

        self.thread_2 = WeatherHandler(lat, lon)
        self.thread_2.received.connect(self.printWeatherInfo)

        if self.lineEditDelay.text() != '':
            delay_ = int(self.lineEditDelay.text())
            self.thread_2.delay = delay_

        self.thread_2.start()

        self.lineEditLatitude.setReadOnly(True)
        self.lineEditLongitude.setReadOnly(True)
        self.lineEditDelay.setReadOnly(True)

    def onPButtonStop(self) -> None:
        """
        Слот нажатия на кропку Стоп, который "убивает" поток
        :return: None
        """
        self.thread_2.terminate()

    def printWeatherInfo(self, received) -> None:
        """
        Слот вывода в textEditWeatherInfo информации перехваченного сигнала потока
        :param received: перехваченный сигнал потока
        :return: None
        """
        self.textEditWeatherInfo.append(f'Температура: {received["temperature"]}\nскорость ветра: {received["windspeed"]}\nнаправление ветра: {received["weathercode"]}\nдата: {received["time"]}')
        self.textEditWeatherInfo.append(" ")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Слот уничтожения потока в момент закрытия окна приложения
        :param event: собитие нажатия на кнопку закрытия окна
        :return: закрытие потока
        """
        self.thread_1.terminate()
        self.thread_2.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = CommonInfoWindow()
    window.show()

    app.exec()
