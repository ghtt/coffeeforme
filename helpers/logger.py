import logging
import time
from helpers import Strings


def log_action(instance):
    def wrapper(func):
        def wrapper_func(*args, **kwargs):
            # create logger
            logging.basicConfig(filename=Strings.LOGGER_FILE.value, level=logging.INFO)
            logger = logging.getLogger("CoffeeForMe")

            # start function
            result = func(*args, **kwargs)

            # log info
            log_time = time.asctime(time.gmtime(time.time()))
            logger.info(
                "{0} {1}.{2} starts with {3} and exits with result={4}".format(log_time, instance, func.__name__,
                                                                               (args, kwargs), result))

            return result

        return wrapper_func

    return wrapper
