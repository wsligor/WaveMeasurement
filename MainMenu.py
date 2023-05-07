from PySide6.QtWidgets import QMenuBar

class MainMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        bd_menu = self.addMenu("NameExp")
        help_menu = self.addMenu("Справка")

        self.__about_qt = help_menu.addAction('О библиотеке Qt')
        self.__about = help_menu.addAction('О программе...')

        self.__addNameExp = bd_menu.addAction('Добавить')
        self.__updateNameExp = bd_menu.addAction('Редактировать')
        self.__deleteNameExp = bd_menu.addAction('Удалить')

    @property
    def about(self):
        return self.__about

    @property
    def about_qt(self):
        return self.__about_qt

    @property
    def addNameExp(self):
        return self.__addNameExp

    @property
    def updateNameExp(self):
        return self.__updateNameExp

    @property
    def deleteNameExp(self):
        return self.__deleteNameExp