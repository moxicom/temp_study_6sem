import sys
import numpy as np
import sympy
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
from ui_mainwindow import Ui_MainWindow


class Agent:
    def __init__(self, x: float):
        self.X = x
        self.Y = None

    def mutate(self, strange: float, chast: float):
        if np.random.rand() <= chast:
            self.X += strange if np.random.rand() > 0.5 else -strange

    def calculate(self, fun):
        self.Y = fun(self.X)

    def __repr__(self):
        return f"Agent(X={self.X}, Y={self.Y})"

    def get_x(self) -> float:
        return self.X

    def get_y(self) -> float:
        return self.Y


class GeneticAlgorithmWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.StartBtn.clicked.connect(self.start)
        self.Slider.valueChanged.connect(self.slide)
        self.StopBtn.setVisible(False)
        self.count = 0

    def start(self):
        A = float(self.AEdit.text())
        B = float(self.BEdit.text())
        D = float(self.DEdit.text())
        tp = self.TypeBox.currentText()
        countpop = self.CountPopSB.value()
        strengMut = float(self.MutStrange.text())
        chastMut = float(self.MutChast.text())
        countos = self.CountOsSB.value()
        self.Slider.setMaximum(countpop - 1)
        self.agents = []
        x = sympy.Symbol('x')

        # Выбор функции в зависимости от выбранного элемента в выпадающем списке
        selected_function = self.FunCombo.currentText()
        if selected_function == 'cos(x) − x/3':
            fun = sympy.lambdify(x, sympy.cos(x) - x / 3)
        elif selected_function == '4 * sin(x) + x/4':
            fun = sympy.lambdify(x, 4 * sympy.sin(x) + x / 4)
        elif selected_function == '3 * cos(x) + x/3':
            fun = sympy.lambdify(x, 3 * sympy.cos(x) + x / 3)

        ar = np.array(self.gen_x(A, B))
        xx, y = self.get_y(fun, ar)

        # Инициализация агентов
        for i in range(countos):
            par = (B - A) * np.random.rand() + A
            self.agents.append(Agent(par))
            self.agents[-1].calculate(fun)

        # Генетический алгоритм
        for i in range(countpop):
            self.drawplot(xx, y)
            for k in range(int(countos / 2)):
                minim = 1000
                maxim = -1000
                index = 0
                ind = 0
                if tp == 'максимум':
                    for d in self.agents:
                        if d.get_y() < minim:
                            minim = d.get_y()
                            index = ind
                        ind += 1
                elif tp == 'минимум':
                    for d in self.agents:
                        if d.get_y() > maxim:
                            maxim = d.get_y()
                            index = ind
                        ind += 1
                self.drawpoint(self.agents[index].get_x(), self.agents[index].get_y(), 'r')
                del self.agents[index]
            for f in self.agents:
                self.drawpoint(f.get_x(), f.get_y(), 'g')
            self.saveplt(i)
            secund = 0
            for dl in range(int(countos / 2)):
                self.agents.append(Agent(self.agents[secund].get_x()))
                secund += 1
            for ag in range(len(self.agents)):
                self.agents[ag].mutate(strengMut, chastMut)
                self.agents[ag].calculate(fun)
        self.show_graph(0)

    def slide(self):
        self.show_graph(self.Slider.value())

    def show_graph(self, name):
        self.mypix = QPixmap(f"./tmp/{name}.jpg").scaled(640, 480)
        self.Graph.setPixmap(self.mypix)

    def gen_x(self, A, B):
        shag = 0.01
        ret = []
        while A < B:
            ret.append(A)
            A += shag
        return ret

    def get_y(self, fun, ar):
        ret = np.zeros(len(ar))
        for ind, i in enumerate(ar):
            ret[ind] = fun(i)
        return ar, ret

    def drawplot(self, xx, y):
        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        self.ax.plot(xx, y)

    def drawpoint(self, x, y, color):
        self.ax.scatter(x, y, c=color)

    def saveplt(self, name):
        plt.savefig(f'./tmp/{name}.jpg', dpi=50)
        plt.close()


app = QtWidgets.QApplication([])
application = GeneticAlgorithmWindow()
application.show()
sys.exit(app.exec())