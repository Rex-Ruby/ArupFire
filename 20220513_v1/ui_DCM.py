# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_DCM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from SlotFunctions import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 811)
        font = QtGui.QFont()
        font.setFamily("宋体")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/pic_cover.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel {\n"
"    color:blue;\n"
"   font-size:11\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 410, 1121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 380, 1121, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(600, 30, 451, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        # self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)                       ####### Qpushbutton没有此函数，注释掉
        # self.label_5.setTextFormat(QtCore.Qt.AutoText)                             ####### Qpushbutton没有此函数，注释掉
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(0, 40, 441, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(7, 60, 434, 261))
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 93, 220))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 180))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(11, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(137)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(147, 63, 132, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(280, 60, 141, 39))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_8.setGeometry(QtCore.QRect(144, 99, 138, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 97, 141, 39))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 133, 141, 39))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_9.setGeometry(QtCore.QRect(144, 136, 138, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 50, 431, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(28, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(28, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(28, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(50, 460, 1031, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget_2.setLineWidth(1)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.comboBox_2 = QtWidgets.QComboBox(self.page)
        self.comboBox_2.setGeometry(QtCore.QRect(113, 50, 127, 41))
        self.comboBox_2.setAcceptDrops(True)
        self.comboBox_2.setAutoFillBackground(True)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setMaxVisibleItems(2)
        self.comboBox_2.setMaxCount(2)
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(238, 90, 126, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_2.setGeometry(QtCore.QRect(113, 10, 761, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Californian FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setAcceptDrops(False)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_2.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("IMG/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon2)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 3, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.comboBox_3 = QtWidgets.QComboBox(self.page)
        self.comboBox_3.setGeometry(QtCore.QRect(239, 50, 127, 41))
        self.comboBox_3.setAcceptDrops(True)
        self.comboBox_3.setAutoFillBackground(True)
        self.comboBox_3.setCurrentText("")
        self.comboBox_3.setMaxVisibleItems(3)
        self.comboBox_3.setMaxCount(3)
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(113, 90, 125, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.Btn_M_Page1_2 = QtWidgets.QPushButton(self.page)
        self.Btn_M_Page1_2.setGeometry(QtCore.QRect(616, 10, 254, 41))
        self.Btn_M_Page1_2.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 255, 255);\n"
"    border-image:url(C:/Users/jing.ma/Desktop/DCM/IMG/12e12e.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 121), stop:1 rgba(255, 255, 255, 100));\n"
"    border:none;\n"
"    font: 13pt \"Californian FB\";\n"
"    text-align:centert;\n"
"    color: blue\n"
"    \n"
"    }\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.134, y1:0.493955, x2:1, y2:0.562, stop:0 rgba(100, 111, 121, 200), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"    }\n"
"")
        self.Btn_M_Page1_2.setObjectName("Btn_M_Page1_2")
        self.comboBox_4 = QtWidgets.QComboBox(self.page)
        self.comboBox_4.setGeometry(QtCore.QRect(488, 50, 385, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMaxVisibleItems(5)
        self.comboBox_4.setMaxCount(5)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(490, 90, 384, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(380, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.page)
        self.comboBox_10.setGeometry(QtCore.QRect(363, 50, 127, 41))
        self.comboBox_10.setAcceptDrops(True)
        self.comboBox_10.setAutoFillBackground(True)
        self.comboBox_10.setCurrentText("")
        self.comboBox_10.setMaxVisibleItems(2)
        self.comboBox_10.setMaxCount(2)
        self.comboBox_10.setFrame(False)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(363, 90, 127, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(180, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(150, 50, 331, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(550, 50, 331, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(580, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.stackedWidget_2.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.menu_2.setFont(font)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionopen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionclose)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)
        self.comboBox_4.setCurrentIndex(-1)
        self.comboBox_10.setCurrentIndex(-1)
        self.comboBox_4.currentIndexChanged['QString'].connect(self.label_8.setText)
        self.comboBox_10.currentIndexChanged['QString'].connect(self.label_16.setText)
        self.comboBox_3.currentIndexChanged['QString'].connect(self.label_6.setText)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.label_7.setText)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arup  Fire Design Compliance Workbench"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "建筑定性"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "灭火救援设施"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "总平面布局"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "防火分区"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "平面布局"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "安全疏散和避难"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "建筑构造"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "消火栓系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "自动灭火系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "火灾自动报警系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "防排烟系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "电气"))
        self.label_4.setText(_translate("MainWindow", "审核结果选择"))
        self.label_5.setText(_translate("MainWindow", "导出"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "新建列"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "建筑定性"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "灭火救援设施"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "总平面布局"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "防火分区"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "平面布局"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "安全疏散和避难"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "建筑构造"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "消火栓系统"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "自动灭火系统"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "火灾自动报警系统"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "防排烟系统"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "电气"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("MainWindow", "建筑定性"))
        self.pushButton.setText(_translate("MainWindow", "全选"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "消防车道"))
        self.pushButton_2.setText(_translate("MainWindow", "全选"))
        self.pushButton_3.setText(_translate("MainWindow", "全选"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "消防车道"))
        self.label.setText(_translate("MainWindow", "建筑名称："))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入建筑/项目名称"))
        self.label_2.setText(_translate("MainWindow", "建筑类型："))

        ##### 给予变量名，方便赋值和读取
        type_building = self.comboBox
        type_building.setItemText(0, _translate("MainWindow", "请选择"))
        type_building.setItemText(1, _translate("MainWindow", "民用建筑"))
        type_building.setItemText(2, _translate("MainWindow", "工业建筑"))
        # type_building.itemText(0)                                         #### 根据索引读取选择

        # self.comboBox.setItemText(0, _translate("MainWindow", "请选择"))
        # self.comboBox.setItemText(1, _translate("MainWindow", "民用建筑"))
        # self.comboBox.setItemText(2, _translate("MainWindow", "工业建筑"))

        self.label_3.setText(_translate("MainWindow", "建筑高度："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入建筑高度（m）"))

        self.doubleValidator = QDoubleValidator()                                           # 新建双精度数值校验器变量
        self.doubleValidator.setRange(0, 5000)                                              # 范围0-5000
        self.doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        self.doubleValidator.setDecimals(2)                                                 # 设置精度2位
        self.lineEdit_2.setValidator(self.doubleValidator)                                  # 设置双精度校验器

        self.comboBox_2.setItemText(0, _translate("MainWindow", "地上建筑"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "地下/半地下"))
        self.label_6.setText(_translate("MainWindow", "选择结果"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "新建行"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "地上/地下"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "住宅/公建"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "有无喷淋"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "其他重要公共建筑"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "请选择"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "请选择"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "请选择"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("MainWindow", "请选择"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox_3.setItemText(0, _translate("MainWindow", "住宅建筑"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "公共建筑（非单层）"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "公共建筑（单层）"))
        self.label_7.setText(_translate("MainWindow", "选择结果"))
        self.Btn_M_Page1_2.setText(_translate("MainWindow", "确认"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "建筑高度24m以上部分任一楼层建筑面积大于1000m2的商店、展览、电信、邮政、财贸金融建筑和其他多种功能组合的建筑"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "医疗建筑、重要公共建筑、独立建造的老年人照料设施"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "省级及以上的广播电视和防灾指挥调度建筑、网局级和省级电力调度建筑"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "藏书超过100万册的图书馆、书库"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "其他"))
        self.label_8.setText(_translate("MainWindow", "选择结果"))
        self.label_9.setText(_translate("MainWindow", "请做出进一步选择"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "有喷淋"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "无喷淋"))
        self.label_16.setText(_translate("MainWindow", "选择结果"))
        self.label_10.setText(_translate("MainWindow", "基本信息"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "耐火等级和防火分区面积"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionsave.setText(_translate("MainWindow", "保存"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionclose.setText(_translate("MainWindow", "关闭"))

 # 将输入值保存至excel表格中，调用RestoreInfo中的函数type_building_choice和write_into_excel
        # 以上两个函数将以下数据存储到excel表格中：建筑/项目名称，民用/工业建筑，建筑高度
        self.lineEdit_2.textEdited.connect(lambda: write_into_excel(self.lineEdit.text(),
                                                                         type_building_choice(
                                                                             type_building.currentIndex()),
                                                                         self.lineEdit_2.text()))


        self.lineEdit.textEdited.connect(lambda: write_into_excel(self.lineEdit.text(),
                                                                             type_building_choice(
                                                                                 type_building.currentIndex()),
                                                                             self.lineEdit_2.text()))


        type_building.currentIndexChanged.connect(lambda: write_into_excel(self.lineEdit.text(),
                                                                             type_building_choice(
                                                                                 type_building.currentIndex()),
                                                                             self.lineEdit_2.text()))
#########################################################################################################################

        self.stackedWidget_2.hide()                                     ###### 点击tab改变页面的触发事件发生之前，先隐藏其信息面板
        self.label_9.hide()                                             ###### 防火分区：“请进一步做出选择”先不显示，判断条件还需要进一步满足时进行显示
        self.Btn_M_Page1_2.clicked.connect(judgeResult)                 ###### 对输入条件进行判断，不需要额外条件的话，可直接显示有关结果，若需要更多条件才能得到结果的话，提示用户继续进行条件的选择
        self.tabWidget.currentChanged.connect(lambda: transfer_tab(self.tabWidget, self.stackedWidget_2))  ### 点击不同的tab，触发显示各自的信息面板
        # self.tabWidget.tabBarClicked()
        # self.tabWidget.currentIndex()