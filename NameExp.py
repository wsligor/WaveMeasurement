from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTextEdit, QLineEdit, QComboBox, QDateEdit, QDialog
from PySide6.QtWidgets import QTableView, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton, QLabel

from PySide6.QtSql import QSqlQueryModel


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.refrechNameExp()

    def refrechNameExp(self):
        sql = '''
            SELECT date, number, name, substance, count, temperature, cuvette FROM nameExp
        '''
        self.setQuery(sql)

class NameExp(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @Slot()
    def addNameExp(self):
        # QMessageBox.information(self, 'NameExp', 'Add')
        dia = dlgAddExp()
        dia.exec()

    @Slot()
    def updateNameExp(self):
        QMessageBox.information(self, 'NameExp', 'Update')

    @Slot()
    def deleteNameExp(self):
        QMessageBox.information(self, 'NameExp', 'Delete')

class dlgAddExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        lblDate  = QLabel('Дата', parent=self)
        self.__deDate = QDateEdit(parent=self)

        lblNumber = QLabel('Номер', parent=self)
        self.__edNumber = QLineEdit(parent=self)

        lblCategory = QLabel('Категория:', parent=self)
        self.__cbCategory = QComboBox(parent=self)

        lblGroup = QLabel('Группа:', parent=self)
        self.__cbGroup = QComboBox(parent=self)

        lblName = QLabel('Наименование:', parent=self)
        self.__edName = QLineEdit(parent=self)

        lblSubstance = QLabel('Образец:', parent=self)
        self.__edSubstance = QLineEdit(parent=self)

        lblCount = QLabel('% содержания', parent=self)
        self.__edCount = QLineEdit(parent=self)

        lblTemp = QLabel('Температура:', parent=self)
        self.__edTemp = QLineEdit(parent=self)

        lblCuvvete = QLabel('Кювета', parent=self)
        self.edCuvvete = QLineEdit(parent=self)

        lblDescription = QLabel('Описание:', parent=self)
        self.__teDescriptin = QTextEdit(parent=self)

        btnAddCategory = QToolButton(parent=self)
        btnAddGroup = QToolButton(parent=self)

        btnOk = QPushButton('Ok',parent=self)
        btnCancel = QPushButton('Отмена', parent=self)
        btnFileOpen = QPushButton('Файл', parent=self)

        layV = QVBoxLayout(self)

        layHCategory = QHBoxLayout()
        layHCategory.addWidget(self.__cbCategory)
        layHCategory.addWidget(btnAddCategory)

        layHCroup = QHBoxLayout()
        layHCroup.addWidget(self.__cbGroup)
        layHCroup.addWidget(btnAddGroup)

        layV.addWidget(lblDate)
        layV.addWidget(self.__deDate)
        layV.addWidget(lblNumber)
        layV.addWidget(self.__edNumber)
        layV.addWidget(lblCategory)
        layV.addLayout(layHCategory)
        layV.addWidget(lblGroup)
        layV.addLayout(layHCroup)
        layV.addWidget(lblName)
        layV.addWidget(self.__edName)
        layV.addWidget(lblSubstance)
        layV.addWidget(self.__edSubstance)
        layV.addWidget(lblCount)
        layV.addWidget(self.__edCount)
        layV.addWidget(lblTemp)
        layV.addWidget(self.__edTemp)
        layV.addWidget(lblCuvvete)
        layV.addWidget(self.edCuvvete)
        layV.addWidget(lblDescription)
        layV.addWidget(self.__teDescriptin)

        layH = QHBoxLayout()
        layH.addWidget(btnOk)
        layH.addWidget(btnCancel)
        layH.addWidget(btnFileOpen)


        layV.addLayout(layH)

        btnCancel.clicked.connect(self.reject)

    @property
    def number(self):
        result: str = self.__edNumber.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def dateExp(self):
        result: str = self.__deDate.text().strip()
        if not result:
            return None
        else:
            return result
