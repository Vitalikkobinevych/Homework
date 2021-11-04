import datetime as dt
import sys


class Validation():

    def check_car(text: str, lst: list):
        if text not in lst:
            raise ValueError
        else:
            return text

    def check_id(num):
        if int(num) <= 0:
            print("This number cannot reach negative values: " + str(num))
        return num

    def check_name(string):
        if all(x.isalpha() or x.isspace() for x in string):
            return string
        else:
            print("name should only contain alphabetic symbols")


    def check_price(num):
        if int(num) <= 0:
            print("This number cannot reach negative values: " + str(num))
        return num

    def validate_date(x):
        if isinstance(x, str):
            try:
                return dt.datetime.strptime(x, '%Y-%m-%d')
            except:
                print(f'Wrong {x}!')
            sys.exit()
        return x
