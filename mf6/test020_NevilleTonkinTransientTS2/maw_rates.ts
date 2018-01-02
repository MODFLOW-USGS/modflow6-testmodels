# The ATTRIBUTES block is required.
# Number of names on NAME line indicates 
#     number of time series to be created.
# NAME must precede METHOD (or METHODS).
# Either METHOD or METHODS must be specified, but not both.
# If METHOD is specified, all time series in file
#     share the same method (either LINEAR or STEPWISE).
# IF METHODS is specified, a method is specified for each time series.
#
BEGIN ATTRIBUTES
  NAME    mawq1    mawq2    aux1   aux2
  METHODS stepwise stepwise linear linear
END ATTRIBUTES

BEGIN TIMESERIES
#   time   mawq1   mawq2   aux1  aux2
     0.0  -1767.  -2767.    100  -200
    30.0  -1767.  -2767.   -100   200
END TIMESERIES
