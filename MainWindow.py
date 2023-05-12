from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QToolBar
from PySide6.QtCore import Slot, Qt
from PySide6 import QtGui

import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sl
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from MainMenu import MainMenu
from ToolBar import ToolBar
from NameExp import NameExp

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1700, 600)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        tool_bar = ToolBar(parent=self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        self.ne = NameExp(parent=self)
        self.ne.setMinimumWidth(350)
        self.ne.setMaximumWidth(350)

        self.graph =MPLGraph()
        self.graph.resize(1000, 400)

        self.btnOk = QPushButton('Ок', parent=self)
        self.btnCancel = QPushButton('Отмена', parent=self)

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

        self.centralWidget()
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
        self.fig = plt.figure(layout="tight") #figsize=(2, 2),
        self.ax = None
        super().__init__(self.fig)
        self.style = "default"
        self.title = "Wave measurement"
        self.plot()

    def plot(self):
        with plt.style.context(self.style):
            if self.ax:
                self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(1, 1, 1)
            self.ax.grid(color='gray', linewidth=0.5, linestyle='-')
            # self.ax.set_xlim(-5, 4)  # мин и мах координаты х
            self.ax.set_ylim(94, 107)  # мин и мах координаты y

            x = []
            y = []
            z = []
            con = sl.connect('SFM.db')
            cur = con.cursor()
            sql = '''SELECT waveLength FROM dataExp WHERE id_nameExp = 30 and waveLength > 300'''
            cur.execute(sql)
            rows = cur.fetchall()
            for i in rows:
                x.append(i[0])

            sql = '''SELECT transparency FROM dataExp WHERE id_nameExp = 30 and waveLength > 300'''
            cur.execute(sql)
            collumns = cur.fetchall()
            for i in collumns:
                y.append(i[0])

            sql = '''SELECT transparency FROM dataExp WHERE id_nameExp = 50 and waveLength > 300'''
            cur.execute(sql)
            collumns = cur.fetchall()
            for i in collumns:
                z.append(i[0])

            con.commit()

            self.ax.plot(x, y)
            self.ax.plot(x, z)
            self.ax.set_title(self.title)
            self.ax.set_xlabel("waveLength")
            self.ax.set_ylabel("transparency")
            self.draw()
