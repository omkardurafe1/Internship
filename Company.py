# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Company_form(object):
    def setupUi(self, Company_form):
        Company_form.setObjectName("Company_form")
        Company_form.resize(952, 906)
        self.groupBox = QtWidgets.QGroupBox(Company_form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 861, 751))
        self.groupBox.setStyleSheet("background-color: rgb(221, 255, 246);\n"
"background-color: rgb(80, 80, 80);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 20, 681, 351))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 151, 33);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Ratechart_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Ratechart_combo.setGeometry(QtCore.QRect(120, 20, 311, 20))
        self.Ratechart_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Ratechart_combo.setObjectName("Ratechart_combo")
        self.Ratechart_combo.addItem("")
        self.AddRtNm_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.AddRtNm_btn.setGeometry(QtCore.QRect(440, 20, 75, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AddRtNm_btn.setFont(font)
        self.AddRtNm_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.AddRtNm_btn.setObjectName("AddRtNm_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 271, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Cow_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Cow_lbl.setGeometry(QtCore.QRect(10, 40, 23, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cow_lbl.setFont(font)
        self.Cow_lbl.setObjectName("Cow_lbl")
        self.Below_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Below_lbl.setGeometry(QtCore.QRect(40, 20, 33, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Below_lbl.setFont(font)
        self.Below_lbl.setObjectName("Below_lbl")
        self.Vas_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Vas_lbl.setGeometry(QtCore.QRect(80, 20, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Vas_lbl.setFont(font)
        self.Vas_lbl.setObjectName("Vas_lbl")
        self.Curd_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Curd_lbl.setGeometry(QtCore.QRect(120, 20, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Curd_lbl.setFont(font)
        self.Curd_lbl.setObjectName("Curd_lbl")
        self.Std_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Std_lbl.setGeometry(QtCore.QRect(160, 20, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Std_lbl.setFont(font)
        self.Std_lbl.setObjectName("Std_lbl")
        self.AddEvn_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.AddEvn_lbl.setGeometry(QtCore.QRect(200, 20, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AddEvn_lbl.setFont(font)
        self.AddEvn_lbl.setObjectName("AddEvn_lbl")
        self.CBelow_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CBelow_txt.setGeometry(QtCore.QRect(40, 40, 31, 16))
        self.CBelow_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CBelow_txt.setObjectName("CBelow_txt")
        self.CBelow_txt.setPlaceholderText('0.00')
        self.CVas_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CVas_txt.setGeometry(QtCore.QRect(80, 40, 31, 16))
        self.CVas_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CVas_txt.setObjectName("CVas_txt")
        self.CVas_txt.setPlaceholderText('0.00')
        self.CCurd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CCurd_txt.setGeometry(QtCore.QRect(120, 40, 31, 16))
        self.CCurd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CCurd_txt.setObjectName("CCurd_txt")
        self.CCurd_txt.setPlaceholderText('0.00')
        self.CStd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CStd_txt.setGeometry(QtCore.QRect(160, 40, 31, 16))
        self.CStd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CStd_txt.setObjectName("CStd_txt")
        self.CStd_txt.setPlaceholderText('0.00')
        self.CAddEvn_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CAddEvn_txt.setGeometry(QtCore.QRect(200, 40, 31, 16))
        self.CAddEvn_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CAddEvn_txt.setObjectName("CAddEvn_txt")
        self.CAddEvn_txt.setPlaceholderText('0.00')
        self.Buff_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Buff_lbl.setGeometry(QtCore.QRect(10, 70, 23, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Buff_lbl.setFont(font)
        self.Buff_lbl.setObjectName("Buff_lbl")
        self.BCurd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BCurd_txt.setGeometry(QtCore.QRect(120, 70, 31, 16))
        self.BCurd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BCurd_txt.setObjectName("BCurd_txt")
        self.BCurd_txt.setPlaceholderText('0.00')
        self.Bstd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.Bstd_txt.setGeometry(QtCore.QRect(160, 70, 31, 16))
        self.Bstd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Bstd_txt.setObjectName("Bstd_txt")
        self.Bstd_txt.setPlaceholderText('0.00')
        self.BBelow_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BBelow_txt.setGeometry(QtCore.QRect(40, 70, 31, 16))
        self.BBelow_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BBelow_txt.setObjectName("BBelow_txt")
        self.BBelow_txt.setPlaceholderText('0.00')
        self.BVas_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BVas_txt.setGeometry(QtCore.QRect(80, 70, 31, 16))
        self.BVas_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BVas_txt.setObjectName("BVas_txt")
        self.BVas_txt.setPlaceholderText('0.00')
        self.BAddEvn_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BAddEvn_txt.setGeometry(QtCore.QRect(200, 70, 31, 16))
        self.BAddEvn_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BAddEvn_txt.setObjectName("BAddEvn_txt")
        self.BAddEvn_txt.setPlaceholderText('0.00')
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 130, 231, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 101, 71))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.F_Fat_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.F_Fat_lbl.setGeometry(QtCore.QRect(10, 0, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F_Fat_lbl.setFont(font)
        self.F_Fat_lbl.setObjectName("F_Fat_lbl")
        self.T_fat_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.T_fat_lbl.setGeometry(QtCore.QRect(60, 0, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.T_fat_lbl.setFont(font)
        self.T_fat_lbl.setObjectName("T_fat_lbl")
        self.BTFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.BTFat_txt.setGeometry(QtCore.QRect(60, 50, 31, 16))
        self.BTFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BTFat_txt.setObjectName("BTFat_txt")
        self.BTFat_txt.setPlaceholderText('0.00')
        self.CFFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.CFFat_txt.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.CFFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CFFat_txt.setObjectName("CFFat_txt")
        self.CFFat_txt.setPlaceholderText('0.00')
        self.BFFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.BFFat_txt.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.BFFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BFFat_txt.setObjectName("BFFat_txt")
        self.BFFat_txt.setPlaceholderText('0.00')
        self.CTFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.CTFat_txt.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.CTFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CTFat_txt.setObjectName("CTFat_txt")
        self.CTFat_txt.setPlaceholderText('0.00')
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(120, 20, 101, 71))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.F_lct_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.F_lct_lbl.setGeometry(QtCore.QRect(10, 0, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F_lct_lbl.setFont(font)
        self.F_lct_lbl.setObjectName("F_lct_lbl")
        self.T_lct_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.T_lct_lbl.setGeometry(QtCore.QRect(60, 0, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.T_lct_lbl.setFont(font)
        self.T_lct_lbl.setObjectName("T_lct_lbl")
        self.BTlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.BTlct_txt.setGeometry(QtCore.QRect(60, 50, 31, 16))
        self.BTlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BTlct_txt.setObjectName("BTlct_txt")
        self.BTlct_txt.setPlaceholderText('0.00')
        self.CFlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.CFlct_txt.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.CFlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CFlct_txt.setObjectName("CFlct_txt")
        self.CFlct_txt.setPlaceholderText('0.00')
        self.BFlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.BFlct_txt.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.BFlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BFlct_txt.setObjectName("BFlct_txt")
        self.BFlct_txt.setPlaceholderText('0.00')
        self.TLct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.TLct_txt.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.TLct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TLct_txt.setObjectName("TLct_txt")
        self.TLct_txt.setPlaceholderText('0.00')
        self.RTChrtFileNm_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.RTChrtFileNm_lbl.setGeometry(QtCore.QRect(10, 240, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RTChrtFileNm_lbl.setFont(font)
        self.RTChrtFileNm_lbl.setObjectName("RTChrtFileNm_lbl")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(100, 240, 321, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.Sel_xls_File_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Sel_xls_File_btn.setGeometry(QtCore.QRect(440, 240, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Sel_xls_File_btn.setFont(font)
        self.Sel_xls_File_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Sel_xls_File_btn.setObjectName("Sel_xls_File_btn")
        self.Route_lbl1 = QtWidgets.QLabel(self.groupBox_2)
        self.Route_lbl1.setGeometry(QtCore.QRect(50, 270, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Route_lbl1.setFont(font)
        self.Route_lbl1.setObjectName("Route_lbl1")
        self.Route1_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Route1_combo.setGeometry(QtCore.QRect(100, 270, 321, 22))
        self.Route1_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Route1_combo.setObjectName("Route1_combo")
        self.NewSetting_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.NewSetting_btn.setGeometry(QtCore.QRect(440, 270, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NewSetting_btn.setFont(font)
        self.NewSetting_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.NewSetting_btn.setObjectName("NewSetting_btn")
        self.Route2_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Route2_combo.setGeometry(QtCore.QRect(100, 300, 321, 22))
        self.Route2_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Route2_combo.setObjectName("Route2_combo")
        self.Route_lbl2 = QtWidgets.QLabel(self.groupBox_2)
        self.Route_lbl2.setGeometry(QtCore.QRect(50, 300, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Route_lbl2.setFont(font)
        self.Route_lbl2.setObjectName("Route_lbl2")
        self.Update_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Update_btn.setGeometry(QtCore.QRect(440, 300, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Update_btn.setFont(font)
        self.Update_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Update_btn.setObjectName("Update_btn")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 50, 511, 80))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.Milk_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Milk_combo.setGeometry(QtCore.QRect(34, 10, 51, 18))
        self.Milk_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Milk_combo.setObjectName("Milk_combo")
        self.Milk_combo.addItem("")
        self.Milk_combo.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_7)
        self.dateEdit.setGeometry(QtCore.QRect(100, 50, 110, 16))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.Method_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Method_lbl.setGeometry(QtCore.QRect(384, 10, 51, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Method_lbl.setFont(font)
        self.Method_lbl.setObjectName("Method_lbl")
        self.Method_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Method_combo.setGeometry(QtCore.QRect(434, 10, 75, 18))
        self.Method_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Method_combo.setObjectName("Method_combo")
        self.Method_combo.addItem("")
        self.FIle_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.FIle_combo.setGeometry(QtCore.QRect(434, 50, 75, 16))
        self.FIle_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FIle_combo.setObjectName("FIle_combo")
        self.FIle_combo.addItem("")
        self.Milk_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Milk_lbl.setGeometry(QtCore.QRect(4, 10, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Milk_lbl.setFont(font)
        self.Milk_lbl.setObjectName("Milk_lbl")
        self.Apply_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Apply_lbl.setGeometry(QtCore.QRect(244, 50, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Apply_lbl.setFont(font)
        self.Apply_lbl.setObjectName("Apply_lbl")
        self.Base_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Base_combo.setGeometry(QtCore.QRect(284, 10, 81, 18))
        self.Base_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Base_combo.setObjectName("Base_combo")
        self.Base_combo.addItem("")
        self.Base_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Base_lbl.setGeometry(QtCore.QRect(244, 10, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Base_lbl.setFont(font)
        self.Base_lbl.setObjectName("Base_lbl")
        self.Date_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Date_lbl.setGeometry(QtCore.QRect(4, 50, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Date_lbl.setFont(font)
        self.Date_lbl.setObjectName("Date_lbl")
        self.File_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.File_lbl.setGeometry(QtCore.QRect(390, 50, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.File_lbl.setFont(font)
        self.File_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.File_lbl.setObjectName("File_lbl")
        self.Shift_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Shift_lbl.setGeometry(QtCore.QRect(104, 10, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Shift_lbl.setFont(font)
        self.Shift_lbl.setObjectName("Shift_lbl")
        self.Shift_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Shift_combo.setGeometry(QtCore.QRect(144, 10, 81, 18))
        self.Shift_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Shift_combo.setObjectName("Shift_combo")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Apply_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Apply_combo.setGeometry(QtCore.QRect(284, 50, 81, 18))
        self.Apply_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Apply_combo.setObjectName("Apply_combo")
        self.Apply_combo.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(129, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(40, 390, 251, 251))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.tab_3)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 150, 251, 16))
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.tabWidget.addTab(self.tab_3, "")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(290, 390, 191, 251))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_2.setGeometry(QtCore.QRect(490, 390, 231, 251))
        self.tableWidget_2.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(55)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(41)
        self.New_btn = QtWidgets.QPushButton(self.groupBox)
        self.New_btn.setGeometry(QtCore.QRect(40, 650, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.New_btn.setFont(font)
        self.New_btn.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"background-color: rgb(171, 196, 255);")
        self.New_btn.setObjectName("New_btn")
        self.Cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.Cancel_btn.setGeometry(QtCore.QRect(130, 650, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.Export_btn = QtWidgets.QPushButton(self.groupBox)
        self.Export_btn.setGeometry(QtCore.QRect(220, 650, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Export_btn.setFont(font)
        self.Export_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Export_btn.setObjectName("Export_btn")
        self.Import_RtChrt_btn = QtWidgets.QPushButton(self.groupBox)
        self.Import_RtChrt_btn.setGeometry(QtCore.QRect(310, 650, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Import_RtChrt_btn.setFont(font)
        self.Import_RtChrt_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Import_RtChrt_btn.setObjectName("Import_RtChrt_btn")
        self.Excel_btn = QtWidgets.QPushButton(self.groupBox)
        self.Excel_btn.setGeometry(QtCore.QRect(420, 650, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Excel_btn.setFont(font)
        self.Excel_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Excel_btn.setObjectName("Excel_btn")
        self.Text_btn = QtWidgets.QPushButton(self.groupBox)
        self.Text_btn.setGeometry(QtCore.QRect(520, 650, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Text_btn.setFont(font)
        self.Text_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Text_btn.setObjectName("Text_btn")
        self.Exit_btn = QtWidgets.QPushButton(self.groupBox)
        self.Exit_btn.setGeometry(QtCore.QRect(620, 650, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit_btn.setFont(font)
        self.Exit_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Exit_btn.setObjectName("Exit_btn")

        self.retranslateUi(Company_form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Company_form)

    def retranslateUi(self, Company_form):
        _translate = QtCore.QCoreApplication.translate
        Company_form.setWindowTitle(_translate("Company_form", "Form"))
        self.groupBox_2.setTitle(_translate("Company_form", "Rate Chart Setting"))
        self.label.setText(_translate("Company_form", "Rate Chart Name :"))
        self.Ratechart_combo.setItemText(0, _translate("Company_form", "Rate Chart"))
        self.AddRtNm_btn.setText(_translate("Company_form", "AddRtNm"))
        self.groupBox_3.setTitle(_translate("Company_form", "Below Grade Milk Rate"))
        self.Cow_lbl.setText(_translate("Company_form", "Cow"))
        self.Below_lbl.setText(_translate("Company_form", "Below"))
        self.Vas_lbl.setText(_translate("Company_form", "Vas"))
        self.Curd_lbl.setText(_translate("Company_form", "Curd"))
        self.Std_lbl.setText(_translate("Company_form", "Std"))
        self.AddEvn_lbl.setText(_translate("Company_form", "AddEvn"))
        self.Buff_lbl.setText(_translate("Company_form", "Buff"))
        self.groupBox_4.setTitle(_translate("Company_form", "RtChrt_From-To Range"))
        self.F_Fat_lbl.setText(_translate("Company_form", "F-Fat"))
        self.T_fat_lbl.setText(_translate("Company_form", "T-Fat"))
        self.F_lct_lbl.setText(_translate("Company_form", "F-Lct"))
        self.T_lct_lbl.setText(_translate("Company_form", "T-Lct"))
        self.RTChrtFileNm_lbl.setText(_translate("Company_form", "RtChrt FileNm:"))
        self.Sel_xls_File_btn.setText(_translate("Company_form", "Sel XLs File"))
        self.Route_lbl1.setText(_translate("Company_form", "Route"))
        self.NewSetting_btn.setText(_translate("Company_form", "New Setting"))
        self.Route_lbl2.setText(_translate("Company_form", "Route"))
        self.Update_btn.setText(_translate("Company_form", "Update"))
        self.Milk_combo.setItemText(0, _translate("Company_form", "Cow"))
        self.Milk_combo.setItemText(1, _translate("Company_form", "Bufellow"))
        self.Method_lbl.setText(_translate("Company_form", "Method:"))
        self.Method_combo.setItemText(0, _translate("Company_form", "RateChart"))
        self.FIle_combo.setItemText(0, _translate("Company_form", "Xls"))
        self.Milk_lbl.setText(_translate("Company_form", "Milk:"))
        self.Apply_lbl.setText(_translate("Company_form", "Apply:"))
        self.Base_combo.setItemText(0, _translate("Company_form", "Fat/Lact"))
        self.Base_lbl.setText(_translate("Company_form", "Base:"))
        self.Date_lbl.setText(_translate("Company_form", "Apply From Date:"))
        self.File_lbl.setText(_translate("Company_form", "File:"))
        self.Shift_lbl.setText(_translate("Company_form", "Shift:"))
        self.Shift_combo.setItemText(0, _translate("Company_form", "Moning"))
        self.Shift_combo.setItemText(1, _translate("Company_form", "Noon"))
        self.Shift_combo.setItemText(2, _translate("Company_form", "Night"))
        self.Apply_combo.setItemText(0, _translate("Company_form", "All"))
        self.label_3.setText(_translate("Company_form", "Company Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Company_form", "118"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Company_form", "108"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Company_form", "109"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Company_form", "Upto Fat"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Company_form", "Fat Rate"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Company_form", " Fat"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Company_form", "Lacto"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Company_form", "SNF"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Company_form", "Rate"))
        self.New_btn.setText(_translate("Company_form", "New"))
        self.Cancel_btn.setText(_translate("Company_form", "Cancel"))
        self.Export_btn.setText(_translate("Company_form", "Export RtChrt"))
        self.Import_RtChrt_btn.setText(_translate("Company_form", "Import RtChrt"))
        self.Excel_btn.setText(_translate("Company_form", "Excel "))
        self.Text_btn.setText(_translate("Company_form", "Text"))
        self.Exit_btn.setText(_translate("Company_form", "Exit"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Company_form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())