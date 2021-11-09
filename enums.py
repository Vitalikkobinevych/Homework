import enum


class bank(enum.Enum):
    privatbank = 1
    universal_bank = 2


class paymant_type(enum.Enum):
    monthly = 1
    yearly = 2