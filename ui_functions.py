from PyQt5 import QtCore, QtWidgets
from pycalc_functions import *

# Button functions 
class StandardButtonFunctions():
    def button0_click(self, cn):
        text = "0"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button1_click(self, cn):
        text = "1"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button2_click(self, cn):
        text = "2"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button3_click(self, cn):
        text = "3"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button4_click(self, cn):
        text = "4"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button5_click(self, cn):
        text = "5"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button6_click(self, cn):
        text = "6"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button7_click(self, cn):
        text = "7"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button8_click(self, cn):
        text = "8"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button9_click(self, cn):
        text = "9"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button_period_click(self, cn):
        CurrentNumber.period_entry(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button_add_click(self, cn):
        CurrentNumber.basic_math(cn, "add")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_subtract_click(self, cn):
        CurrentNumber.basic_math(cn, "subtract")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_multiply_click(self, cn):
        CurrentNumber.basic_math(cn, "multiply")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_divide_click(self, cn):
        CurrentNumber.basic_math(cn, "divide")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)

    def button_squared(self, cn):
        CurrentNumber.square(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button_square_root(self, cn):
        CurrentNumber.square_root(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button_clear(self, cn):
        CurrentNumber.clear_current_number(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))

    def button_equal(self, cn):
        CurrentNumber.equals(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
    
class BinaryButtonFunctions():
    # Function for binary addition
    def button_binary_add(self, cn):
        CurrentNumber.binary_math(cn, "add")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary subtraction
    def button_binary_subtract(self, cn):
        CurrentNumber.binary_math(cn, "subtract")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary multiplication
    def button_binary_multiply(self, cn):
        CurrentNumber.binary_math(cn, "multiply")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary division
    def button_binary_divide(self, cn):
        CurrentNumber.binary_math(cn, "divide")
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
        CurrentNumber.clear_current_number(cn)
    
    # Function for equals button in binary mode
    def button_bin_equals(self, cn):
        CurrentNumber.bin_equals(cn)
        self.display.setText(str(CurrentNumber.get_current_number(cn)))
    
    # Function for testing button reconnections
    def test_function(self):
        print("Test Successful!")
        self.display.setText("Test Successful!")
        
class SignalUtility():
    # Function to enable buttons
    def enable_button(button):
        button.setEnabled(True)
    
    # Function to disable buttons
    def disable_button(button):
        button.setEnabled(False)
            