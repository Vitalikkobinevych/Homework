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

        self.object_validation()

    def __str__(self):
        string = ""
        for attr, values in vars(self).items():
            string += str(attr) + ": " + str(values) + "\n"

        return string

    def edit(self):
        id = self._id
        for attr, values in vars(self).items():
            setattr(self, attr, input(attr + " = "))

        setattr(self, "_id", id)

        self.object_validation()

    def object_validation(self):
        Validator.check_positive(self._id)
        Validator.check_name(self._recipient_name)
        Validator.check_name(self._recipient_iban)
        Validator.check_bank(self._bank)
        Validator.check_paymant_type(self._payment_type)
        Validator.check_positive(self._amount)
        Validator.check_time(self._payment_datetime)


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

    def set_recipient_name(self, text):
        self._recipient_name = text

    def set_recipient_iban(self, text):
        self._recipient_iban = text

    def set_bank(self, text):
        self._bank = text

    def set_payment_type(self, text):
        self._payment_type = text

    def set_amount(self, text):
        self._amount = text

    def set_payment_datetime(self, text):
        self._payment_datetime = text
