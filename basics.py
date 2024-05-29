import numpy as np
import datetime
import re

from utils import time_it

import logging

# setting up logging
path_log_op = '/Users/p****i/project_folder/learn_logging/log_output/'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(funcName)s: %(message)s')

file_handler = logging.FileHandler(path_log_op + 'log_basics.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# code starts here

def check_basic_logging():
    '''
    check basic logging
    '''
    first_name = 'Pinaki'
    last_name = 'Brahma'
    domain = 'walmart.com'
    logger.debug(f"email: {first_name}.{last_name}@{domain}")

def get_numbers(*args):
    '''
    convert all the inputs into an array
    checks if input is not a number
    '''
    nbrs = np.asarray([nbr for nbr in args if type(nbr) not in [str, list, set, dict]])
    return nbrs

@time_it
def add_nbrs(*args):
    '''
    add two or more numbers
    '''
    nbrs = get_numbers(*args)
    return np.sum(nbrs)

@time_it
def multiply_nbrs(*args):
    '''
    multiply two or more numbers
    '''
    nbrs = get_numbers(*args)
    return np.product(nbrs)

@time_it
def subtract_nbrs(*args):
    '''
    subtract two or more numbers from the first
    '''
    nbrs = get_numbers(*args)
    nbrs_neg = np.asarray([nbr*-1 if idx>0 else nbr for idx, nbr in enumerate(nbrs)])
    return np.sum(nbrs_neg)

@time_it
def divide_nbrs(*args):
    '''
    divide two or more numbers from the first
    '''
    nbrs = get_numbers(*args)
    nbrs_neg = np.asarray([1/nbr if idx>0 else nbr for idx, nbr in enumerate(nbrs)])
    return np.product(nbrs_neg)

if __name__ == '__main__':

    def test_main():
        mysum = add_nbrs(30,10,2,5)
        logger.debug(f"res from sum is: {mysum}")

        myprod = multiply_nbrs(5,4,3)
        logger.debug(f"res from product is: {myprod}")

        mysubt = subtract_nbrs(35,5,3)
        logger.debug(f"res from subtraction is: {mysubt}")

        mydiv = divide_nbrs(350,5,10)
        logger.debug(f"res from division is: {mydiv:.0f}")

        check_basic_logging()

    test_main()
