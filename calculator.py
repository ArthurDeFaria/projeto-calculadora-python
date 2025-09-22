class Calculator:
    def __init__(self):
        self.result = 0
        self.current_number = ""
        self.current_operator = ""
        self.is_new_calculation = True

    def add_digit(self, digit):
        if self.is_new_calculation:
            self.current_number = str(digit)
            self.is_new_calculation = False
        else:
            self.current_number += str(digit)

    def add_operator(self, operator):
        if self.current_number:
            self._perform_calculation()
            self.current_operator = operator
            self.is_new_calculation = True

    def _perform_calculation(self):
        try:
            num = float(self.current_number)
            if self.current_operator == "+":
                self.result += num
            elif self.current_operator == "-":
                self.result -= num
            elif self.current_operator == "*":
                self.result *= num
            elif self.current_operator == "/":
                if num == 0:
                    raise ValueError("Cannot divide by zero")
                self.result /= num
            else:
                self.result = num
            self.current_number = str(self.result)
        except (ValueError, ZeroDivisionError) as e:
            self.result = 0
            self.current_number = "Error"
        
    def equals(self):
        self._perform_calculation()
        self.current_operator = ""
        self.is_new_calculation = True
    
    def clear(self):
        self.result = 0
        self.current_number = ""
        self.current_operator = ""
        self.is_new_calculation = True

    def get_display_value(self):
        return self.current_number if self.current_number else str(self.result)