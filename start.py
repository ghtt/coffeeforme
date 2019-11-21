from __future__ import print_function
import argparse
from helpers import log_action
from helpers.session import Session
from helpers.utils import get_available_items

@log_action("main")
def parse_arguments():
    """Parse input arguments"""

    def check_salesman_args(input_args, *args):
        result = True
        for arg in args:
            if input_args.__dict__[arg] is None:
                print("{} is missed".format(arg))
                if result:
                    result = False
        return result

    parser = argparse.ArgumentParser(u"CoffeeForMe")
    parser.add_argument(
        u"--username",
        type=str,
        required=True,
        help="Input your name"
    )
    parser.add_argument(
        u"--user_position",
        type=str,
        required=True,
        choices=[u'Salesman', u'Manager'],
        help=u"Input your position (Salesman or Manager)"
    )
    parser.add_argument(
        u"--beverage_type",
        required=False,
        type=str,
        choices=get_available_items(u"beverages"),
        help="Input beverage type"
    )
    parser.add_argument(
        u"--beverage_price",
        required=False,
        type=float,
        help="Input beverage price"
    )
    parser.add_argument(
        u"--additional_ingredients",
        nargs="*",
        required=False,
        type=str,
        choices=get_available_items(u"additional_ingredients"),
        help=u"Input additional beverage ingredients"
    )

    arguments = parser.parse_args()
    if arguments.user_position == u'Salesman':
        if not check_salesman_args(arguments, u"beverage_type", u"beverage_price"):
            parser.error(u"Some arguments are missed")

    return arguments


if __name__ == u"__main__":
    parameters = parse_arguments()
    current_session = Session((parameters.username, parameters.user_position))

    if u'add_entry' in dir(current_session.user):
        current_session.user.add_entry(
            order=current_session.order,
            beverage_type=parameters.beverage_type,
            beverage_price=parameters.beverage_price,
            additional_ingredients=parameters.additional_ingredients)

    current_session.menu.start()
    current_session.save_result()
