import numpy as np
from numba import guvectorize

_REDUCE_NUMPY_SIGNATURE = '(n)->()'

_NUMBA_SIG_ARGFUNCS = ['void(int32[:],float32[:])',
                           'void(int64[:],float64[:])',
                           'void(float32[:],float32[:])',
                           'void(float64[:],float64[:])']


@guvectorize(_NUMBA_SIG_ARGFUNCS, _REDUCE_NUMPY_SIGNATURE, nopython=True)
def argfirst(a, out):
    out[0] = np.nan
    for i in range(len(a)):
        if not np.isnan(a[i]):
            out[0] = i
            break


@guvectorize(_NUMBA_SIG_ARGFUNCS, _REDUCE_NUMPY_SIGNATURE, nopython=True)
def arglast(a, out):
    out[0] = np.nan
    for i in range(len(a) - 1, -1, -1):
        if not np.isnan(a[i]):
            out[0] = i
            break
