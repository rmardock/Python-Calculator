class StyleUtility():
    # Function for assigning colors to buttons on startup and for going back to standard mode
    def standard_button_color(self):
        self.button_number_0.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_1.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_2.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_3.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_4.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_5.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_6.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_7.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_8.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_number_9.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_period.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_add.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_subtract.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_multiply.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_divide.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_square.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_sqrt.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_ce.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
        self.button_equals.setStyleSheet("QPushButton{background-color:rgb(25,25,25);color:white;border:none;}QPushButton::hover{background-color:#8300FF;}")
    
    def window_element_color(self):
        # Window button and line edit styling
        self.button_close.setStyleSheet("QPushButton{background-color:rgb(53,53,53);color:white;border:none;}QPushButton::hover{background-color:rgb(25,25,25);}")
        self.button_min.setStyleSheet("QPushButton{background-color:rgb(53,53,53);color:white;border:none;}QPushButton::hover{background-color:rgb(25,25,25);}")
        self.display.setStyleSheet("QLineEdit{background-color:rgb(25,25,25);border:none;}")
        self.mode_switch.setStyleSheet("QComboBox{background-color:rgb(25,25,25);border:none;color:white;}")
        
    # Function to change color of disabled buttons
    def binary_button_color(self):
            self.button_number_2.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_3.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_4.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_5.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_6.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_7.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_8.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_number_9.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_period.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_square.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")
            self.button_sqrt.setStyleSheet("QPushButton{background-color:black;color:rgb(188,188,188);}")