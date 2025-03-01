from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Основной вертикальный layout для всех элементов
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Группируем элементы в горизонтальные layout для удобства
        self.gridLayout = QtWidgets.QGridLayout()

        # Лейблы и элементы для ввода
        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setText("A (левая граница):")
        self.gridLayout.addWidget(self.labelA, 0, 0)

        self.AEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.AEdit, 0, 1)

        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setText("B (правая граница):")
        self.gridLayout.addWidget(self.labelB, 1, 0)

        self.BEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.BEdit, 1, 1)

        self.labelD = QtWidgets.QLabel(self.centralwidget)
        self.labelD.setText("D (плюс к отображению):")
        self.gridLayout.addWidget(self.labelD, 2, 0)

        self.DEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.DEdit, 2, 1)

        self.labelMutStrange = QtWidgets.QLabel(self.centralwidget)
        self.labelMutStrange.setText("Интенсивность мутации:")
        self.gridLayout.addWidget(self.labelMutStrange, 3, 0)

        self.MutStrange = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.MutStrange, 3, 1)

        self.labelMutChast = QtWidgets.QLabel(self.centralwidget)
        self.labelMutChast.setText("Частота мутации:")
        self.gridLayout.addWidget(self.labelMutChast, 4, 0)

        self.MutChast = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.MutChast, 4, 1)

        self.labelCountPop = QtWidgets.QLabel(self.centralwidget)
        self.labelCountPop.setText("Кол-во популяций:")
        self.gridLayout.addWidget(self.labelCountPop, 5, 0)

        self.CountPopSB = QtWidgets.QSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.CountPopSB, 5, 1)
        self.CountPopSB.setValue(10)

        self.labelCountOs = QtWidgets.QLabel(self.centralwidget)
        self.labelCountOs.setText("Количество особей:")
        self.gridLayout.addWidget(self.labelCountOs, 6, 0)

        self.CountOsSB = QtWidgets.QSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.CountOsSB, 6, 1)
        self.CountOsSB.setValue(10)

        self.labelType = QtWidgets.QLabel(self.centralwidget)
        self.labelType.setText("Тип оптимума:")
        self.gridLayout.addWidget(self.labelType, 7, 0)

        self.TypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.TypeBox.addItem("максимум")
        self.TypeBox.addItem("минимум")
        self.gridLayout.addWidget(self.TypeBox, 7, 1)

        # Добавляем ComboBox для выбора функции
        self.labelFun = QtWidgets.QLabel(self.centralwidget)
        self.labelFun.setText("Выбор функции:")
        self.gridLayout.addWidget(self.labelFun, 8, 0)

        self.FunCombo = QtWidgets.QComboBox(self.centralwidget)
        self.FunCombo.addItem("cos(x) − x/3")
        self.FunCombo.addItem("4 * sin(x) + x/4")
        self.FunCombo.addItem("3 * cos(x) + x/3")
        self.gridLayout.addWidget(self.FunCombo, 8, 1)

        # Добавляем кнопки
        self.StartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartBtn.setText("Старт")
        self.gridLayout.addWidget(self.StartBtn, 9, 0)

        self.StopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StopBtn.setText("Стоп")
        self.StopBtn.setVisible(False)
        self.gridLayout.addWidget(self.StopBtn, 9, 1)

        # Слайдер
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.gridLayout.addWidget(self.Slider, 10, 0, 1, 2)

        # Место для отображения графика
        self.Graph = QtWidgets.QLabel(self.centralwidget)
        self.graphLayout = QtWidgets.QHBoxLayout()
        self.graphLayout.addWidget(self.Graph)

        # Собираем layout
        self.mainLayout.addLayout(self.gridLayout)
        self.mainLayout.addLayout(self.graphLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генетический Алгоритм"))