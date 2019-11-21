from enum import Enum
from os.path import abspath, dirname, join


class Strings(Enum):
    BILLS_FOLDER = join(dirname(dirname(abspath(__file__))), u"bills")
    CONFIG_FILE = join(dirname(dirname(abspath(__file__))), u"config.cfg")
    HISTORY_FILE = join(dirname(dirname(abspath(__file__))), u"sales_history.csv")
    LOGGER_FILE = join(dirname(dirname(abspath(__file__))), u"log.txt")
