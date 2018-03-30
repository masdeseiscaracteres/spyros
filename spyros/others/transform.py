import numpy as np
import bottleneck as bn
import pandas.core.nanops as nanops

__all__ = ['gt', 'ge', 'lt', 'le', 'eq', 'ne',
           'mov_sum', 'mov_mean', 'mov_std', 'mov_var',
           'mov_min', 'mov_max', 'mov_argmin',
           'mov_argmax', 'mov_median', 'mov_rank',
           'cum_sum', 'cum_prod']

# Binary element-wise functions
# Signature: (),()->()
gt = nanops.nangt
ge = nanops.nange
lt = nanops.nanlt
le = nanops.nanle
eq = nanops.naneq
ne = nanops.nanne

# Moving window functions
mov_sum = bn.move_sum
mov_mean = bn.move_mean
mov_std = bn.move_std
mov_var = bn.move_var
mov_min = bn.move_min,
mov_max = bn.move_max
mov_argmin = bn.move_argmin
mov_argmax = bn.move_argmax
mov_median = bn.move_median
mov_rank = bn.move_rank

# Expanding window functions
cum_sum = np.nancumsum
cum_prod = np.nancumprod