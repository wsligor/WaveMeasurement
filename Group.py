from PySide6.QtCore import Qt, Slot
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QPushButton, QHeaderView, QMessageBox
from PySide6.QtWidgets import QDialog, QToolButton, QHBoxLayout, QTableView, QVBoxLayout, QLabel, QLineEdit
import sqlite3 as sl


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refrechGroup()

    def refrechGroup(self):
        sql = 'SELECT id, name FROM groups'
        self.setQuery(sql)

    def add(self, name):
        con = sl.connect('SFM.db')
        sql = 'INSERT INTO groups (name) values (?)'
        data = [name]
        con.execute(sql, data)
        con.commit()
        con.close()
        self.refrechGroup()

    def edit(self, id, name):
        con = sl.connect('SFM.db')
        sql = 'UPDATE groups SET name = "{}" WHERE id = {}'.format(name, id)
        con.execute(sql)
        con.commit()
        con.close()
        self.refrechGroup()

    def delete(self, id):
        con = sl.connect('SFM.db')
        sql = 'DELETE FROM groups WHERE id = {}'.format(id)
        con.execute(sql)
        con.commit()
        con.close()
        self.refrechGroup()


class dlgGroups(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Группы')
        self.resize(300, 400)

        btnAddGroup = QToolButton(parent=self)
        btnAddGroup.setText('+')
        btnEditGroup = QToolButton(parent=self)
        btnEditGroup.setText('...')
        btnDelGroup = QToolButton(parent=self)
        btnDelGroup.setText('-')

        layHButton = QHBoxLayout()
        layHButton.addWidget(btnAddGroup)
        layHButton.addWidget(btnEditGroup)
        layHButton.addWidget(btnDelGroup)
        layHButton.setAlignment(Qt.AlignmentFlag.AlignLeft)

        model = Model(parent=self)
        self.tvGroup = QTableView(parent=self)
        self.tvGroup.setModel(model)
        self.tvGroup.hideColumn(0)

        hh = self.tvGroup.horizontalHeader()
        hh.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        hh.hide()
        # self.tvCategory.horizontalHeader().setSelectionBehavior()

        layV = QVBoxLayout(self)
        layV.addLayout(layHButton)
        layV.addWidget(self.tvGroup)

        btnAddGroup.clicked.connect(self.btnAddGroup_clicked)
        btnEditGroup.clicked.connect(self.btnEditGroup_clicked)
        btnDelGroup.clicked.connect(self.btnDelGroup_clicked)

    @Slot()
    def btnAddGroup_clicked(self):
        dlg = dlgGroup()
        if dlg.exec():
            self.tvGroup.model().add(dlg.nameGroup)

    @Slot()
    def btnEditGroup_clicked(self):
        dlg = dlgGroup()
        row = self.tvGroup.currentIndex().row()
        id = self.tvGroup.model().record(row).value(0)
        dlg.nameGroup = self.tvGroup.model().record(row).value(1)
        if dlg.exec():
            self.tvGroup.model().edit(id, dlg.nameGroup)

    @Slot()
    def btnDelGroup_clicked(self):
        if QMessageBox.question(self, 'Категория', 'Вы уверены?'):
            row = self.tvGroup.currentIndex().row()
            id = self.tvGroup.model().record(row).value(0)
            self.tvGroup.model().delete(id)


class dlgGroup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Группа')
        self.resize(400, 80)

        lblName = QLabel('Наименование группы', parent=self)
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
        if self.nameGroup is None:
            return
        else:
            self.accept()

    @property
    def nameGroup(self):
        result: str = self.__edName.text().strip()
        if not result:
            return None
        else:
            return result

    @nameGroup.setter
    def nameGroup(self, value):
        self.__edName.setText(value)
