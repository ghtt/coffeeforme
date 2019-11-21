import configparser
from helpers import Strings, log_action


@log_action("utils")
def get_available_entries(config_file=Strings.CONFIG_FILE.value):
    """Parse config file to get default values
    :param config_file - name of a config file
    :return ConfigParser object with data
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


@log_action("utils")
def get_available_items(item_name):
    try:
        items = get_available_entries()["default"][item_name].split(",")
        items = [item.strip() for item in items]
        return items
    except KeyError:
        print("Config file doesn't have required values or doesn't exist")
        quit()
