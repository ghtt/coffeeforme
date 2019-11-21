# CoffeeForMe

Commandline utility that can be used by salesman or managers of the CoffeeForMe company

## Prerequisites

What do you need to install:

1) Python 2.7.12 or 3+
2) Packages from requirements.txt

## Installing

Install Python 3+ according to the official documentation https://docs.python.org/

Install needed packages using the following command:
```
pip install -r requirements.txt
```
or
```
python -m pip install -r requirements.txt
```

## How to use

Firstly, you need to setup configuration parameters in the _config.cfg_ file: 
specify available beverages and additional ingredients types. They will be used for inputs validations

_config.cfg_ example:
    
    [default]
    beverages = coffee,tea,latte
    additional_ingredients = sugar,cream,cinnamon


Utility usage:

    usage: CoffeeForMe [-h] --username USERNAME --user_position {Salesman,Manager}
                       [--beverage_type {coffee,tea,latte}]
                       [--beverage_price BEVERAGE_PRICE]
                       [--additional_ingredients [{sugar,cream,cinnamon} [{sugar,cream,cinnamon} ...]]]
    
    optional arguments:
      -h, --help            show this help message and exit
      --username USERNAME   Input your name
      --user_position {Salesman,Manager}
                            Input your position (Salesman or Manager)
      --beverage_type {coffee,tea,latte}
                            Input beverage type
      --beverage_price BEVERAGE_PRICE
                            Input beverage price
      --additional_ingredients [{sugar,cream,cinnamon} [{sugar,cream,cinnamon} ...]]
                            Input additional beverage ingredients

Utility produces following outputs:
    
1) Saved bills are stored in *bills* folder
2) Sales history are stored in the utility's  folder with name *sales_history.csv*
3) Utility log is stored in the utility's folder with name *log.txt*