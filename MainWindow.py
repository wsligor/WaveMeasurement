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
from NameExp import MPLGraph

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1700, 600)

        self.lset = []

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        tool_bar = ToolBar(parent=self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        self.ne = NameExp(parent=self)
        self.ne.setMinimumWidth(350)
        self.ne.setMaximumWidth(350)

        self.graph =MPLGraph()
        self.graph.resize(1000, 400)

        btnOk = QPushButton('Ок', parent=self)
        btnCancel = QPushButton('Отмена', parent=self)

        btnCorrelationCalc = QPushButton('Корреляция', parent=self)
        btnCorrelationCalc.setMaximumWidth(100)

        layVButtonCalk = QVBoxLayout()

        layVButtonCalk.addWidget(btnCorrelationCalc)
        layVButtonCalk.setAlignment(Qt.AlignmentFlag.AlignTop)

        layV = QVBoxLayout(self)

        layHTableGraph = QHBoxLayout()
        layHTableGraph.addWidget(self.ne)
        layHTableGraph.addLayout(layVButtonCalk)
        layHTableGraph.addWidget(self.graph)

        layV.addLayout(layHTableGraph)

        layH = QHBoxLayout()
        layH.addWidget(btnOk)
        layH.addWidget(btnCancel)

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
        self.ne.clicked.connect(self.tvNameExp_clickedMM)
        btnCorrelationCalc.clicked.connect(self.btnCorrelationCalc_clicked)

    def btnCorrelationCalc_clicked(self):
        if len(self.lset) < 2:
            print('Выберите более 1 строки')
            return

        A = np.array([])
        con = sl.connect('SFM.db')
        cur = con.cursor()
        for id_x in self.lset:
            sql = '''SELECT transparency FROM dataExp WHERE id_nameExp = {} and waveLength > 300'''.format(id_x)
            cur.execute(sql)
            data = cur.fetchall()
            # for k in data:
            #     z = A.append(data[0])
        print(z)


    @Slot()
    def about_qt(self):
        QMessageBox.aboutQt(self,'')

    @Slot()
    def about(self):
        title = "Анализ измерений"
        text = "Анализ измерений спектофотометра"
        QMessageBox.about(self, title, text)

    def drawLineChartMultiMM(self, lset):
        self.graph.plot(lset)

    def tvNameExp_clickedMM(self):
        self.lset = self.ne.tvNameExp_clicked()
        self.drawLineChartMultiMM(self.lset)
