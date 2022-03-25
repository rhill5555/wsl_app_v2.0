# This file contains validatinos that I would want to do in real time in my app
# For example I'd want to check that items that should be numbers do not have other characters
# Or I may want to check that a break name entered does not already exist

# Class for checking that something is a number
class NumCheck():
    def __init__(self, input_num: str):
        self.input_num = input_num

    def int_check(self, input_num: str):
        try:
            print(f"I'm checking for an integer.")
            if input_num == '':
                input_num = 0
            int(input_num)
            print(f"It's an integer.")
            print(f"I've adjusted the type to int.")
            return(input_num)
        except:
            print(f"It's not an integer.")
            return('Invalid Number')