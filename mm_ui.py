# Form implementation generated from reading ui file 'mm.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from Application import Application


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(parent=self.splitter)
        self.widget.setObjectName("widget")
        self.layh1 = QtWidgets.QHBoxLayout(self.widget)
        self.layh1.setContentsMargins(0, 0, 0, 0)
        self.layh1.setObjectName("layh1")
        self.layv1 = QtWidgets.QVBoxLayout()
        self.layv1.setObjectName("layv1")
        self.layhComboBox = QtWidgets.QHBoxLayout()
        self.layhComboBox.setObjectName("layhComboBox")
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.layhComboBox.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.layhComboBox.addWidget(self.comboBox_2)
        self.layv1.addLayout(self.layhComboBox)
        self.tableView = QtWidgets.QTableView(parent=self.widget)
        self.tableView.setObjectName("tableView")
        self.layv1.addWidget(self.tableView)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.layv1.addWidget(self.label)
        self.layhButton1 = QtWidgets.QHBoxLayout()
        self.layhButton1.setObjectName("layhButton1")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.layhButton1.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.layhButton1.addWidget(self.pushButton_2)
        self.layv1.addLayout(self.layhButton1)
        self.layh1.addLayout(self.layv1)
        self.layvButton2 = QtWidgets.QVBoxLayout()
        self.layvButton2.setObjectName("layvButton2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.layvButton2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.layvButton2.addWidget(self.pushButton_4)
        self.layh1.addLayout(self.layvButton2)
        self.widget1 = QtWidgets.QWidget(parent=self.splitter)
        self.widget1.setObjectName("widget1")
        self.layh2 = QtWidgets.QVBoxLayout(self.widget1)
        self.layh2.setContentsMargins(0, 0, 0, 0)
        self.layh2.setObjectName("layh2")
        self.widget2 = QtWidgets.QWidget(parent=self.widget1)
        self.widget2.setMinimumSize(QtCore.QSize(0, 200))
        self.widget2.setObjectName("widget2")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.widget2)
        self.graphicsView.setGeometry(QtCore.QRect(30, 60, 161, 141))
        self.graphicsView.setObjectName("graphicsView")
        self.layh2.addWidget(self.widget2)
        self.layhButton3 = QtWidgets.QHBoxLayout()
        self.layhButton3.setObjectName("layhButton3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.layhButton3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.layhButton3.addWidget(self.pushButton_6)
        self.layh2.addLayout(self.layhButton3)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)

if __name__ == '__main__':
    app = Application(sys.argv)
    mn = Window()
    mn.show()

    result = app.exec()
    sys.exit(result)