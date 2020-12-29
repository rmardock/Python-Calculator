import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
	#UI Initialization
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 81, 71))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 50, 81, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 50, 81, 71))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 130, 81, 71))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 130, 81, 71))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 130, 81, 71))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 50, 81, 71))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 130, 81, 71))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 210, 81, 71))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 210, 81, 71))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 210, 81, 71))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 210, 81, 71))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 290, 81, 71))
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(90, 370, 261, 71))
        self.pushButton_14.setObjectName("pushButton_14")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 331, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(90, 290, 81, 71))
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(180, 290, 81, 71))
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(270, 290, 81, 71))
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 370, 81, 71))
        self.pushButton_18.setObjectName("pushButton_18")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "√"))
        self.pushButton_8.setText(_translate("MainWindow", "x²"))
        self.pushButton_9.setText(_translate("MainWindow", "1"))
        self.pushButton_10.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_12.setText(_translate("MainWindow", "*"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_14.setText(_translate("MainWindow", "="))
        self.pushButton_15.setText(_translate("MainWindow", "+"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "÷"))
        self.pushButton_18.setText(_translate("MainWindow", "CE"))

    #Button connections for gui
    def initUI(self, MainWindow):
    	#Number buttons
    	self.pushButton_13.clicked.connect(self.button0_click)
    	self.pushButton_9.clicked.connect(self.button1_click)
    	self.pushButton_10.clicked.connect(self.button2_click)
    	self.pushButton_11.clicked.connect(self.button3_click)
    	self.pushButton_4.clicked.connect(self.button4_click)
    	self.pushButton_5.clicked.connect(self.button5_click)
    	self.pushButton_6.clicked.connect(self.button6_click)
    	self.pushButton.clicked.connect(self.button7_click)
    	self.pushButton_2.clicked.connect(self.button8_click)
    	self.pushButton_3.clicked.connect(self.button9_click)

    	#Function buttons
    	self.pushButton_15.clicked.connect(self.button_add_click)
    	self.pushButton_16.clicked.connect(self.button_subtract_click)
    	self.pushButton_12.clicked.connect(self.button_multiply_click)
    	self.pushButton_17.clicked.connect(self.button_divide_click)
    	self.pushButton_7.clicked.connect(self.button_square_root)
    	self.pushButton_8.clicked.connect(self.button_squared)
    	self.pushButton_14.clicked.connect(self.button_equal)
    	self.pushButton_18.clicked.connect(self.button_clear)

    	global math_function
    	math_function = ""
    	
    #Button functions 
    def button0_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.setText(text + "0")

    def button1_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.setText(text + "1")

    def button2_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.setText(text + "2")

    def button3_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.setText(text + "3")

    def button4_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.setText(text + "4")

    def button5_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.text()
    	self.lineEdit.setText(text + "5")

    def button6_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.text()
    	self.lineEdit.setText(text + "6")

    def button7_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.text()
    	self.lineEdit.setText(text + "7")

    def button8_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.text()
    	self.lineEdit.setText(text + "8")

    def button9_click(self):
    	text = self.lineEdit.text()
    	self.lineEdit.text()
    	self.lineEdit.setText(text + "9")

    def button_add_click(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	global math_function
    	math_function = "addition"
    	fnum = float(fnumber)
    	self.lineEdit.clear()

    def button_subtract_click(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	global math_function
    	math_function = "subtraction"
    	fnum = float(fnumber)
    	self.lineEdit.clear()

    def button_multiply_click(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	global math_function
    	math_function = "multiplication"
    	fnum = float(fnumber)
    	self.lineEdit.clear()

    def button_divide_click(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	global math_function
    	math_function = "division"
    	fnum = float(fnumber)
    	self.lineEdit.clear()

    def button_squared(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	fnum = float(fnumber)
    	self.lineEdit.clear()
    	self.lineEdit.setText(str(fnum * fnum))

    def button_square_root(self):
    	fnumber = self.lineEdit.text()
    	global fnum
    	fnum = float(fnumber)
    	self.lineEdit.clear()
    	self.lineEdit.setText(str(math.sqrt(fnum)))

    def button_clear(self):
    	self.lineEdit.clear()
    	global math_function
    	math_function = ""

    def button_equal(self):
    	snum = self.lineEdit.text()
    	self.lineEdit.clear()

    	if math_function == "":
    		self.lineEdit.setText(str(snum))

    	if math_function == "addition":
    		self.lineEdit.setText(str(fnum + float(snum)))

    	if math_function == "subtraction":
    		self.lineEdit.setText(str(fnum - float(snum)))

    	if math_function == "multiplication":
    		self.lineEdit.setText(str(fnum * float(snum)))

    	if math_function == "division":
    		self.lineEdit.setText(str(fnum / float(snum)))