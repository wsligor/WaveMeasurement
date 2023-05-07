from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QToolBar
from PySide6.QtCore import Slot, Qt
from PySide6 import QtGui
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

        self.btnOk = QPushButton('Ок', parent=self)
        self.btnCancel = QPushButton('Отмена', parent=self)

        self.centralWidget()

        layV = QVBoxLayout(self)

        layV.addWidget(self.ne)

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
        tool_bar.tbUpdate.triggered.connect(self.ne.updateNameExp)
        tool_bar.tbDelete.triggered.connect(self.ne.deleteNameExp)

    @Slot()
    def about_qt(self):
        QMessageBox.aboutQt(self,'')

    @Slot()
    def about(self):
        title = "Анализ измерений"
        text = "Анализ измерений спектофотометра"
        QMessageBox.about(self, title, text)

