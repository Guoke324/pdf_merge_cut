# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdf.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QAbstractItemView, QTableView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4) # 设置 列数
        self.tableWidget_2.setRowCount(11) # 设置 行数
        self.tableWidget_2.setHorizontalHeaderLabels(['文件名','      文件路径      ','文件大小','文件页码'])
        # self.tableWidget_2.setStyleSheet("background-color:transparent;")
        self.tableWidget_2.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);color: black;};")
        self.tableWidget_2.verticalHeader().setVisible(False) # 隐藏表头
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget_2.resizeColumnsToContents() # 设置列宽高按照内容自适应
        self.tableWidget_2.resizeRowsToContents() # # 设置行宽和高按照内容自适应
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # # 所有列自动拉伸，充满界面
        #self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        #self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.gridLayout_7.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setIconSize(QtCore.QSize(51, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4) # 设置 列数
        self.tableWidget.setRowCount(11) # 设置 行数
        self.tableWidget.setHorizontalHeaderLabels(['文件名','      文件路径      ','文件大小','文件页码'])
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);color: black;};")
        self.tableWidget.verticalHeader().setVisible(False) # 隐藏表头
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.resizeColumnsToContents() # 设置列宽高按照内容自适应
        self.tableWidget.resizeRowsToContents() # # 设置行宽和高按照内容自适应
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # # 所有列自动拉伸，充满界面
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.gridLayout_8.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("分割页码:1-20")
        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_6.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def size_format(self, size):
        if size < 1000:
            return '%i' % size + 'Byte'
        elif 1000 <= size < 1000000:
            return '%.1f' % float(size/1000) + 'KB'
        elif 1000000 <= size < 1000000000:
            return '%.1f' % float(size/1000000) + 'MB'
        elif 1000000000 <= size < 1000000000000:
            return '%.1f' % float(size/1000000000) + 'GB'
        elif 1000000000000 <= size:
            return '%.1f' % float(size/1000000000000) + 'TB'


    def newItem_showinfo_cut_pdf(self, i, name, num):
        newItem = QTableWidgetItem(name)
        newItem.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter) # 文字上下及左右都居中
        self.tableWidget.setItem(i, num, newItem)
        

    def newItem_showinfo_merge_pdf(self, i, name, num):
        newItem = QTableWidgetItem(name)
        newItem.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
        self.tableWidget_2.setItem(i, num, newItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF 合并及分割工具"))
        self.pushButton_5.setText(_translate("MainWindow", "添加"))
        self.pushButton_3.setText(_translate("MainWindow", "清空表格"))
        self.pushButton_6.setText(_translate("MainWindow", "合并"))
        self.pushButton_4.setText(_translate("MainWindow", "导出地址"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "PDF 合并"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_8.setText(_translate("MainWindow", "清空表格"))
        self.label_3.setText(_translate("MainWindow", "分割页码"))
        self.pushButton_7.setText(_translate("MainWindow", "导出地址"))
        self.pushButton_2.setText(_translate("MainWindow", "分割"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PDF 分割"))
