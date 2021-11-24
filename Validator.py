import datetime
import os
import enums


class Validator:

    @staticmethod
    def input_positive(message):
        while True:
            try:
                num = int(input(message))
                if num <= 0:
                    print("This number cannot reach negative values: " + str(num))
                    continue
                return num
            except ValueError:
                print("It is not an integer")

    @staticmethod
    def input_file(message):
        while True:
            path = input(message)
            if os.path.isfile(path) and path.endswith(".txt"):
                return path
            else:
                print("File name is incorrect")
                continue

    @staticmethod
    def check_positive(func):
        def func_wrapper(self, num):
            if num.isdigit():
                if int(num) <= 0:
                    print("This number cannot reach negative values: " + str(num))
                func(self, num)

        return func_wrapper

    @staticmethod
    def check_float(func):
        def func_wrapper(self, num):
            try:
                num = round(float(num), 2)
            except ValueError:
                print('This number can be float type')
            func(self, num)

        return func_wrapper

    @staticmethod
    def check_name(func):
        def func_wrapper(self, string):
            if not all(x.isalpha() or x.isspace() for x in string):
                print("name should only contain alphabetic symbols")
            func(self, string)

        return func_wrapper

    @staticmethod
    def check_time(func):
        def func_wrapper(self, date):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d ')
            except ValueError:
                print("Incorrect data format. Correct is YYYY-MM-DD ")
            func(self, date)

        return func_wrapper

    @staticmethod
    def check_file_existence(func):
        def func_wrapper(self, path):
            if not (os.path.isfile(path) and path.endswith(".txt")):
                print("File does not exist")
                path = Validator.input_file("Input correct file name: ")

            func(self, path)

        return func_wrapper

    @staticmethod
    def check_bank(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enums.bank.__members__:
                print("That bank " + info + " is not listed in Enum")
            func(self, info)

        return func_wrapper

    @staticmethod
    def check_paymant_type(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enums.paymant_type.__members__:
                print("That paymant type " + info + " is not listed in Enum")
            func(self, info)

        return func_wrapper


    @staticmethod
    def check_obj(func):
        def func_wrapper(self):
            func(self)

            self.set_id(self.get_id())
            self.set_recipient_name(self.get_recipient_name())
            self.set_recipient_iban(self.get_recipient_iban())
            self.set_bank(self.get_bank())
            self.set_payment_type(self.get_payment_type())
            self.set_amount(self.get_amount())
            self.set_payment_datetime(self.get_payment_datetime())


        return func_wrapper