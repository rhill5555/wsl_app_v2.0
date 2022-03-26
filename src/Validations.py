# This file contains validatinos that I would want to do in real time in my app
# For example I'd want to check that items that should be numbers do not have other characters
# Or I may want to check that a break name entered does not already exist

# Class for checking that something is a number
import datetime


class NumCheck():
    def __init__(self, input_num: str):
        self.input_num = input_num

    def int_check(self):
        try:
            # print(f"I'm checking for an integer.")
            if self.input_num == '':
                self.input_num = 0
            int(self.input_num)
            # print(f"It's an integer.")
            # print(f"I've adjusted the type to int.")
            return self.input_num
        except:
            print(f"It's not an integer.")
            raise ValueError

    def float_check(self):
        try:
            # print(f"I'm checking for an integer.")
            if self.input_num == '':
                self.input_num = 0
            float(self.input_num)
            # print(f"It's an integer.")
            # print(f"I've adjusted the type to int.")
            return self.input_num
        except:
            print(f"It's not an integer.")
            raise ValueError

    def year_check(self):
        if not self.input_num == '':
            if len(self.input_num) == 4:
                self.int_check()
            else:
                print("First Season must be a year in form YYYY")
                raise ValueError


# Class for checking that dates were entered in correct format
class DateCheck():
    # def __init__(self, input_dt: str):
    #     self.input_dt = input_dt

    def date_check(self, input_dt: str):
        try:
            if input_dt == '':
                input_dt = '1900-01-01'
            else:
                dt_string = input_dt
                dt_format = '%m/%d/%Y'
                output_dt = datetime.datetime.strptime(dt_string, dt_format)
                return output_dt
        except:
            print(f"Date format should be %m/%d/%Y")
            return "Invalid Date"



