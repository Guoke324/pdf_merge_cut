#!/usr/bin/env python
# coding=utf-8
# ----- ----- ----- ----
# @Author       : Guoke324
# @Date         : 2021-03-16 15:57:49
# @Email        : querysoft2019@outlook.com
# @LastEditTime : 2021-07-19 14:45:10


import sys,os
import PyPDF2
from pdfui import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QHBoxLayout

merge_list = []
cut_list = []
class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.merge_pdf) #实现按钮点击功能
        self.pushButton_2.clicked.connect(self.cut_pdf) #实现按钮点击功能
        self.pushButton_5.clicked.connect(self.showinfo_merge_pdf)
        self.pushButton.clicked.connect(self.showinfo_cut_pdf)
        self.pushButton_3.clicked.connect(self.clear_merge_data)
        self.pushButton_4.clicked.connect(self.merge_save_event)
        self.pushButton_8.clicked.connect(self.clear_cut_data)
        self.pushButton_7.clicked.connect(self.cut_save_event)



    def Error_tips(self,tips, text):
        return QMessageBox.warning(self, tips, text, QMessageBox.Yes | QMessageBox.Yes)


    def open_pdf(self, who_list, files_name, pdfName):
        try:
            print(who_list,12312312)
            if os.path.splitext(files_name)[1] == ".pdf":
                Reader = PyPDF2.PdfFileReader(open(pdfName, 'rb'))  # 打开pdf文件 Reader = PdfFileReader(readFile)
                NumPages = Reader.getNumPages()
                print(NumPages)
            else:
                who_list.pop()
                self.Error_tips("错误", "文件不是 pdf 文件，请重新选择！")
                print("文件不是 pdf 文件，请重新选择！")
                print(NumPages)
            return NumPages
        except Exception as e:
            pass

    def clear_merge_data(self):
        print("clear_merge_data")
        # self.tableWidget_2.clear()   #清除所有数据--包括标题头
        self.tableWidget_2.clearContents()  # 清除所有数据--不包括标题头

    def clear_cut_data(self):
        print("clear_cut_data")
        self.tableWidget.clearContents()

    def merge_save_event(self):
        # global merge_save_path
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "", "PDF Files(*pdf)")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        self.lineEdit_2.setText(fileName2)

    def cut_save_event(self):
        # global merge_save_path
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "", "PDF Files(*pdf)")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        self.lineEdit_4.setText(fileName2)


    def showinfo_merge_pdf(self):
        try:
            pdfName, imgType = QFileDialog.getOpenFileName(self, "添加 PDF", "", "All Files(*)") #打开文件夹选择文件
            self.lineEdit_3.setText(pdfName) # lineEdit 设置文本框内容
            # self.textEdit.append(pdfName) # textEdit 追加字符创
            print(pdfName,234234234 )
            if pdfName:
                if pdfName in merge_list:
                    print(merge_list,1)
                    self.Error_tips("错误", "PDF 文件已选择，请勿重复选择！")
                    print(merge_list)
                else:
                    merge_list.append(pdfName)
                    # print(len(test_list))
                    # print(test_list)
                    files_name = os.path.basename(pdfName) # 获取文件名
                    size = self.size_format(os.path.getsize(pdfName))
                    i = len(merge_list)-1
                    print(i)
                    NumPages = self.open_pdf(merge_list, files_name, pdfName)
                    if NumPages:
                        self.newItem_showinfo_merge_pdf(i, files_name,0)
                        self.newItem_showinfo_merge_pdf(i, pdfName,1)
                        self.newItem_showinfo_merge_pdf(i, size,2)
                        self.newItem_showinfo_merge_pdf(i, "1 - " + str(NumPages),3)
                        print(merge_list)
                        print("[{},{},{},{}]".format(files_name,pdfName,size,NumPages))
                    else:
                        pass
        except Exception as e:
            self.Error_tips("错误", "请选择文件")


    def showinfo_cut_pdf(self):
        try:
            pdfName, imgType = QFileDialog.getOpenFileName(self, "添加 PDF", "", "All Files(*)") #打开文件夹选择文件
            self.lineEdit.setText(pdfName) # lineEdit 设置文本框内容
            # self.textEdit.append(pdfName) # textEdit 追加字符创
            print(pdfName, )
            if pdfName:
                if pdfName in cut_list:
                    self.Error_tips("错误", "PDF 文件已已选择，请勿重复选择！") 
                else:
                    cut_list.append(pdfName)
                    # print(len(test_list))
                    # print(test_list)
                    files_name = os.path.basename(pdfName) # 获取文件名
                    size = self.size_format(os.path.getsize(pdfName))
                    i = len(cut_list)-1
                    if i == 0:
                        NumPages = self.open_pdf(cut_list, files_name, pdfName)
                        if NumPages:
                            self.newItem_showinfo_cut_pdf(i, files_name,0)
                            self.newItem_showinfo_cut_pdf(i, pdfName,1)
                            self.newItem_showinfo_cut_pdf(i, size,2)
                            self.newItem_showinfo_cut_pdf(i, "1 - " + str(NumPages),3)
                            print(cut_list)
                            print("[{},{},{},{}]".format(files_name,pdfName,size,NumPages))
                        else:
                            pass
                    else:
                        self.Error_tips("错误", "PDF 文件分割只支持一个文件！") 
        except Exception as e:
            print(e)
            self.Error_tips("错误", "请选择文件！")
            # files_name = os.path.basename(pdfName) # 获取文件名
            # size = self.size_format(os.path.getsize(pdfName)) # 获取文件大小
            # self.newItem_showinfo_cut_pdf(files_name,0) # 输出显示
            # self.newItem_showinfo_cut_pdf(pdfName,1)
            # self.newItem_showinfo_cut_pdf(size,2)
            # print(test_list)
            # print(pdfName,type(pdfName))


    def cut_pdf(self):
        if len(cut_list) != 0:
            input_pdf = cut_list[0]
            print("分割 PDF 为：", input_pdf)
            Reader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
            PdfFileWriter = PyPDF2.PdfFileWriter() # 获取一个 PdfFileWriter 对象
            print(self.lineEdit_5.text())
            Numlist = self.lineEdit_5.text().split("-")
            outpdf = self.lineEdit_4.text()
            if outpdf:
                if len(Numlist) == 2:
                    Num = int(Numlist[0].strip()) - 1
                    print(Num)
                    try:
                        for i in range(Num,int(Numlist[1].strip())):
                            PdfFileWriter.addPage(Reader.getPage(i)) # 将一个 PageObject 加入到 PdfFileWriter 中
                            PdfFileWriter.write(open(outpdf, 'wb'))  # 输出到 outpdf 文件中
                        cut_list.clear()
                        self.Error_tips("提示", "PDF 文件已分割完成！")
                    except Exception as e:
                        self.Error_tips("提示", "PDF 文件未能成功分割，请检查！")
                else:
                    self.Error_tips("提示", "PDF 文件分割页码有误，请检查！") 
            else:
                self.Error_tips("提示", "请输入 PDF 导出路径及文件名，谢谢！") 
        else:
             self.Error_tips("提示", "请输入添加要分割的pdf文件，谢谢！") 


    def merge_pdf(self):
        # 合并 pdf
        # print(self.textEdit.toPlainText()) # 读取 textEdit 的内容
        if len(merge_list) != 0:
            outpdf = self.lineEdit_2.text()
            print("输出 PDF 文件名为",outpdf)
            if outpdf:
                try:
                    PdfFileWriter = PyPDF2.PdfFileWriter()
                    for files in merge_list:
                        Reader = PyPDF2.PdfFileReader(open(files, 'rb'))
                        Pages = Reader.getNumPages()
                        for index in range(0,Pages):
                            pageObj = Reader.getPage(index)
                            PdfFileWriter.addPage(pageObj)
                    PdfFileWriter.write(open(outpdf, 'wb'))
                    merge_list.clear()
                    self.Error_tips("提示", "PDF 文件合并完成！") 
                except Exception as e:
                    self.Error_tips("提示", "PDF 文件未能成功合并，请检查！")
            else:
                self.Error_tips("提示", "请输入 PDF 导出路径及文件名，谢谢！") 
        else:
            self.Error_tips("提示", "请输入添加要合成的pdf文件，谢谢！") 





    def closeEvent(self, event):       
        reply = QMessageBox.question(self, '提示',
            "你确认退出吗?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())