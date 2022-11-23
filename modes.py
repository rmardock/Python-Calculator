from PyQt5 import QtCore, QtWidgets
from connection_utility import ConnectionTools, SignalUtility
from calc_core import CurrentNumber
from standard_ui_functions import StandardButtonFunctions
from bin_ui_functions import BinaryButtonFunctions
class CalculatorMode():
    
    def standard_calc_connection_utility(mw):
        # Instantiate CurrentNumber object
        cn = CurrentNumber()
        # Assign calculator mode
        cn.set_mode("standard")
        # Change color of enabled buttons
        StandardButtonFunctions.standard_button_color(mw)
        # Number button connections
        ConnectionTools.reconnect(mw.button_number_0.clicked, lambda: StandardButtonFunctions.button0_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_1.clicked, lambda: StandardButtonFunctions.button1_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_2.clicked, lambda: StandardButtonFunctions.button2_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_3.clicked, lambda: StandardButtonFunctions.button3_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_4.clicked, lambda: StandardButtonFunctions.button4_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_5.clicked, lambda: StandardButtonFunctions.button5_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_6.clicked, lambda: StandardButtonFunctions.button6_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_7.clicked, lambda: StandardButtonFunctions.button7_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_8.clicked, lambda: StandardButtonFunctions.button8_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_9.clicked, lambda: StandardButtonFunctions.button9_click(mw, cn))
        # Function button connections
        ConnectionTools.reconnect(mw.button_period.clicked, lambda: StandardButtonFunctions.button_period_click(mw, cn))
        ConnectionTools.reconnect(mw.button_add.clicked, lambda: StandardButtonFunctions.button_add_click(mw, cn))
        ConnectionTools.reconnect(mw.button_subtract.clicked, lambda: StandardButtonFunctions.button_subtract_click(mw, cn))
        ConnectionTools.reconnect(mw.button_multiply.clicked, lambda: StandardButtonFunctions.button_multiply_click(mw, cn))
        ConnectionTools.reconnect(mw.button_divide.clicked, lambda: StandardButtonFunctions.button_divide_click(mw, cn))
        ConnectionTools.reconnect(mw.button_square.clicked, lambda: StandardButtonFunctions.button_squared(mw, cn))
        ConnectionTools.reconnect(mw.button_sqrt.clicked, lambda: StandardButtonFunctions.button_square_root(mw, cn))
        ConnectionTools.reconnect(mw.button_ce.clicked, lambda: StandardButtonFunctions.button_clear(mw, cn))
        ConnectionTools.reconnect(mw.button_equals.clicked, lambda: StandardButtonFunctions.button_equal(mw, cn))
        
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
        
        SignalUtility.enable_button(mw.button_multiply)
        SignalUtility.enable_button(mw.button_divide)
        
        # Clear current number
        CurrentNumber.clear_current_number(cn)
        # Set display to current number
        mw.display.setText(str(CurrentNumber.get_current_number(cn)))
        
    def binary_calc_connection_utility(mw):
        # Instantiate CurrentNumber object
        cn = CurrentNumber()
        # Set calculator mode
        cn.set_mode("binary")
        # Change color of disabled buttons
        BinaryButtonFunctions.binary_button_color(mw)
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
        # Disable multiplication and division buttons
        SignalUtility.disable_button(mw.button_multiply)
        SignalUtility.disable_button(mw.button_divide)
        # Reconnect buttons for binary mode
        ConnectionTools.reconnect(mw.button_number_0.clicked, lambda: BinaryButtonFunctions.button_bin_0(mw, cn), lambda: StandardButtonFunctions.button0_click(mw, cn))
        ConnectionTools.reconnect(mw.button_number_1.clicked, lambda: BinaryButtonFunctions.button_bin_1(mw, cn), lambda: StandardButtonFunctions.button1_click(mw, cn))
        ConnectionTools.reconnect(mw.button_add.clicked, lambda: BinaryButtonFunctions.button_binary_add(mw, cn), lambda: StandardButtonFunctions.button_add_click(mw, cn))
        ConnectionTools.reconnect(mw.button_subtract.clicked, lambda: BinaryButtonFunctions.button_binary_subtract(mw, cn), lambda: StandardButtonFunctions.button_subtract_click(mw, cn))
        # Multiplication and division have been disabled for the binary calculator mode
        # These operations are more complex and will take more work to complete
        #ConnectionTools.reconnect(mw.button_multiply.clicked, lambda: BinaryButtonFunctions.button_binary_multiply(mw, cn), lambda: StandardButtonFunctions.button_multiply_click(mw, cn))
        #ConnectionTools.reconnect(mw.button_divide.clicked, lambda: BinaryButtonFunctions.button_binary_divide(mw, cn), lambda: StandardButtonFunctions.button_divide_click(mw, cn))
        ConnectionTools.reconnect(mw.button_equals.clicked, lambda: BinaryButtonFunctions.button_bin_equals(mw, cn), lambda: StandardButtonFunctions.button_equal(mw, cn))