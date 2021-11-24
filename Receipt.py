from Validator import Validator
import json


class Receipt:
    def __init__(self,
                 _id, _recipient_name, _recipient_iban, _bank, _payment_type, _amount, _payment_datetime):
        self._id = _id
        self._recipient_name = _recipient_name
        self._recipient_iban = _recipient_iban
        self._bank = _bank
        self._payment_type = _payment_type
        self._amount = _amount
        self._payment_datetime = _payment_datetime


    def __str__(self):
        string = ""
        for attr, values in vars(self).items():
            string += str(attr) + ": " + str(values) + "\n"

        return string

    @Validator.check_obj
    def edit(self):
        for attr, values in vars(self).items():
            if attr == "_id":
                continue
            setattr(self, attr, input(attr + " = "))


    @classmethod
    def read_json(cls, line):
        flight_object = Receipt(**json.loads(line))
        return flight_object

    def data_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def get_id(self):
        return self._id

    def get_recipient_name(self):
        return self._recipient_name

    def get_recipient_iban(self):
        return self._recipient_iban

    def get_bank(self):
        return self._bank

    def get_payment_type(self):
        return self._payment_type

    def get_amount(self):
        return self._amount

    def get_arrival_time(self):
        return self._payment_datetime

    @Validator.check_positive
    def set_id(self, id_num):
        self._id = id_num

    @Validator.check_name
    def set_recipient_name(self, text):
        self._recipient_name = text

    @Validator.check_name
    def set_recipient_iban(self, text):
        self._recipient_iban = text

    @Validator.check_bank
    def set_bank(self, text):
        self._bank = text

    @Validator.check_paymant_type
    def set_payment_type(self, text):
        self._payment_type = text

    @Validator.check_positive
    def set_amount(self, text):
        self._amount = text

    @Validator.check_time
    def set_payment_datetime(self, text):
        self._payment_datetime = text

