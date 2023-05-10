from PySide6.QtCore import Qt, Slot
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QDialog, QToolButton, QHBoxLayout, QTableView, QVBoxLayout, QLabel, QLineEdit
import sqlite3 as sl


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.refrechCategories()

    def refrechCategories(self):
        sql = '''
            SELECT name FROM categories
        '''
        self.setQuery(sql)

    def add(self, name):
        con = sl.connect('SFM.db')
        sql = '''INSERT INTO categories (name) values (?)'''
        data = [(name)]
        con.execute(sql, data)
        con.commit()
        self.refrechCategories()



class dlgCategories(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        layV = QVBoxLayout(self)
        layV.addLayout(layHButton)
        layV.addWidget(self.tvCategory)

        btnAddCategory.clicked.connect(self.btnAddCategory_clicked)

    @Slot()
    def btnAddCategory_clicked(self):
        dlg = dlgCategory()
        if dlg.exec():
            self.tvCategory.model().add(dlg.name)
            pass

class dlgCategory(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Категория')
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
        if self.name is None:
            return
        else:
            self.accept()

    @property
    def name(self):
        result: str = self.__edName.text().strip()
        if not result:
            return None
        else:
            return result
