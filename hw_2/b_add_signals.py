import random

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация интерфейса
        :return: None
        """

        # comboBox -----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Элемент 1")
        self.comboBox.addItem("Элемент 2")
        self.comboBox.addItems(["Элемент 3", "Элемент 4", "Элемент 5"])
        self.comboBox.insertItem(0, "")

        self.pushButtonComboBox = QtWidgets.QPushButton("Получить данные")

        layoutComboBox = QtWidgets.QHBoxLayout()
        layoutComboBox.addWidget(self.comboBox)
        layoutComboBox.addWidget(self.pushButtonComboBox)

        # lineEdit -----------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите текст")

        self.pushButtonLineEdit = QtWidgets.QPushButton("Получить данные")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEdit)
        layoutLineEdit.addWidget(self.pushButtonLineEdit)

        # textEdit -----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setPlaceholderText("Введите текст")

        self.pushButtonTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutTextEdit = QtWidgets.QHBoxLayout()
        layoutTextEdit.addWidget(self.textEdit)
        layoutTextEdit.addWidget(self.pushButtonTextEdit)

        # plainTextEdit ------------------------------------------------------
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText("Введите текст")

        self.pushButtonPlainTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutPlainTextEdit = QtWidgets.QHBoxLayout()
        layoutPlainTextEdit.addWidget(self.plainTextEdit)
        layoutPlainTextEdit.addWidget(self.pushButtonPlainTextEdit)

        # spinBox ------------------------------------------------------------
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(random.randint(-50, 50))

        self.pushButtonSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutSpinBox = QtWidgets.QHBoxLayout()
        layoutSpinBox.addWidget(self.spinBox)
        layoutSpinBox.addWidget(self.pushButtonSpinBox)

        # doubleSpinBox ------------------------------------------------------
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setValue(random.randint(-50, 50))

        self.pushButtonDoubleSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutDoubleSpinBox = QtWidgets.QHBoxLayout()
        layoutDoubleSpinBox.addWidget(self.doubleSpinBox)
        layoutDoubleSpinBox.addWidget(self.pushButtonDoubleSpinBox)

        # timeEdit -----------------------------------------------------------
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime().addSecs(random.randint(-10000, 10000)))

        self.pushButtonTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutTimeEdit = QtWidgets.QHBoxLayout()
        layoutTimeEdit.addWidget(self.timeEdit)
        layoutTimeEdit.addWidget(self.pushButtonTimeEdit)

        # dateTimeEdit -------------------------------------------------------
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addDays(random.randint(-10, 10)))

        self.pushButtonDateTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutDateTimeEdit = QtWidgets.QHBoxLayout()
        layoutDateTimeEdit.addWidget(self.dateTimeEdit)
        layoutDateTimeEdit.addWidget(self.pushButtonDateTimeEdit)

        # plainTextEditLog ---------------------------------------------------
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        self.pushButtonClearLog = QtWidgets.QPushButton("Очистить лог")

        layoutLog = QtWidgets.QHBoxLayout()
        layoutLog.addWidget(self.plainTextEditLog)
        layoutLog.addWidget(self.pushButtonClearLog)

        # main layout

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutComboBox)
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutTextEdit)
        layoutMain.addLayout(layoutPlainTextEdit)
        layoutMain.addLayout(layoutSpinBox)
        layoutMain.addLayout(layoutDoubleSpinBox)
        layoutMain.addLayout(layoutTimeEdit)
        layoutMain.addLayout(layoutDateTimeEdit)
        layoutMain.addLayout(layoutLog)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonComboBox.clicked.connect(self.onPbComboBoxClicked)
        self.pushButtonLineEdit.clicked.connect(self.onPbLineEditClicked)
        self.pushButtonTextEdit.clicked.connect(self.onPbTextEditClicked)
        self.pushButtonPlainTextEdit.clicked.connect(self.onPbPlainTextEditClicked)
        self.pushButtonSpinBox.clicked.connect(self.onPbSpinBoxClicked)
        self.pushButtonDoubleSpinBox.clicked.connect(self.onPbDoubleSpinBoxClicked)
        self.pushButtonTimeEdit.clicked.connect(self.onPbTimeEditClicked)
        self.pushButtonDateTimeEdit.clicked.connect(self.onPbDateTimeEditClicked)
        self.pushButtonClearLog.clicked.connect(self.onPbClearLog)

        self.comboBox.currentTextChanged.connect(self.comboBoxTextChanged)
        self.spinBox.textChanged.connect(self.spinBoxTextChanged)
        self.dateTimeEdit.dateTimeChanged.connect(self.dateTimeEditTextChanged)

    # slots clicked --------------------------------------------------------------

    def onPbComboBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonComboBox
        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.comboBox.currentText())

    def onPbLineEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.lineEdit.text())

    def onPbTextEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonTextEdit

        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.textEdit.toPlainText())

    def onPbPlainTextEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonPlainTextEdit

        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.plainTextEdit.toPlainText())

    def onPbSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonSpinBox
        :return:
        """
        self.plainTextEditLog.appendPlainText(self.spinBox.text())

    def onPbDoubleSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonDoubleSpinBox
        :return:
        """
        self.plainTextEditLog.appendPlainText(self.doubleSpinBox.text())

    def onPbTimeEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonTimeEdit
        :return:
        """
        self.plainTextEditLog.appendPlainText(self.timeEdit.text())

    def onPbDateTimeEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonDateTimeEdit
        :return:
        """
        self.plainTextEditLog.appendPlainText(self.dateTimeEdit.text())

    def onPbClearLog(self) -> None:
        """
        Обработка сигнала при нажатии кнопки "Очистить лог"
        :return:
        """
        self.plainTextEditLog.clear()

    # slots changed --------------------------------------------------------

    def comboBoxTextChanged(self) -> None:
        """
        Обработка сигнала при изменении элемента в comboBox
        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.comboBox.currentText())

    def spinBoxTextChanged(self) -> None:
        """
        Обработка сигнала при изменении значения в spinBox
        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.spinBox.text())

    def dateTimeEditTextChanged(self) -> None:
        """
        Обработка сигнала при изменении знечения в dateTimeEdit
        :return: None
        """
        self.plainTextEditLog.appendPlainText(self.dateTimeEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
