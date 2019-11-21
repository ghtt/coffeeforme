import csv
from os import mkdir
from os.path import join, exists
from time import time
from helpers import Strings
from helpers import log_action


class Order:

    def __init__(self):
        self.entries = []

    @log_action("Order")
    def save_bill(self):

        if not exists(Strings.BILLS_FOLDER.value):
            mkdir(Strings.BILLS_FOLDER.value)

        bill_filename = join(Strings.BILLS_FOLDER.value, u"bill_{time}.csv".format(time=time()))
        with open(bill_filename, 'w') as file:
            fieldnames = [u'beverage_type', u'beverage_price', u'additional_ingredients']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.entries:
                writer.writerow(entry.__dict__)

    @log_action("Order")
    def add_entry(self, **kwargs):
        entry = Entry(**kwargs)
        self.entries.append(entry)


class Entry:

    def __init__(self, beverage_type, beverage_price, additional_ingredients):
        self.beverage_type = beverage_type
        self.beverage_price = beverage_price
        self.additional_ingredients = additional_ingredients

    def __str__(self):
        return str(self.__dict__)
