from typing import Any
from datetime import date

from PySide6.QtCore import Qt, Slot, QModelIndex
from PySide6.QtWidgets import QTextEdit, QLineEdit, QComboBox, QDateEdit, QDialog, QHeaderView
from PySide6.QtWidgets import QTableView, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton, QLabel
from PySide6.QtSql import QSqlQueryModel

from Category import dlgCategories
from Group import dlgGroups


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.setHeaderData(0, Qt.Orientation.Horizontal, 'ID')
        self.setHeaderData(1, Qt.Orientation.Horizontal, 'Номер')

        self.refreshNameExp()

    def refreshNameExp(self):
        sql = 'SELECT id, name, date, number FROM nameExp'
        self.setQuery(sql)

    def data(self, item: QModelIndex, role: int = ...) -> Any:
        if not item.isValid():
            return
        if item.column() == 3:
            if role == Qt.ItemDataRole.TextAlignmentRole:
                print(super().data(item))
                return Qt.AlignmentFlag.AlignCenter
        return super().data(item, role)


class NameExp(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

        # выделение полной строки в таблице
        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        # убираем первый столбик ID
        self.hideColumn(0)
        # настройка горизонтального заголовка
        hh = self.horizontalHeader()
        # ширина всех столбцов регулируется по контексту
        hh.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # столбец "Name" регулируется растягиваясь на оставшуюся длину
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        # настройка вертикального заголовка
        hv = self.verticalHeader()
        # убираем вертикальную нумерацию строк
        hv.hide()

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


class ModelCategories(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refreshCategories()

    def refreshCategories(self):
        sql = 'SELECT name FROM categories'
        self.setQuery(sql)


class ModelGroups(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refreshGroups()

    def refreshGroups(self):
        sql = 'SELECT name FROM groups'
        self.setQuery(sql)


class dlgAddExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        lblDate = QLabel('Дата', parent=self)
        self.__deDate = QDateEdit(parent=self)
        self.__deDate.setDate(date.today())

        lblNumber = QLabel('Номер', parent=self)
        self.__edNumber = QLineEdit(parent=self)

        lblCategory = QLabel('Категория:', parent=self)
        self.__cbCategory = QComboBox(parent=self)
        self.modelCategories = ModelCategories(parent=self)
        self.__cbCategory.setModel(self.modelCategories)

        lblGroup = QLabel('Группа:', parent=self)
        self.__cbGroup = QComboBox(parent=self)
        self.modelGroups = ModelGroups(parent=self)
        self.__cbGroup.setModel(self.modelGroups)

        lblName = QLabel('Наименование:', parent=self)
        self.__edName = QLineEdit(parent=self)

        lblSubstance = QLabel('Образец:', parent=self)
        self.__edSubstance = QLineEdit(parent=self)

        lblCount = QLabel('% содержания', parent=self)
        self.__edCount = QLineEdit(parent=self)

        lblTemp = QLabel('Температура:', parent=self)
        self.__edTemp = QLineEdit(parent=self)

        lblCuvette = QLabel('Кювета', parent=self)
        self.__edCuvette = QLineEdit(parent=self)

        lblDescription = QLabel('Описание:', parent=self)
        self.__teDescription = QTextEdit(parent=self)

        btnCategory = QToolButton(parent=self)
        btnCategory.setText('...')
        btnGroup = QToolButton(parent=self)
        btnGroup.setText('...')

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
        layHCroup.addWidget(btnGroup)

        layHCountTempCuvette = QHBoxLayout()
        layVCount = QVBoxLayout()
        layVCount.addWidget(lblCount)
        layVCount.addWidget(self.__edCount)
        layHCountTempCuvette.addLayout(layVCount)
        layVTemp = QVBoxLayout()
        layVTemp.addWidget(lblTemp)
        layVTemp.addWidget(self.__edTemp)
        layHCountTempCuvette.addLayout(layVTemp)
        layVCuvette = QVBoxLayout()
        layVCuvette.addWidget(lblCuvette)
        layVCuvette.addWidget(self.__edCuvette)
        layHCountTempCuvette.addLayout(layVCuvette)

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
        layV.addLayout(layHCountTempCuvette)
        layV.addWidget(lblDescription)
        layV.addWidget(self.__teDescription)
        layH = QHBoxLayout()
        layH.addWidget(btnOk)
        layH.addWidget(btnCancel)
        layH.addWidget(btnFileOpen)
        layV.addLayout(layH)

        btnCancel.clicked.connect(self.reject)
        btnCategory.clicked.connect(self.btnCategory_clicked)
        btnGroup.clicked.connect(self.btnGroup_clicked)

    def btnGroup_clicked(self):
        dlg_groups = dlgGroups()
        dlg_groups.exec()
        self.__cbGroup.model().refrechGroups()

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
        result: str = self.__edCuvette.text().strip()
        if not result:
            return None
        else:
            return result

    @property
    def description(self):
        result: str = self.__teDescription.toPlainText().strip()
        if not result:
            return None
        else:
            return result
