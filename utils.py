import numpy as np
import datetime 
from functools import wraps

import logging 

# setting up logging
path_log_op = '/Users/prb000j/Library/CloudStorage/OneDrive-WalmartInc/Python Learn Projects/Python Projects/learn_logging/log_output/'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(message)s')

file_handler = logging.FileHandler(path_log_op + 'log_utils.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# utility functions start here 

# wrapper func to return execution time for a function call
def time_it(func, *args, **kwargs):
    @wraps(func)
    def call_func(*args, **kwargs):
        st_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        exec_time = (end_time - st_time).total_seconds()
        logger.info(f"{str(func.__name__)} :: run time: {exec_time:.4f} seconds")
        return result
    return call_func


if __name__ == '__main__':

    @time_it
    def test_sum_of_squares_till(max_val:int=5):
        nbrs = np.asarray([nbr**2 for nbr in range(max_val + 1)])
        return np.sum(nbrs)
    
    res = test_sum_of_squares_till(5)
    logger.debug(f"res for sum of squares: {res}")