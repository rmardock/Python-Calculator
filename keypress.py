class KeypressModule():
    # Function for handling keyboard keypresses
    def keypress_handler(self, event):
        # If calculator is in standard or binary mode simulate button clicks based on keypresses
        if(self.mode == 'standard' or self.mode == 'binary'):
            # If '0' key is pressed on keyboard
            if(event.name == '0'):
                self.button_number_0.click()
            # If '1' key is pressed on keyboard
            elif(event.name == '1'):
                self.button_number_1.click()
            # If '+' key is pressed on keyboard
            elif(event.name == '+'):
                self.button_add.click()
            # If '-' key is pressed on keyboard
            elif(event.name == '-'):
                self.button_subtract.click()
            # If '*' key is pressed on keyboard
            elif(event.name == '*'):
                self.button_multiply.click()
            # If '/' key is pressed on keyboard
            elif(event.name == '/'):
                self.button_divide.click()
            # If 'esc' key is pressed on keyboard
            elif(event.name == 'esc'):
                self.button_ce.click()
            # If 'enter' key is pressed on keyboard
            elif(event.name == 'enter'):
                self.button_equals.click()
                
        # If calculator is in standard mode simulate button clicks based on keypresses
        if(self.mode == 'standard'):        
            # If '2' key is pressed on keyboard
            if(event.name == '2'):
                self.button_number_2.click()
            # If '3' key is pressed on keyboard
            elif(event.name == '3'):
                self.button_number_3.click()
            # If '4' key is pressed on keyboard
            elif(event.name == '4'):
                self.button_number_4.click()
            # If '5' key is pressed on keyboard
            elif(event.name == '5'):
                self.button_number_5.click()
            # If '6' key is pressed on keyboard
            elif(event.name == '6'):
                self.button_number_6.click()
            # If '7' key is pressed on keyboard
            elif(event.name == '7'):
                self.button_number_7.click()
            # If '8' key is pressed on keyboard
            elif(event.name == '8'):
                self.button_number_8.click()
            # If '9' key is pressed on keyboard
            elif(event.name == '9'):
                self.button_number_9.click()
            # If '.' key is pressed on keyboard
            elif(event.name == '.'):
                self.button_period.click()