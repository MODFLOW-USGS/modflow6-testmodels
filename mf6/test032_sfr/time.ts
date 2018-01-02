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
  NAME    conc    temp
  METHODS stepwise stepwise
END ATTRIBUTES

BEGIN TIMESERIES
#   time   conc   temp
     0.0     0.    10.
    30.0     0.    10.
END TIMESERIES
