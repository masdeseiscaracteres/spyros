import numpy as np
import bottleneck as bn
import pandas.core.nanops as nanops

__all__ = ['nangt', 'nange', 'lt', 'le', 'eq', 'ne',
           'mov_sum', 'mov_mean', 'mov_std', 'mov_var',
           'mov_min', 'mov_max', 'mov_argmin',
           'mov_argmax', 'mov_median', 'mov_rank',
           'cum_sum', 'cum_prod']

# Binary element-wise functions
# Signature: (),()->()
nangt = nanops.nangt
nange = nanops.nange
nanlt = nanops.nanlt
nanle = nanops.nanle
naneq = nanops.naneq
nanne = nanops.nanne

# Moving window functions
movsum = bn.move_sum
movmean = bn.move_mean
movstd = bn.move_std
movvar = bn.move_var
movmin = bn.move_min
movmax = bn.move_max
movargmin = bn.move_argmin
movargmax = bn.move_argmax
movmedian = bn.move_median
movrank = bn.move_rank

# Expanding window functions
cumsum = np.cumsum
cumprod = np.cumprod
nancumsum = np.nancumsum
nancumprod = np.nancumprod
cummax = np.cummax
cummin = np.cummin
nancummax = np.fmax.accumulate
nancummin = np.fmin.accumulate

