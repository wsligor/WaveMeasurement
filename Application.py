from PySide6 import QtSql
from PySide6.QtWidgets import QApplication

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.DataBase = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.DataBase.setDatabaseName('SFM.db')
        if not self.DataBase.open():
            print('no')