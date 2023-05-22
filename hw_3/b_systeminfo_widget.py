"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets, QtGui
from hw_3.a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(None)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация UI
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

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutDelay)
        layoutMain.addLayout(layoutCPUInfo)
        layoutMain.addLayout(layoutRAMInfo)

        self.setLayout(layoutMain)

    # threads
    def initThreads(self) -> None:
        """
        Инициализация потоков
        :return: None
        """
        self.thread = SystemInfo()
        self.thread.start()

    # signals
    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.thread.systemInfoReceived.connect(self.printSystemInfo)
        self.lineEditDelay.textChanged.connect(self.delayChange)

    # slots
    def delayChange(self):
        """
        Слот получающий изменение значения задержки в self.lineEditDelay и совершающий изменение задержки "на горячую"
        :return: None
        """
        delay = int(self.lineEditDelay.text())
        self.thread.delay = delay

    def printSystemInfo(self, systemInfoReceived):
        """
        Слот перехватывающий поток, принимащий сигнал systemInfoReceived и устанавливающий данные сигнала в
        self.textEditCPUInfo и self.textEditRAMInfo

        :param systemInfoReceived:
        :return: None
        """
        self.textEditCPUInfo.setPlainText(str(systemInfoReceived[0]))
        self.textEditRAMInfo.setPlainText(str(systemInfoReceived[1]))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Слот уничтожения потока в момент закрытия окна приложения
        :param event: собитие нажатия на кнопку закрытия окна
        :return: закрытие потока
        """
        return self.thread.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWindow()
    window.show()

    app.exec()





