import os
import numpy as np

def analwt(b1, b2, Lx, V):
    rd = (V/Lx)
    idx = rd > 1.
    rd[idx] = 1.
    h = np.sqrt(b1**2 - rd * (b1**2 - b2**2))
    idx = V > Lx
    h[idx] = b2
    return h

ncol, nrow = 151, 151
dx = 1072.9
bot = 0.
h1 = 6.1
h2 = 3.05


xmax = dx * float(ncol)
ymax = dx * float(nrow)
print xmax, ymax

#--x
x = np.arange(0, xmax, dx) + dx/2.
#--y
y = np.arange(0, ymax, dx) + dx/2.
#
print(x.shape, y.shape)
#--mesh grid object
X, Y = np.meshgrid(x, y[::-1])

xc, yc = X[75, 75], Y[75, 75]

R = np.sqrt((X-xc)**2 + (Y-yc)**2)
print R.min(), R.max()

h = analwt(h1, h2, xmax/2., R)

np.savetxt('ihead.ref', h, delimiter=' ')
np.savetxt(os.path.join('..', 'ihead.ref'), h, delimiter=' ')

K = 1000.
b = h2 - bot
cond = K * b * dx / (0.5 * dx)

Ko = np.ones((nrow, ncol), np.float) * K
np.savetxt('K.ref', Ko, delimiter=' ')
np.savetxt(os.path.join('..', 'K.ref'), Ko, delimiter=' ')

ib = np.zeros((nrow, ncol), dtype=np.int)
ib[0, :] = 1
ib[-1, :] = 1
ib[:, 0] = 1
ib[:, -1] = 1
    
f = open('ghb.ref', 'w')
f2 = open(os.path.join('..', 'ghb.ref'), 'w')
    
for i in range(nrow):
    for j in range(ncol):
        if ib[i, j] > 0:
            line = '{:10d} {:10d} {:10d} {:10.4g} {:10.4g}\n'.format(1, i+1, j+1, h2, cond)
            f.write(line)
            f2.write(line)

f.close()
f2.close()