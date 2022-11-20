import math

# Class to hold and compute calculator values  
class CurrentNumber():
    
    # Class Constructor
    def __init__(self):
        # Variable for current number stored in calculator
        self.current_number = 0
        # Variable for last recorded keypress
        self.last_keypress = None
        # Variable for math function
        self.function = ""
        # Variable for first number in calculation
        self.fnum = 0
        # Variable for second number in calculation
        self.snum = 0
    
    # Getter Function for current number
    def get_current_number(self):
        return self.current_number
    
    # Function for number entry using the onscreen number keys
    def number_entry(self, number):
        # If last keypress was "." button
        if(self.last_keypress == "."):
            current_number_str = str(self.current_number)
            # Remove the zero automatically added to float number (ex: 123.0)
            current_number_str = current_number_str[:-1]
        # If last keypress was a number or "." was pressed earlier, keep number as is
        else:
            current_number_str = str(self.current_number)
        new_number_str = current_number_str + number
        self.last_keypress = number
        # If number is type float, reassign to float (if "." has been pressed)
        if(type(self.current_number) is float):
            self.current_number = float(new_number_str)
        # If "." button has not been pressed, keep as int
        # Casting to float here will complicate number entry for integers
        else:
            self.current_number = int(new_number_str)        
    
    # Function for period (".") entry
    def period_entry(self):
        # If "." is already present in number, do nothing
        if("." in str(self.current_number)):
            pass
        else:
            self.last_keypress = "."
            current_number_str = str(self.current_number) + "."
            self.current_number = float(current_number_str)
    
    # Function to reset current number and last keypress values 
    def clear_current_number(self):
        self.current_number = 0
        self.last_keypress = None
        
    # Function for addition, subtraction, multiplication, and division
    def basic_math(self, math_function):
        # Assign math function used (+,-, *, /) to self.function variable
        self.function = math_function
        # If self.fnum is unset
        if(self.fnum == 0):
            self.fnum = self.current_number
        # If self.fnum is set
        else:
            self.snum = self.current_number
            if(math_function == "add"):
                self.fnum = self.fnum + self.snum
            elif(math_function == "subtract"):
                self.fnum = self.fnum - self.snum
            elif(math_function == "multiply"):
                self.fnum = self.fnum * self.snum
            elif(math_function == "divide"):
                self.fnum = self.fnum / self.snum
            self.current_number = self.fnum

    # Function for squaring number
    def square(self):
        self.current_number = self.current_number * self.current_number
        self.function = ""
    # Function to find square root of number
    def square_root(self):
        self.current_number = math.sqrt(self.current_number)
        self.function = ""
        
    # Function for equals button in calculator
    def equals(self):
        # If no function operation buttons have been pressed (+, -, *, /), do nothing
        if(self.function == ""):
            pass
        # If function operation button has been pressed (+, -, *, /)
        else:
            self.snum = self.current_number
            if(self.function == "add"):
                self.current_number = self.fnum + self.snum
            elif(self.function == "subtract"):
                self.current_number = self.fnum - self.snum
            elif(self.function == "multiply"):
                self.current_number = self.fnum * self.snum
            elif(self.function == "divide"):
                self.current_number = self.fnum / self.snum
            
            # Reset self.fnum and self.snum variables
            self.fnum = 0
            self.snum = 0