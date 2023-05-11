from PySide6.QtCore import Qt, Slot
from PySide6.QtSql import QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import QPushButton, QHeaderView, QMessageBox
from PySide6.QtWidgets import QDialog, QToolButton, QHBoxLayout, QTableView, QVBoxLayout, QLabel, QLineEdit
import sqlite3 as sl
from Application import Application

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.refrechCategories()

    def refrechCategories(self):
        sql = '''
            SELECT id, name FROM categories
        '''
        self.setQuery(sql)

    def add(self, name):
        con = sl.connect('SFM.db')
        sql = '''INSERT INTO categories (name) values (?)'''
        data = [(name)]
        con.execute(sql, data)
        con.commit()
        con.close()
        self.refrechCategories()

    def edit(self, id, name):
        con = sl.connect('SFM.db')
        sql = '''UPDATE categories SET name = "{}" WHERE id = {}'''.format(name, id)
        con.execute(sql)
        con.commit()
        con.close()
        self.refrechCategories()

    def delete(self, id):
        con = sl.connect('SFM.db')
        sql = '''DELETE FROM categories WHERE id = {}'''.format(id)
        con.execute(sql)
        con.commit()
        con.close()
        self.refrechCategories()



class dlgCategories(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Категории')
        self.resize(300, 400)

        btnAddCategory = QToolButton(parent=self)
        btnAddCategory.setText('+')
        btnEditCategory = QToolButton(parent=self)
        btnEditCategory.setText('...')
        btnDelCategory = QToolButton(parent=self)
        btnDelCategory.setText('-')

        layHButton = QHBoxLayout()
        layHButton.addWidget(btnAddCategory)
        layHButton.addWidget(btnEditCategory)
        layHButton.addWidget(btnDelCategory)
        layHButton.setAlignment(Qt.AlignmentFlag.AlignLeft)

        model = Model(parent=self)
        self.tvCategory = QTableView(parent=self)
        self.tvCategory.setModel(model)
        self.tvCategory.hideColumn(0)

        hh = self.tvCategory.horizontalHeader()
        hh.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        hh.hide()
        # self.tvCategory.horizontalHeader().setSelectionBehavior()

        layV = QVBoxLayout(self)
        layV.addLayout(layHButton)
        layV.addWidget(self.tvCategory)

        btnAddCategory.clicked.connect(self.btnAddCategory_clicked)
        btnEditCategory.clicked.connect(self.btnEditCategory_clicked)
        btnDelCategory.clicked.connect(self.btnDelCategory_clicked)

    @Slot()
    def btnAddCategory_clicked(self):
        dlg = dlgCategory()
        if dlg.exec():
            self.tvCategory.model().add(dlg.name_cat)

    @Slot()
    def btnEditCategory_clicked(self):
        dlg = dlgCategory()
        row = self.tvCategory.currentIndex().row()
        id = self.tvCategory.model().record(row).value(0)
        dlg.name_cat = self.tvCategory.model().record(row).value(1)
        if dlg.exec():
            self.tvCategory.model().edit(id, dlg.name_cat)

    @Slot()
    def btnDelCategory_clicked(self):
        if QMessageBox.question(self, 'Категория', 'Вы уверены?'):
            row = self.tvCategory.currentIndex().row()
            id = self.tvCategory.model().record(row).value(0)
            self.tvCategory.model().delete(id)


class dlgCategory(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Категория')

        self.resize(400, 80)


        lblName = QLabel('Наименование категории', parent=self)
        self.__edName = QLineEdit(parent=self)

        layHEdit = QHBoxLayout()
        layHEdit.addWidget(lblName)
        layHEdit.addWidget(self.__edName)

        btnOK = QPushButton('Сохранить')
        btnCancel = QPushButton('Отмена')

        layHButton = QHBoxLayout()
        layHButton.setAlignment(Qt.AlignmentFlag.AlignRight)
        layHButton.addWidget(btnOK)
        layHButton.addWidget(btnCancel)

        layV = QVBoxLayout(self)
        layV.addLayout(layHEdit)
        layV.addLayout(layHButton)

        btnCancel.clicked.connect(self.reject)
        btnOK.clicked.connect(self.btnOK_clicked)

    def btnOK_clicked(self):
        if self.name_cat is None:
            return
        else:
            self.accept()

    @property
    def name_cat(self):
        result: str = self.__edName.text().strip()
        if not result:
            return None
        else:
            return result

    @name_cat.setter
    def name_cat(self, value):
        self.__edName.setText(value)