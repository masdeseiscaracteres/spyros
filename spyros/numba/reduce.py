import numpy as np
from .ufunc import reduce as numba_reduce

__all__ = ['argfirst', 'arglast']


def argfirst(arr, axis=0):
    arr = np.moveaxis(arr, axis, -1)  # transpose may be faster
    return numba_reduce.argfirst(arr)


def arglast(arr, axis=0):
    arr = np.moveaxis(arr, axis, -1)  # transpose may be faster
    return numba_reduce.arglast(arr)