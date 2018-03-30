# New functions
cummax
cummin
fillna_holes (similar to Pandas' fillna)
find (on boolean arrays, similar to Matlab's find)

# New internals
Create automatic mov/cum-type functions from reduce-type functions at the expense of some speed

# Wrappers
Consider the application of these functions to all numpy, pandas and xarray objects by any of the following
two approaches:
- `__array__` + `__array_wrap__`/`__reduced_array_wrap__`/`__resized_array_wrap__` (monkey-patching)
- http://xarray.pydata.org/en/stable/computation.html#wrapping-custom-computation