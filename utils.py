import numpy as np
import datetime 
from functools import wraps

# wrapper func to return execution time for a function call
def time_it(func, *args, **kwargs):
    @wraps(func)
    def call_func(*args, **kwargs):
        st_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        exec_time = (end_time - st_time).total_seconds()
        print(f"{str(func.__name__)} :: run time: {exec_time:.4f} seconds")
        return result
    return call_func


if __name__ == '__main__':

    @time_it
    def test_sum_of_squares_till(max_val:int=5):
        nbrs = np.asarray([nbr**2 for nbr in range(max_val + 1)])
        return np.sum(nbrs)
    
    res = test_sum_of_squares_till(5)
    print(f"res for sum of squares: {res}")