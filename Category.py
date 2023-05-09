from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QDialog, QToolButton, QHBoxLayout, QTableView, QVBoxLayout

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.refrechCategories()

    def refrechCategories(self):
        sql = '''
            SELECT name FROM categories
        '''
        self.setQuery(sql)


class dlgCategory(QDialog):
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

        tvCategory = QTableView(parent=self)
        model = Model(parent=self)
        tvCategory.setModel(model)

        layV = QVBoxLayout(self)
        layV.addLayout(layHButton)
        layV.addWidget(tvCategory)
