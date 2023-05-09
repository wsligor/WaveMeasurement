from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QToolBar
from PySide6.QtCore import Slot, Qt
from PySide6 import QtGui

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from MainMenu import MainMenu
from ToolBar import ToolBar
from NameExp import NameExp

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 1000)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        tool_bar = ToolBar(parent=self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        self.ne = NameExp(parent=self)
        self.ne.setGeometry(0, 25, 800, 600)

        self.graph =MPLGraph()

        self.btnOk = QPushButton('Ок', parent=self)
        self.btnCancel = QPushButton('Отмена', parent=self)

        self.centralWidget()

        layV = QVBoxLayout(self)

        layHTableGraph = QHBoxLayout()
        layHTableGraph.addWidget(self.ne)
        layHTableGraph.addWidget(self.graph)

        layV.addLayout(layHTableGraph)

        layH = QHBoxLayout()
        layH.addWidget(self.btnOk)
        layH.addWidget(self.btnCancel)

        layV.addLayout(layH)

        container = QWidget()
        container.setLayout(layV)

        self.setCentralWidget(container)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)
        main_menu.addNameExp.triggered.connect(self.ne.addNameExp)
        main_menu.updateNameExp.triggered.connect(self.ne.updateNameExp)
        main_menu.deleteNameExp.triggered.connect(self.ne.deleteNameExp)
        tool_bar.tbAdd.triggered.connect(self.ne.addNameExp)
        tool_bar.tbEdit.triggered.connect(self.ne.updateNameExp)
        tool_bar.tbDelete.triggered.connect(self.ne.deleteNameExp)

    @Slot()
    def about_qt(self):
        QMessageBox.aboutQt(self,'')

    @Slot()
    def about(self):
        title = "Анализ измерений"
        text = "Анализ измерений спектофотометра"
        QMessageBox.about(self, title, text)

class MPLGraph(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = plt.figure(figsize=(2, 2), layout="tight")
        self.ax = None
        super().__init__(self.fig)
        self.style = "default"
        self.title = ""
        self.noise_scale = 0.1
        self.plot()

    def plot(self):
        with plt.style.context(self.style):
            if self.ax:
                self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(111)
            x = np.linspace(0, 1)
            noise = np.random.normal(0, self.noise_scale, size=(len(x),))
            y = x + noise
            self.ax.plot(x, y)
            self.ax.set_title(self.title)
            self.ax.set_xlabel("t")
            self.ax.set_ylabel("signal")
            self.draw()
