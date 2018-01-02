BEGIN ATTRIBUTES
  NAMES   rate_1   rate_2   rate_3   rate_4   rate_5
  METHODS LINEAR   LINEAR   LINEAR   STEPWISE STEPWISE
END ATTRIBUTES

BEGIN TIMESERIES
! time    rate_1   rate_2   rate_3   rate_4   rate_5
0.0       3.0E30    0.0     3.0E30    -1.0     -0.0    begin SP 1
1440.0    3.0E30   -10.0    3.0E30    -2.0     -2.0    begin SP 2
1500.0    3.0E30   -10.0    3.0E30    -4.0    3.0E30
2000.0    3.0E30   -10.0    3.0E30    -5.0    3.0E30
2880.0     -5.0    -10.0    3.0E30    -7.0     -3.0    begin SP 3
4320.0     -5.0    -10.0    -30.0    3.0E30    -4.0    begin SP 4
5760.0     -7.0    -14.0    -35.0     -9.0     -5.0    begin SP 5
7200.0    3.0E30   3.0E30   3.0E30   3.0E30   3.0E30   begin SP 6
8640.0    3.0E30   -15.0    -42.0    -12.0     -7.0    begin SP 7
9000.0     -8.0    -17.0    -45.0    -12.0     -7.0
10080.0    -9.0    3.0E30   -25.0    -14.0     -8.0    begin SP 8
11000.0   -10.0    3.0E30   -25.0    -14.0    3.0E30
11520.0   -11.0    3.0E30   -25.0    -15.0     -9.0    begin SP 9
12000.0   -12.0    3.0E30   3.0E30   -16.0    3.0E30
12500.0   -14.0    3.0E30   3.0E30   -18.0    3.0E30
12960.0   -15.0    -20.0    3.0E30   -19.0    3.0E30   begin SP 10
13000.0   3.0E30   -19.0    3.0E30   3.0E30   3.0E30
14000.0   3.0E30   -18.0    3.0E30   3.0E30   3.0E30
14400.0   3.0E30   -15.0    3.0E30   -90.0    -99.0    end SP 10
END TIMESERIES
