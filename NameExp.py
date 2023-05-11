from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QTextEdit, QLineEdit, QComboBox, QDateEdit, QDialog, QHeaderView
from PySide6.QtWidgets import QTableView, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton, QLabel
from PySide6.QtSql import QSqlQueryModel

from Category import dlgCategories, Model as ModelCategories



class ModelCategories(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refrechCategories()

    def refrechCategories(self):
        sql = 'SELECT name FROM categories'
        self.setQuery(sql)

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.setHeaderData(0, Qt.Orientation.Horizontal, 'ID')
        self.setHeaderData(1, Qt.Orientation.Horizontal, 'Номер')

        self.refrechNameExp()

    def refrechNameExp(self):
        sql = 'SELECT id, name, date, number FROM nameExp'
        self.setQuery(sql)


class NameExp(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        self.hideColumn(0)

        hh: QTableView().horizontalHeader() = self.horizontalHeader()
        hh.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # hh.setSectionResizeMode(8, QHeaderView.ResizeMode.Stretch)

    @Slot()
    def addNameExp(self):
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

        lblDate = QLabel('Дата', parent=self)
        self.__deDate = QDateEdit(parent=self)

        lblNumber = QLabel('Номер', parent=self)
        self.__edNumber = QLineEdit(parent=self)

        lblCategory = QLabel('Категория:', parent=self)
        self.__cbCategory = QComboBox(parent=self)
        self.modelCategories = ModelCategories(parent=self)
        self.__cbCategory.setModel(self.modelCategories)

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

        lblCuvete = QLabel('Кювета', parent=self)
        self.__edCuvvete = QLineEdit(parent=self)

        lblDescription = QLabel('Описание:', parent=self)
        self.__teDescriptin = QTextEdit(parent=self)

        btnCategory = QToolButton(parent=self)
        btnCategory.setText('...')
        btnAddGroup = QToolButton(parent=self)
        btnAddGroup.setText('...')

        btnOk = QPushButton('Ok', parent=self)
        btnCancel = QPushButton('Отмена', parent=self)
        btnFileOpen = QPushButton('Файл', parent=self)

        layHDateNumber = QHBoxLayout()
        layVDate = QVBoxLayout()
        layVDate.addWidget(lblDate)
        layVDate.addWidget(self.__deDate)
        layHDateNumber.addLayout(layVDate)
        layVNumber = QVBoxLayout()
        layVNumber.addWidget(lblNumber)
        layVNumber.addWidget(self.__edNumber)
        layHDateNumber.addLayout(layVNumber)

        layHCategory = QHBoxLayout()
        layHCategory.addWidget(self.__cbCategory)
        layHCategory.addWidget(btnCategory)

        layHCroup = QHBoxLayout()
        layHCroup.addWidget(self.__cbGroup)
        layHCroup.addWidget(btnAddGroup)

        layHCountTempCuvvete = QHBoxLayout()
        layVCount = QVBoxLayout()
        layVCount.addWidget(lblCount)
        layVCount.addWidget(self.__edCount)
        layHCountTempCuvvete.addLayout(layVCount)
        layVTemp = QVBoxLayout()
        layVTemp.addWidget(lblTemp)
        layVTemp.addWidget(self.__edTemp)
        layHCountTempCuvvete.addLayout(layVTemp)
        layVCuvvete = QVBoxLayout()
        layVCuvvete.addWidget(lblCuvete)
        layVCuvvete.addWidget(self.__edCuvvete)
        layHCountTempCuvvete.addLayout(layVCuvvete)

        layV = QVBoxLayout(self)

        layV.addLayout(layHDateNumber)
        layV.addWidget(lblCategory)
        layV.addLayout(layHCategory)
        layV.addWidget(lblGroup)
        layV.addLayout(layHCroup)
        layV.addWidget(lblName)
        layV.addWidget(self.__edName)
        layV.addWidget(lblSubstance)
        layV.addWidget(self.__edSubstance)
        layV.addLayout(layHCountTempCuvvete)
        layV.addWidget(lblDescription)
        layV.addWidget(self.__teDescriptin)
        layH = QHBoxLayout()
        layH.addWidget(btnOk)
        layH.addWidget(btnCancel)
        layH.addWidget(btnFileOpen)
        layV.addLayout(layH)

        btnCancel.clicked.connect(self.reject)
        btnCategory.clicked.connect(self.btnCategory_clicked)

        print(self.geometry())

    def btnCategory_clicked(self):
        dlg_category = dlgCategories()
        dlg_category.exec()
        self.__cbCategory.model().refrechCategories()

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

    @property
    def name(self):
        result: str = self.__edName.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def substance(self):
        result: str = self.__edSubstance.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def countExp(self):
        result: str = self.__edCount.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def tempExp(self):
        result: str = self.__edTemp.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def cuvette(self):
        result: str = self.__edCuvvete.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def description(self):
        result: str = self.__teDescriptin.toPlainText().strip()
        if not result:
            return None
        else:
            return result
