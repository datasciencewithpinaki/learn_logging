import numpy as np
import datetime
import re



def get_numbers(*args):
    nbrs = np.asarray([nbr for nbr in args])
    return nbrs

def add_nbrs(*args):
    nbrs = get_numbers(*args)
    return np.sum(nbrs)

def multiply_nbrs(*args):
    nbrs = get_numbers(*args)
    return np.product(nbrs)

def subtract_nbrs(*args):
    nbrs = get_numbers(*args)
    nbrs_neg = np.asarray([nbr*-1 if idx>0 else nbr for idx, nbr in enumerate(nbrs)])
    return np.sum(nbrs_neg)

def divide_nbrs(*args):
    nbrs = get_numbers(*args)
    nbrs_neg = np.asarray([1/nbr if idx>0 else nbr for idx, nbr in enumerate(nbrs)])
    return np.product(nbrs_neg)

if __name__ == '__main__':

    mysum = add_nbrs(30,10,2,5)
    print(f"res from sum is: {mysum}")

    myprod = multiply_nbrs(5,4,3)
    print(f"res from product is: {myprod}")

    mysubt = subtract_nbrs(35,5,3)
    print(f"res from subtraction is: {mysubt}")

    mydiv = divide_nbrs(350,5,10)
    print(f"res from division is: {mydiv:.0f}")