from main import CarReservation
from os.path import exists
import sys

class Collection:
    def init(self, file_name):
        self.car_reservation = []
        self.read(file_name)
        self.file_name = file_name

    def read(self, file_name):
        if exists(file_name):
            with open(file_name, 'r') as f:
                for i, line in enumerate(f):
                    print(f'reading line {i} ...', end=' ')
                    row = line.split()
                    try:
                        item = CarReservation(*row)
                        self.car_reservation.append(item)
                    except:
                        pass
        else:
            sys.exit(f'{file_name} does not exists')