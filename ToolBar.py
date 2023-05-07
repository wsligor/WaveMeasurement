from PySide6.QtWidgets import QToolBar
from PySide6 import QtGui

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        icon = QtGui.QIcon()
        self.__tbAdd = QtGui.QAction('+')
        self.addAction(self.tbAdd)
        self.__tbUpdate = QtGui.QAction('/')
        self.addAction(self.tbUpdate)
        self.__tbDelete = QtGui.QAction('-')
        self.addAction(self.tbDelete)

    @property
    def tbAdd(self):
        return self.__tbAdd

    @property
    def tbUpdate(self):
        return self.__tbUpdate

    @property
    def tbDelete(self):
        return self.__tbDelete