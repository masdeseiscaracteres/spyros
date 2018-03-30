"""This package is divided into two modules be of different types:

Modules
-------
- numba: fast implementations requiring numba
- others: implementations using other libraries

References
----------
1. Bottleneck functions : http://berkeleyanalytics.com/bottleneck/reference.html
2. Numpy functions : https://docs.scipy.org/doc/numpy/reference/routines.math.html
3. Pandas nanops module functions (for many, it is just a wrapper of
  bottleneck) : https://github.com/pandas-dev/pandas/blob/master/pandas/core/nanops.py
4. Scipy.stats operations for unmasked and masked arrays :
  - https://docs.scipy.org/doc/scipy-0.16.0/reference/stats.html#statistical-functions
  - https://docs.scipy.org/doc/scipy-0.16.1/reference/stats.mstats.html
5. Some less common functionalities are implemented as Numpy's ufuncs in the scipy.special module:
  - https://docs.scipy.org/doc/scipy/reference/special.html

Those that are not available out there, require custom implementations:
Take a look at
- https://docs.scipy.org/doc/numpy-1.13.0/reference/ufuncs.html#methods
- http://numba.pydata.org/numba-doc/latest/user/vectorize.html
- and the numba module in this package
to learn how to write your own numpy ufunc's.
"""

from .numba import *
from .others import *
