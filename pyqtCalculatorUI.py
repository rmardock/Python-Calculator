from PyQt5 import QtCore, QtWidgets
from pycalc_functions import *

class Ui_MainWindow(object):
	# UI Initialization Function
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
        self.pushButton_14.setGeometry(QtCore.QRect(180, 370, 171, 71))
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

        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(90, 370, 81, 71))
        self.pushButton_19.setObjectName("pushButton_19")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function to set all text values on UI
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
        self.pushButton_19.setText(_translate("MainWindow", "."))

    # Function to connect on-click button functions to buttons on GUI
    # MainWindow parameter is required for QtWidgets.QMainWindow() -> removing the parameter will break the program

    def initUI(self, MainWindow):
        # Instantiate CurrentNumber object
        # This object will hold the values and complete calculations for the calculator
        cn = CurrentNumber()
    	# On-Click Number Buttons
        self.pushButton_13.clicked.connect(lambda: self.button0_click(cn))
        self.pushButton_9.clicked.connect(lambda: self.button1_click(cn))
        self.pushButton_10.clicked.connect(lambda: self.button2_click(cn))
        self.pushButton_11.clicked.connect(lambda: self.button3_click(cn))
        self.pushButton_4.clicked.connect(lambda: self.button4_click(cn))
        self.pushButton_5.clicked.connect(lambda: self.button5_click(cn))
        self.pushButton_6.clicked.connect(lambda: self.button6_click(cn))
        self.pushButton.clicked.connect(lambda: self.button7_click(cn))
        self.pushButton_2.clicked.connect(lambda: self.button8_click(cn))
        self.pushButton_3.clicked.connect(lambda: self.button9_click(cn))

    	# On-Click Function Buttons
        self.pushButton_15.clicked.connect(lambda: self.button_add_click(cn))
        self.pushButton_16.clicked.connect(lambda: self.button_subtract_click(cn))
        self.pushButton_12.clicked.connect(lambda: self.button_multiply_click(cn))
        self.pushButton_17.clicked.connect(lambda: self.button_divide_click(cn))
        self.pushButton_7.clicked.connect(lambda: self.button_square_root(cn))
        self.pushButton_8.clicked.connect(lambda: self.button_squared(cn))
        self.pushButton_14.clicked.connect(lambda: self.button_equal(cn))
        self.pushButton_18.clicked.connect(lambda: self.button_clear(cn))
        self.pushButton_19.clicked.connect(lambda: self.button_period_click(cn))

        # Global variable initialization
        global math_function
        math_function = ""	
    
    # Button functions 
    def button0_click(self, cn):
        text = "0"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button1_click(self, cn):
        text = "1"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button2_click(self, cn):
        text = "2"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button3_click(self, cn):
        text = "3"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button4_click(self, cn):
        text = "4"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button5_click(self, cn):
        text = "5"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button6_click(self, cn):
        text = "6"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button7_click(self, cn):
        text = "7"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button8_click(self, cn):
        text = "8"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button9_click(self, cn):
        text = "9"
        CurrentNumber.number_entry(cn, text)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button_period_click(self, cn):
        CurrentNumber.period_entry(cn)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button_add_click(self, cn):
        CurrentNumber.basic_math(cn, "add")
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_subtract_click(self, cn):
        CurrentNumber.basic_math(cn, "subtract")
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_multiply_click(self, cn):
        CurrentNumber.basic_math(cn, "multiply")
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_divide_click(self, cn):
        CurrentNumber.basic_math(cn, "divide")
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_squared(self, cn):
        CurrentNumber.square(cn)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button_square_root(self, cn):
        CurrentNumber.square_root(cn)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button_clear(self, cn):
        CurrentNumber.clear_current_number(cn)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))

    def button_equal(self, cn):
        CurrentNumber.equals(cn)
        self.lineEdit.setText(str(CurrentNumber.get_current_number(cn)))
# ><----->< New functions to implement ><----->< #
    # Decimal to binary 
    # Binary to decimal 
    # Re-Build interface entirely to accommodate basic and programmer functions similar to Windows 10 Calculator and any future functionality 
        # Use QComboBox for swapping between calculator modes 
    # Implement bin to hex, hex to bin, dec to hex, hex to dec
    # Add functionality for logarithmic functions
    # Build functions for sin, cos, tan
