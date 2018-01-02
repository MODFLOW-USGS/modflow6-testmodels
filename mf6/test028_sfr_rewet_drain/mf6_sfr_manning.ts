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
  NAME    man1     man2
  METHODS stepwise stepwise
END ATTRIBUTES

BEGIN TIMESERIES
#   time    man1     man2
     0.0    0.05      0.1
   600.0    0.05      0.1
END TIMESERIES
