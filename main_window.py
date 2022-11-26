from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from modes import CalculatorMode
from calc_core import CurrentNumber
from standard_ui_functions import StandardButtonFunctions
from style_module import StyleUtility
from keypress import KeypressModule
import keyboard
import sys
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(410, 590)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Close button
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(365, 0, 45, 40))
        self.button_close.setObjectName("button_close")
        
        # Minimize button
        self.button_min = QtWidgets.QPushButton(self.centralwidget)
        self.button_min.setGeometry(QtCore.QRect(320, 0, 45, 40))
        self.button_min.setObjectName("button_min")
        
        # Title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(5, 5, 315, 35))
        self.title.setObjectName("title")
        self.title.setFont(QtGui.QFont("Arial", 18))

        # Number 0 button
        self.button_number_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_0.setGeometry(QtCore.QRect(5, 385, 100, 100))
        self.button_number_0.setObjectName("button_number_0")

        # Number 1 button
        self.button_number_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_1.setGeometry(QtCore.QRect(5, 285, 100, 100))
        self.button_number_1.setObjectName("button_number_1")
        
        # Number 2 button
        self.button_number_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_2.setGeometry(QtCore.QRect(105, 285, 100, 100))
        self.button_number_2.setObjectName("button_number_2")
        
        # Number 3 button
        self.button_number_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_3.setGeometry(QtCore.QRect(205, 285, 100, 100))
        self.button_number_3.setObjectName("button_number_3")

        # Number 4 button
        self.button_number_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_4.setGeometry(QtCore.QRect(5, 185, 100, 100))
        self.button_number_4.setObjectName("button_number_4")
        
        # Number 5 button
        self.button_number_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_5.setGeometry(QtCore.QRect(105, 185, 100, 100))
        self.button_number_5.setObjectName("button_number_5")
        
        # Number 6 button
        self.button_number_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_6.setGeometry(QtCore.QRect(205, 185, 100, 100))
        self.button_number_6.setObjectName("button_number_6")

        # Number 7 button
        self.button_number_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_7.setGeometry(QtCore.QRect(5, 85, 100, 100))
        self.button_number_7.setObjectName("button_number_7")

        # Number 8 button
        self.button_number_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_8.setGeometry(QtCore.QRect(105, 85, 100, 100))
        self.button_number_8.setObjectName("button_number_8")

        # Number 9 button
        self.button_number_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_number_9.setGeometry(QtCore.QRect(205, 85, 100, 100))
        self.button_number_9.setObjectName("button_number_9")
        
        # Period button
        self.button_period = QtWidgets.QPushButton(self.centralwidget)
        self.button_period.setGeometry(QtCore.QRect(105, 485, 100, 100))
        self.button_period.setObjectName("button_period")
        
        # Add button
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(105, 385, 100, 100))
        self.button_add.setObjectName("button_add")
        
        # Subtract button
        self.button_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.button_subtract.setGeometry(QtCore.QRect(205, 385, 100, 100))
        self.button_subtract.setObjectName("button_subtract")
        
        # Multiply button
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiply.setGeometry(QtCore.QRect(305, 285, 100, 100))
        self.button_multiply.setObjectName("button_multiply")
        
        # Divide button
        self.button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.button_divide.setGeometry(QtCore.QRect(305, 385, 100, 100))
        self.button_divide.setObjectName("button_divide")
        
        # Square button (x²)
        self.button_square = QtWidgets.QPushButton(self.centralwidget)
        self.button_square.setGeometry(QtCore.QRect(305, 185, 100, 100))
        self.button_square.setObjectName("button_square")

        # Square root button
        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.button_sqrt.setGeometry(QtCore.QRect(305, 85, 100, 100))
        self.button_sqrt.setObjectName("button_sqrt")
        
        # Clear button
        self.button_ce = QtWidgets.QPushButton(self.centralwidget)
        self.button_ce.setGeometry(QtCore.QRect(5, 485, 100, 100))
        self.button_ce.setObjectName("button_ce")

        # Equals button
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setGeometry(QtCore.QRect(205, 485, 200, 100))
        self.button_equals.setObjectName("button_equals")

        # Line edit for calculator number display
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(5, 45, 295, 35))
        self.display.setObjectName("display")
        self.display.setReadOnly(True)

        # Combo box for switching calculator modes
        self.mode_switch = QtWidgets.QComboBox(self.centralwidget)
        self.mode_switch.setGeometry(QtCore.QRect(305, 45, 100, 35))
        self.mode_switch.setObjectName("mode_switch")
        self.mode_switch.addItem("Standard")
        self.mode_switch.addItem("Binary")

        # Set centralwidget
        self.setCentralWidget(self.centralwidget)
        
        # Retranslate UI
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # Assign function for when comboBox selection is changed
        self.mode_switch.currentTextChanged.connect(lambda: self.change_mode(self.mode_switch.currentText()))
        # Initialize UI button connections
        self.init_ui()
        # Enable mouse events
        QtWidgets.QWidget.setEnabled(self, True)

    # Mouse press event handler
    def mousePressEvent(self, event):
        self.is_pressed = True
        self.start_pos = self.mapToGlobal(event.pos())
        
    # Mouse movement event handler
    def mouseMoveEvent(self, event):
        if(self.is_pressed):
            self.end_pos = self.mapToGlobal(event.pos())
            self.delta = self.mapToGlobal(self.end_pos - self.start_pos)
            self.setGeometry(self.delta.x(), self.delta.y(), self.width(), self.height())
            self.start_pos = self.end_pos
           
    # Mouse release event handler 
    def mouseReleaseEvent(self, event):
        self.is_pressed = False
        
    # Function for detecting keypresses
    def keyboardEventReceived(self, event):
        # If key is pressed
        if(event.event_type == 'down'):
            KeypressModule.keypress_handler(self, event)
            
    # Function to set all text values on UI 
    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.button_close.setText(_translate("MainWindow", "X"))
        self.button_min.setText(_translate("MainWindow", "-"))
        self.title.setText(_translate("MainWindow", "Calculator"))
        self.button_number_0.setText(_translate("MainWindow", "0"))
        self.button_number_1.setText(_translate("MainWindow", "1"))
        self.button_number_2.setText(_translate("MainWindow", "2"))
        self.button_number_3.setText(_translate("MainWindow", "3"))
        self.button_number_4.setText(_translate("MainWindow", "4"))
        self.button_number_5.setText(_translate("MainWindow", "5"))
        self.button_number_6.setText(_translate("MainWindow", "6"))
        self.button_number_7.setText(_translate("MainWindow", "7"))
        self.button_number_8.setText(_translate("MainWindow", "8"))
        self.button_number_9.setText(_translate("MainWindow", "9"))
        self.button_period.setText(_translate("MainWindow", "."))  
        self.button_add.setText(_translate("MainWindow", "+"))  
        self.button_subtract.setText(_translate("MainWindow", "-"))
        self.button_multiply.setText(_translate("MainWindow", "*"))
        self.button_divide.setText(_translate("MainWindow", "÷"))
        self.button_square.setText(_translate("MainWindow", "x²"))
        self.button_sqrt.setText(_translate("MainWindow", "√"))
        self.button_ce.setText(_translate("MainWindow", "CE"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.mode_switch.setItemText(0, _translate("MainWindow", "Standard"))
        self.mode_switch.setItemText(1, _translate("MainWindow", "Binary"))
        
    # Function to initialize UI
    def init_ui(self):
        # Instantiate CurrentNumber object
        # This object will hold the values and complete calculations for the calculator
        cn = CurrentNumber()
        # Set calculator mode
        cn.set_mode("standard")
        
        self.mode = cn.get_mode()
    	# On-Click Number Buttons
        self.button_number_0.clicked.connect(lambda: StandardButtonFunctions.button0_click(self, cn))
        self.button_number_1.clicked.connect(lambda: StandardButtonFunctions.button1_click(self, cn))
        self.button_number_2.clicked.connect(lambda: StandardButtonFunctions.button2_click(self, cn))
        self.button_number_3.clicked.connect(lambda: StandardButtonFunctions.button3_click(self, cn))
        self.button_number_4.clicked.connect(lambda: StandardButtonFunctions.button4_click(self, cn))
        self.button_number_5.clicked.connect(lambda: StandardButtonFunctions.button5_click(self, cn))
        self.button_number_6.clicked.connect(lambda: StandardButtonFunctions.button6_click(self, cn))
        self.button_number_7.clicked.connect(lambda: StandardButtonFunctions.button7_click(self, cn))
        self.button_number_8.clicked.connect(lambda: StandardButtonFunctions.button8_click(self, cn))
        self.button_number_9.clicked.connect(lambda: StandardButtonFunctions.button9_click(self, cn))

    	# On-Click Function Buttons
        self.button_period.clicked.connect(lambda: StandardButtonFunctions.button_period_click(self, cn))
        self.button_add.clicked.connect(lambda: StandardButtonFunctions.button_add_click(self, cn))
        self.button_subtract.clicked.connect(lambda: StandardButtonFunctions.button_subtract_click(self, cn))
        self.button_multiply.clicked.connect(lambda: StandardButtonFunctions.button_multiply_click(self, cn))
        self.button_divide.clicked.connect(lambda: StandardButtonFunctions.button_divide_click(self, cn))
        self.button_square.clicked.connect(lambda: StandardButtonFunctions.button_squared(self, cn))
        self.button_sqrt.clicked.connect(lambda: StandardButtonFunctions.button_square_root(self, cn))
        self.button_ce.clicked.connect(lambda: StandardButtonFunctions.button_clear(self, cn))
        self.button_equals.clicked.connect(lambda: StandardButtonFunctions.button_equal(self, cn))    

        # Title Bar Buttons
        self.button_close.clicked.connect(lambda: self.close_app(self))
        self.button_min.clicked.connect(lambda: self.min_app(self))
        
        # Keyboard listener
        self.hook = keyboard.on_press(self.keyboardEventReceived)
        
        # Style Utility
        StyleUtility.window_element_color(self)
        StyleUtility.standard_button_color(self)
        StyleUtility.font_style(self)
    
    # Function for closing application
    def close_app(self, MainWindow):
        MainWindow.close()
    
    # Function for minimizing application
    def min_app(self, MainWindow):
        MainWindow.showMinimized()
    
    # Setter function for MainWindow
    # def set_mw(self, mw):
    #     self.mw = mw
    
    # # Getter function for MainWindow  
    # def get_mw(self):
    #     return self.mw
    
    # Function to reconnect button signals for different comboBox selections in mode_switch
    def change_mode(self, text):
        # If changing to standard mode
        if(text == "Standard"):
            CalculatorMode.standard_calc_connection_utility(self)
        # If changing to binary mode
        if(text == "Binary"):
            CalculatorMode.binary_calc_connection_utility(self)