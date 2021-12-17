# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(561, 491)
        mainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.tab)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label1)
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.graphicsView)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setStatusTip("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 23))
        self.menubar.setObjectName("menubar")
        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setCheckable(False)
        self.action.setWhatsThis("")
        self.action.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.action_2.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_2.setObjectName("action_2")
        self.menu_options.addAction(self.action_2)
        self.menu_about.addAction(self.action)
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label1.setText(_translate("mainWindow", "学生图书管理系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Tab 2"))
        self.menu_options.setTitle(_translate("mainWindow", "选项"))
        self.menu_about.setTitle(_translate("mainWindow", "关于"))
        self.action.setText(_translate("mainWindow", "关于作者"))
        self.action_2.setText(_translate("mainWindow", "退出"))

from PyQt5.QtWidgets import QApplication, QMainWindow  #导入PyQt相关模块

#from  SetupUi import *  #导入之前新生成的窗口模块

class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()  #创建对象
    myWin.show()    #显示窗口
    sys.exit(app.exec_())
