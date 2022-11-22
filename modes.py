from PyQt5 import QtCore, QtWidgets
from connection_utility import connection_tools
from pycalc_functions import *
from ui_functions import *
class CalculatorMode(object):
    def standard_calc_connection_utility(self, mw):
        cn = CurrentNumber()
        connection_tools.reconnect(mw.button_number_0.clicked, lambda: ButtonFunctions.button0_click(mw, cn))
        connection_tools.reconnect(mw.button_number_1.clicked, lambda: ButtonFunctions.button1_click(mw, cn))
        connection_tools.reconnect(mw.button_number_2.clicked, lambda: ButtonFunctions.button2_click(mw, cn))
        connection_tools.reconnect(mw.button_number_3.clicked, lambda: ButtonFunctions.button3_click(mw, cn))
        connection_tools.reconnect(mw.button_number_4.clicked, lambda: ButtonFunctions.button4_click(mw, cn))
        connection_tools.reconnect(mw.button_number_5.clicked, lambda: ButtonFunctions.button5_click(mw, cn))
        connection_tools.reconnect(mw.button_number_6.clicked, lambda: ButtonFunctions.button6_click(mw, cn))
        connection_tools.reconnect(mw.button_number_7.clicked, lambda: ButtonFunctions.button7_click(mw, cn))
        connection_tools.reconnect(mw.button_number_8.clicked, lambda: ButtonFunctions.button8_click(mw, cn))
        connection_tools.reconnect(mw.button_number_9.clicked, lambda: ButtonFunctions.button9_click(mw, cn))
        
        connection_tools.reconnect(mw.button_period.clicked, lambda: ButtonFunctions.button_period_click(mw, cn))
        connection_tools.reconnect(mw.button_add.clicked, lambda: ButtonFunctions.button_add_click(mw, cn))
        connection_tools.reconnect(mw.button_subtract.clicked, lambda: ButtonFunctions.button_subtract_click(mw, cn))
        connection_tools.reconnect(mw.button_multiply.clicked, lambda: ButtonFunctions.button_multiply_click(mw, cn))
        connection_tools.reconnect(mw.button_divide.clicked, lambda: ButtonFunctions.button_divide_click(mw, cn))
        connection_tools.reconnect(mw.button_square.clicked, lambda: ButtonFunctions.button_squared(mw, cn))
        connection_tools.reconnect(mw.button_sqrt.clicked, lambda: ButtonFunctions.button_square_root(mw, cn))
        connection_tools.reconnect(mw.button_ce.clicked, lambda: ButtonFunctions.button_clear(mw, cn))
        connection_tools.reconnect(mw.button_equals.clicked, lambda: ButtonFunctions.button_equal(mw, cn))
        
    def programming_calc_connection_utility(mw):
        #cn = CurrentNumber()
        connection_tools.reconnect(mw.button_number_0.clicked, lambda: ButtonFunctions.test_function(mw))