from __future__ import print_function
from builtins import input
from consolemenu import SelectionMenu
from helpers.user import Salesman
from helpers.utils import get_available_items
from helpers import log_action


class Menu:

    YES_NO = (u"Yes", u"No")

    def __init__(self, order, user):
        self.beverage_list = get_available_items(u"beverages")
        self.additional_ingredients = get_available_items(u"additional_ingredients")
        self.order = order
        self.user = user

    @log_action("Menu")
    def get_user_choice(self, message, items):
        """Function to get user choice 
        :param message - menu header
        :param items - list of menu items
        """

        menu = self.create_menu(items, message)
        menu.show()
        menu.join()

        # selected index 
        index = menu.selected_item.get_return()
        return items[index]

    @staticmethod
    @log_action("Menu")
    def get_price(beverage):
        """Get price for beverage
        :param beverage
        :return beverage price
        """
        price = 0.0
        while True:
            try:
                price = float(input(u"You selected '{}'. Please input price: ".format(beverage)))
                break
            except ValueError:
                print(u"Please, input correct price")
                continue
        return price

    @staticmethod
    @log_action("Menu")
    def create_menu(items, message):
        """Create selection menu
        :param items - menu items
        :param message - menu header message
        :return SelectionMenu object
        """

        return SelectionMenu(items, message, show_exit_option=False, exit_option_text='')

    @log_action("Menu")
    def need_more(self, item):
        need_more = self.get_user_choice(u"Do you want to add {}?".format(item), Menu.YES_NO)
        return True if need_more == u'Yes' else False

    @log_action("Menu")
    def start(self):
        if isinstance(self.user, Salesman):
            """Start menu"""
            while self.need_more(u"beverage"):
                beverage = self.get_user_choice(u"Select beverage:", self.beverage_list)
                price = self.get_price(beverage)

                # add ingredients
                if self.additional_ingredients:
                    ingredients = []
                    while self.need_more(u"ingredient"):
                        ingredients.append(
                            self.get_user_choice(u"Select additional ingredients", self.additional_ingredients))

                # add entry to order
                self.user.add_entry(
                    order=self.order,
                    beverage_type=beverage,
                    beverage_price=price,
                    additional_ingredients=ingredients)

            # does user wanna save the bill?
            save_menu = self.get_user_choice(u"Do you want to save the bill", Menu.YES_NO)
            if save_menu == u"Yes":
                self.order.save_bill()
