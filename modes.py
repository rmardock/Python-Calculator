from PyQt5 import QtCore, QtWidgets
from connection_utility import connection_tools
from pycalc_functions import *
from ui_functions import *
class CalculatorMode():
    def standard_calc_connection_utility(mw):
        cn = CurrentNumber()
        cn.set_mode("standard")
        connection_tools.reconnect(mw.button_number_0.clicked, lambda: StandardButtonFunctions.button0_click(mw, cn))
        connection_tools.reconnect(mw.button_number_1.clicked, lambda: StandardButtonFunctions.button1_click(mw, cn))
        connection_tools.reconnect(mw.button_number_2.clicked, lambda: StandardButtonFunctions.button2_click(mw, cn))
        connection_tools.reconnect(mw.button_number_3.clicked, lambda: StandardButtonFunctions.button3_click(mw, cn))
        connection_tools.reconnect(mw.button_number_4.clicked, lambda: StandardButtonFunctions.button4_click(mw, cn))
        connection_tools.reconnect(mw.button_number_5.clicked, lambda: StandardButtonFunctions.button5_click(mw, cn))
        connection_tools.reconnect(mw.button_number_6.clicked, lambda: StandardButtonFunctions.button6_click(mw, cn))
        connection_tools.reconnect(mw.button_number_7.clicked, lambda: StandardButtonFunctions.button7_click(mw, cn))
        connection_tools.reconnect(mw.button_number_8.clicked, lambda: StandardButtonFunctions.button8_click(mw, cn))
        connection_tools.reconnect(mw.button_number_9.clicked, lambda: StandardButtonFunctions.button9_click(mw, cn))
        
        connection_tools.reconnect(mw.button_period.clicked, lambda: StandardButtonFunctions.button_period_click(mw, cn))
        connection_tools.reconnect(mw.button_add.clicked, lambda: StandardButtonFunctions.button_add_click(mw, cn))
        connection_tools.reconnect(mw.button_subtract.clicked, lambda: StandardButtonFunctions.button_subtract_click(mw, cn))
        connection_tools.reconnect(mw.button_multiply.clicked, lambda: StandardButtonFunctions.button_multiply_click(mw, cn))
        connection_tools.reconnect(mw.button_divide.clicked, lambda: StandardButtonFunctions.button_divide_click(mw, cn))
        connection_tools.reconnect(mw.button_square.clicked, lambda: StandardButtonFunctions.button_squared(mw, cn))
        connection_tools.reconnect(mw.button_sqrt.clicked, lambda: StandardButtonFunctions.button_square_root(mw, cn))
        connection_tools.reconnect(mw.button_ce.clicked, lambda: StandardButtonFunctions.button_clear(mw, cn))
        connection_tools.reconnect(mw.button_equals.clicked, lambda: StandardButtonFunctions.button_equal(mw, cn))
        
        # Enable disabled buttons
        SignalUtility.enable_button(mw.button_number_2)
        SignalUtility.enable_button(mw.button_number_3)
        SignalUtility.enable_button(mw.button_number_4)
        SignalUtility.enable_button(mw.button_number_5)
        SignalUtility.enable_button(mw.button_number_6)
        SignalUtility.enable_button(mw.button_number_7)
        SignalUtility.enable_button(mw.button_number_8)
        SignalUtility.enable_button(mw.button_number_9)
        SignalUtility.enable_button(mw.button_period)
        SignalUtility.enable_button(mw.button_square)
        SignalUtility.enable_button(mw.button_sqrt)
        
    def binary_calc_connection_utility(mw):
        cn = CurrentNumber()
        cn.set_mode("binary")
        
        # Disable unnecessary buttons for binary mode
        SignalUtility.disable_button(mw.button_number_2)
        SignalUtility.disable_button(mw.button_number_3)
        SignalUtility.disable_button(mw.button_number_4)
        SignalUtility.disable_button(mw.button_number_5)
        SignalUtility.disable_button(mw.button_number_6)
        SignalUtility.disable_button(mw.button_number_7)
        SignalUtility.disable_button(mw.button_number_8)
        SignalUtility.disable_button(mw.button_number_9)
        SignalUtility.disable_button(mw.button_period)
        SignalUtility.disable_button(mw.button_square)
        SignalUtility.disable_button(mw.button_sqrt)
        # Reconnect buttons for binary mode
        connection_tools.reconnect(mw.button_add.clicked, lambda: BinaryButtonFunctions.button_binary_add(mw, cn), lambda: StandardButtonFunctions.button_add_click(mw, cn))
        connection_tools.reconnect(mw.button_subtract.clicked, lambda: BinaryButtonFunctions.button_binary_subtract(mw, cn), lambda: StandardButtonFunctions.button_subtract_click(mw, cn))
        connection_tools.reconnect(mw.button_multiply.clicked, lambda: BinaryButtonFunctions.button_binary_multiply(mw, cn), lambda: StandardButtonFunctions.button_multiply_click(mw, cn))
        connection_tools.reconnect(mw.button_divide.clicked, lambda: BinaryButtonFunctions.button_binary_divide(mw, cn), lambda: StandardButtonFunctions.button_divide_click(mw, cn))
        connection_tools.reconnect(mw.button_equals.clicked, lambda: BinaryButtonFunctions.button_bin_equals(mw, cn), lambda: StandardButtonFunctions.button_equal(mw, cn))