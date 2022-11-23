from PyQt5 import QtCore, QtWidgets
from calc_core import CurrentNumber

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
            
    def standard_button_color(self):
        self.button_number_2.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_3.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_4.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_5.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_6.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_7.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_8.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_number_9.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_period.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_square.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_sqrt.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_multiply.setStyleSheet("background-color:rgb(53,53,53);color:white")
        self.button_divide.setStyleSheet("background-color:rgb(53,53,53);color:white")