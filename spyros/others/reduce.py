import numpy as np
import bottleneck as bn
import pandas.core.nanops as nanops

__all__ = ['mean', 'var', 'std', 'sum', 'prod', 'max', 'min',
           'nanmean', 'nanvar', 'nanstd', 'nansum', 'nanprod',
           'nanmax', 'nanmin', 'nanargmax', 'nanargmin', 'nanmedian', 'ss',
           'nanany', 'nanall', 'nansem', 'nanskew', 'nankurt', 'nanpercentile']

# Unary reducing functions
# Signature: roughly (n)->()
mean = np.mean
var = np.var
std = np.std
sum = np.sum
prod = np.prod
max = np.max
min = np.min

nanmean = bn.nanmean
nanvar = bn.nanvar
nanstd = bn.nanstd
nansum = bn.nansum
nanprod = nanops.nanprod
nanmax = bn.nanmax
nanmin = bn.nanmin
nanargmax = bn.nanargmax
nanargmin = bn.nanargmin
nanmedian = bn.nanmedian
ss = bn.ss
nanany = bn.anynan
nanall = bn.allnan
nansem = nanops.nansem
nanskew = nanops.nanskew
nankurt = nanops.nankurt
nanpercentile = np.nanpercentile

# Binary reducing functions
# Signature: roughly (n),(n)->()
nancov = nanops.nancov
nancorr = nanops.nancorr


