from __future__ import print_function
import os
import pandas as pd
from helpers import user
from helpers import Strings
from helpers import log_action
from helpers.menu import Menu
from helpers.order import Order
from pandas import DataFrame, read_csv


class Session:

    def __init__(self, user_info):
        self.user = user.factory.get_user(*user_info)
        self.order = Order()
        self.logger = None
        self.menu = Menu(self.order, self.user)

    @log_action("Session")
    def save_result(self):
        if self.user.is_enough_rights():
            session_result = {
                u"Seller name": self.user.name,
                u"Number of sales": len(self.order.entries),
                u"Total values": sum((entry.beverage_price for entry in self.order.entries))
            }

            result = session_result
            df = DataFrame(result, index=[0])
            if os.path.exists(Strings.HISTORY_FILE.value):
                result = self.add_result_in_history(session_result)
                df = DataFrame(result)

            with open(Strings.HISTORY_FILE.value, 'w') as f:
                df.to_csv(f, index=False)

        else:
            history = self.get_history()
            if history:
                history = DataFrame(history)
                total = pd.Series(history.sum())
                total[u"Seller name"] = u"Total:"
                history = history.append(total, ignore_index=True)
                print(history)
            else:
                print(u"History is empty")

    @staticmethod
    @log_action("Session")
    def get_history():
        try:
            history = read_csv(Strings.HISTORY_FILE.value)
            history = history.to_dict('r')
            return history
        except IOError as e:
            print(u"{} doesn't exist".format(Strings.HISTORY_FILE.value))
            return None

    @log_action("Session")
    def add_result_in_history(self, result):
        history = self.get_history()
        is_found = False

        for row_number in range(len(history)):
            if history[row_number][u"Seller name"].lower() == self.user.name.lower():
                history[row_number][u"Number of sales"] += result[u"Number of sales"]
                history[row_number][u"Total values"] += result[u"Total values"]
                is_found = True
                break

        if is_found:
            return history
        else:
            history.extend([result])
            return history
