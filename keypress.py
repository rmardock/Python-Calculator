from PyQt5 import QtCore, QtWidgets
from standard_ui_functions import *
class KeypressModule():
    def standard_keypress_event(self, event):
        if(event.key() == QtCore.Qt.Key.Key_0):
            #StandardButtonFunctions.button0_click
            print("0")
        elif(event.key() == QtCore.Qt.Key.Key_1):
            #StandardButtonFunctions.button1_click
            print("1")