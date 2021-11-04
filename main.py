from Validation import Validation
from Collection import Collection
from os.path import exists
import sys

class CarReservation(Validation):
    list_of_cars = ["Audi A3", "BMW X1", "Toyota Yaris", "Volkswagen T-Roc", "Ford Fiesta", "Honda Civic",
                    "Volkswagen Golf"]



    def __init__(self, id, car, start_datetime, end_datetime, name, price):
        self._id = Validation.check_id(id)
        self.car = Validation.check_car(car, self.list_of_car)
        self.start_datetime = Validation.validate_date(start_datetime)
        self.end_datetime = Validation.validate_date(end_datetime)
        self.name = Validation.check_name(name)
        self.price = Validation.check_price(price)


    def set_id(self, value):
        self.id = value

    def get_id(self):
        return self.id

    def set_car(self, value):
        self.car = value

    def get_car(self):
        return self.car

    def set_star_datetime(self, value):
        self.start_datetime = value

    def get_start_datetime(self):
        return self.start_datetime

    def set_end_datetime(self, value):
        self.end_datetime = value

    def get_end_datetime(self):
        return self.end_datetime

    def set_name(self, value):
        self.name = value

    def get_name(self):
        return self.name

    def set_price(self, value):
        self.price = value

    def get_price(self):
        return self.price

с = Collection('Car.txt')
