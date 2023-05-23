from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLabel, QComboBox, QMessageBox, QVBoxLayout
from PySide6.QtCore import Slot, Qt

import numpy as np
import sqlite3 as sl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from MainMenu import MainMenu
from ToolBar import ToolBar
from NameExp import NameExp
from MPLGraph import MPLGraph
from NameExp import dlgAddExp


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1700, 900)

        self.countSelectTableRows = []
        self.arrayMeanSave = []

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        tool_bar = ToolBar(parent=self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        self.tableViewNameExp = NameExp(parent=self)
        self.tableViewNameExp.setMinimumWidth(350)
        self.tableViewNameExp.setMaximumWidth(350)

        self.cbSelCategory = QComboBox()
        self.cbSelGroup = QComboBox()

        layHComboBox = QHBoxLayout()
        layHComboBox.addWidget(self.cbSelCategory)
        layHComboBox.addWidget(self.cbSelGroup)

        layVComboBoxTableNameExp = QVBoxLayout()
        layVComboBoxTableNameExp.addLayout(layHComboBox)
        layVComboBoxTableNameExp.addWidget(self.tableViewNameExp)


        self.plotGraph = MPLGraph()
        tbar = NavigationToolbar(self.plotGraph, self)

        btnOk = QPushButton('Ок', parent=self)
        btnCancel = QPushButton('Отмена', parent=self)

        btnCorrelationCalc = QPushButton('Корреляция', parent=self)
        btnCorrelationCalc.setMaximumWidth(120)

        self.lblCorrel = QLabel('Cor = : ', parent=self)

        btnMeanCalc = QPushButton('Показать\n среднею линию', parent=self)
        btnMeanCalc.setMaximumWidth(120)

        btnMeanCalcSave = QPushButton('Записать\n среднею линию', parent=self)
        btnMeanCalcSave.setMaximumWidth(120)

        btnMinCalc = QPushButton('Показать\n линию минимума', parent=self)
        btnMinCalc.setMaximumWidth(120)

        btnMinCalcSave = QPushButton('Сохранить\n линию минимума', parent=self)
        btnMinCalcSave.setMaximumWidth(120)

        btnMaxCalc = QPushButton('Показать\n линию максимума', parent=self)
        btnMaxCalc.setMaximumWidth(120)

        btnMaxCalcSave = QPushButton('Сохранить\n линию максимума', parent=self)
        btnMaxCalcSave.setMaximumWidth(120)

        layVButtonCalk = QVBoxLayout()

        layVButtonCalk.addWidget(btnCorrelationCalc)
        layVButtonCalk.addWidget(self.lblCorrel)
        layVButtonCalk.addWidget(btnMeanCalc)
        layVButtonCalk.addWidget(btnMeanCalcSave)
        layVButtonCalk.addWidget(btnMinCalc)
        layVButtonCalk.addWidget(btnMinCalcSave)
        layVButtonCalk.addWidget(btnMaxCalc)
        layVButtonCalk.addWidget(btnMaxCalcSave)
        layVButtonCalk.setAlignment(Qt.AlignmentFlag.AlignTop)

        layHButtonGraph = QHBoxLayout()

        btnTwoGraph = QPushButton('Два окна', parent=self)

        layHButtonGraph.addWidget(btnTwoGraph)
        layHButtonGraph.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layVGraphButtonCalk = QVBoxLayout()
        # layVGraphButtonCalk.addWidget(self.graph)
        layVGraphButtonCalk.addWidget(tbar)
        layVGraphButtonCalk.addWidget(self.plotGraph)
        layVGraphButtonCalk.addLayout(layHButtonGraph)

        layV = QVBoxLayout(self)

        layHTableGraph = QHBoxLayout()
        layHTableGraph.addLayout(layVComboBoxTableNameExp)
        layHTableGraph.addLayout(layVButtonCalk)
        layHTableGraph.addLayout(layVGraphButtonCalk)

        layV.addLayout(layHTableGraph)

        layHBottom = QHBoxLayout()
        layHBottom.addWidget(btnOk)
        layHBottom.addWidget(btnCancel)
        layHBottom.setAlignment(Qt.AlignmentFlag.AlignRight)

        layV.addLayout(layHBottom)

        container = QWidget()
        container.setLayout(layV)

        self.centralWidget()
        self.setCentralWidget(container)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)
        main_menu.addNameExp.triggered.connect(self.tableViewNameExp.addNameExp)
        main_menu.updateNameExp.triggered.connect(self.tableViewNameExp.updateNameExp)
        main_menu.deleteNameExp.triggered.connect(self.tableViewNameExp.deleteNameExp)
        tool_bar.tbAdd.triggered.connect(self.tableViewNameExp.addNameExp)
        tool_bar.tbEdit.triggered.connect(self.tableViewNameExp.updateNameExp)
        tool_bar.tbDelete.triggered.connect(self.tableViewNameExp.deleteNameExp)
        self.tableViewNameExp.clicked.connect(self.tvNameExp_clickedMM)
        btnCorrelationCalc.clicked.connect(self.btnCorrelationCalc_clicked)
        btnMeanCalc.clicked.connect(self.btnMeanCalc_clicked)
        btnMeanCalcSave.clicked.connect(self.btnMeanCalcSave_clicked)
        btnMinCalc.clicked.connect(self.btnMinCalc_clicked)
        btnMinCalcSave.clicked.connect(self.btnMinCalcSave_clicked)
        btnMaxCalc.clicked.connect(self.btnMaxCalc_clicked)
        btnMaxCalcSave.clicked.connect(self.btnMaxCalcSave_clicked)
        btnTwoGraph.clicked.connect(self.btnTwoGraph_clicked)

    def btnTwoGraph_clicked(self):
        pass

    def btnMaxCalcSave_clicked(self):
        pass

    def btnMaxCalc_clicked(self):
        if len(self.countSelectTableRows) < 2:
            QMessageBox.information(self, 'График', 'Выделите 2 строки и более')
            return
        # Заполняем массив 0
        array_result = [0] * 700
        con = sl.connect('SFM.db')
        cur = con.cursor()
        for id_sel in self.tableViewNameExp.idSelectTableNameExp:
            sql_text = f"""SELECT transparency 
                            FROM dataExp 
                            WHERE id_nameExp = {id_sel} and waveLength > 300"""
            cur.execute(sql_text)
            data = cur.fetchall()
            for p in range(len(array_result)):
                if data[p][0] > array_result[p]:
                    array_result[p] = data[p][0]
        con.close()
        self.plotGraph.plot_meam(self.tableViewNameExp.idSelectTableNameExp, array_result)

    def btnMinCalcSave_clicked(self):
        pass

    def btnMinCalc_clicked(self):
        if len(self.countSelectTableRows) < 2:
            QMessageBox.information(self, 'График', 'Выделите 2 строки и более')
            return
        # Заполняем массив 0
        array_result = [1000] * 700
        con = sl.connect('SFM.db')
        cur = con.cursor()
        for id_sel in self.tableViewNameExp.idSelectTableNameExp:
            sql_text = f"""SELECT transparency 
                            FROM dataExp 
                            WHERE id_nameExp = {id_sel} and waveLength > 300"""
            cur.execute(sql_text)
            data = cur.fetchall()
            for p in range(len(array_result)):
                if data[p][0] < array_result[p]:
                    array_result[p] = data[p][0]
        con.close()
        self.plotGraph.plot_meam(self.tableViewNameExp.idSelectTableNameExp, array_result)

    # TODO Обеспечить разный вход для загрузки файла и сохранения расчётных данных
    def btnMeanCalcSave_clicked(self):
        dlgAddExp.filename = 'R'
        self.tableViewNameExp.addNameExpCalcSave(self.arrayMeanSave)
        pass

    def btnMeanCalc_clicked(self):
        if len(self.countSelectTableRows) < 2:
            print('Выберите более 1 строки')
            return
        a = []
        a_result = []
        for i in range(700):
            a_result.append(0)
        con = sl.connect('SFM.db')
        cur = con.cursor()
        for id in self.tableViewNameExp.idSelectTableNameExp:
            sql = '''SELECT transparency FROM dataExp WHERE id_nameExp = {} and waveLength > 300'''.format(id)
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                a.append(i[0])
            lenA = len(a)
            for i in range(lenA):
                a_result[i] = a_result[i] + a[i]
            a.clear()
        r = len(self.tableViewNameExp.idSelectTableNameExp)
        for i in range(700):
            a_result[i] = round(a_result[i] / r, 1)
        self.plotGraph.plot_meam(self.tableViewNameExp.idSelectTableNameExp, a_result)
        self.arrayMeanSave = a_result

    def btnCorrelationCalc_clicked(self):
        if len(self.countSelectTableRows) < 2:
            print('Выберите более 1 строки')
            return

        con = sl.connect('SFM.db')
        cur = con.cursor()
        sql = f'''SELECT transparency FROM dataExp WHERE id_nameExp = {self.countSelectTableRows[0]} and waveLength > 300'''
        cur.execute(sql)
        data1 = cur.fetchall()
        data1 = [p[0] for p in data1]
        sql = f'''SELECT transparency FROM dataExp WHERE id_nameExp = {self.countSelectTableRows[1]} and waveLength > 300'''
        cur.execute(sql)
        data2 = cur.fetchall()
        data2 = [p[0] for p in data2]
        con.close()
        self.lblCorrel.setText('')
        corrcoef_array = np.corrcoef(data1, data2)
        corrcoef = round(corrcoef_array[0][1], 5)
        self.lblCorrel.setText(f'Cor = :  {str(corrcoef)}')

    @Slot()
    def about_qt(self):
        QMessageBox.aboutQt(self, '')

    @Slot()
    def about(self):
        title = "Анализ измерений"
        text = "Анализ измерений спектрофотометра"
        QMessageBox.about(self, title, text)

    def drawLineChartMultiMM(self, lset):
        self.plotGraph.plot(self.countSelectTableRows)

    def tvNameExp_clickedMM(self):
        self.countSelectTableRows = self.tableViewNameExp.idSelectTableNameExp
        self.drawLineChartMultiMM(self.countSelectTableRows)
