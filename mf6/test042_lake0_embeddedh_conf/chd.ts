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
  NAME    chdh_1
  METHODS linear
END ATTRIBUTES

BEGIN TIMESERIES
#   time  chdh_1
     0.0     4.0
    10.0     9.0
    20.0     4.0
    20.0     5.0
    30.0     0.0
END TIMESERIES
