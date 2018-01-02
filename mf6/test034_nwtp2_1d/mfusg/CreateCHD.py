import numpy as np

hds = np.genfromtxt('test034_nwtp2.csv', delimiter=',', names=True)

locs = np.array([[10,1,1], [11,1,1], [12,1,1], [13,1,1], [14,1,1]])

f = open('Pr2.chd', 'w')

f.write('{:10d}{:10d}\n'.format(locs.shape[0], 0))

for idx, hd in enumerate(hds['L10HEAD']):
    f.write('{:10d}{:10d}  #stress period {}\n'.format(locs.shape[0], 0, idx+1))
    for k, i, j in locs:
        f.write('{:10d}{:10d}{:10d}{:10.6f}{:10.6f}\n'.format(k, i, j, hd, hd))
        
f.close()