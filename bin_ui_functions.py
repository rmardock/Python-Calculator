from calc_core import CurrentNumber

# Button functions for binary calculator mode
class BinaryButtonFunctions():
    # Function for 0 button 
    def button_bin_0(self, cn):
        text = "0"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        
    # Function for 1 button
    def button_bin_1(self, cn):
        text = "1"
        CurrentNumber.number_entry(cn, text)
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        
    # Function for binary addition
    def button_binary_add(self, cn):
        CurrentNumber.binary_math(cn, "add")
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary subtraction
    def button_binary_subtract(self, cn):
        CurrentNumber.binary_math(cn, "subtract")
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary multiplication
    def button_binary_multiply(self, cn):
        CurrentNumber.binary_math(cn, "multiply")
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        CurrentNumber.clear_current_number(cn)
        
    # Function for binary division
    def button_binary_divide(self, cn):
        CurrentNumber.binary_math(cn, "divide")
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
        CurrentNumber.clear_current_number(cn)
    
    # Function for clear button in binary mode
    def button_bin_ce(self, cn):
        CurrentNumber.clear_current_number(cn)
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))
    
    # Function for equals button in binary mode
    def button_bin_equals(self, cn):
        CurrentNumber.bin_equals(cn)
        self.display.setText(CurrentNumber.get_curr_bin_num(cn))