import os
import numpy as np
import flopy

ml = flopy.modflow.Modflow.load('l2a_2k.nam', version='mf2005', verbose=True)

delx = ml.dis.delr.array
dely = ml.dis.delc.array

# get data from the lst file
f = open('l2a_2k.lst', 'r')

for line in f:
    if 'LAYER #    ROW #    COLUMN #   LAKE #  INTERFACE TYPE  LAKEBED LEAKANCE' in line:
        break

cdata = []
for idx, line in enumerate(f):
    if (len(line.strip()) < 1):
        break
    cdata.append(line)
f.close()

tpth = 'mf5.conn.dat'
f = open(tpth, 'w')
for c in cdata:
    f.write(c)
f.close()

dir_dict = {1:'HORIZONTAL', 
            2:'HORIZONTAL',
            3:'HORIZONTAL', 
            4:'HORIZONTAL', 
            6:'VERTICAL'}

dtype = [('k', np.int), ('i', np.int), ('j', np.int),
         ('lake', np.int), ('itype', np.int),
         ('bedleak', np.float)]

cdata = np.loadtxt(tpth, dtype=dtype)
cdata['k'] -= 1
cdata['i'] -= 1
cdata['j'] -= 1


nlakes = np.unique(cdata['lake'])
print(nlakes)
lake_cnt = {}
for lake in nlakes:
    lake_cnt[lake] = 0
print(lake_cnt)

dtype2 = [('iconn', np.int), ('belev', np.float), ('telev', np.float),
          ('dx', np.float), ('width', np.float)]
cdata2 = np.zeros((cdata.shape[0]), dtype=dtype2)

# fill cdata2
for idx in range(cdata.shape[0]):
    k = cdata['k'][idx]
    i = cdata['i'][idx]
    j = cdata['j'][idx]
    ilak = cdata['lake'][idx]
    lake_cnt[ilak] += 1 
    itype = cdata['itype'][idx]
    cdir = dir_dict[itype]
    belev = 0.
    telev = 0.
    if cdir == 'HORIZONTAL':
        if itype == 1 or itype == 2:
            dx = 0.5 * delx[j]
            width = dely[i]
        elif itype == 3 or itype == 4:
            dx = 0.5 * dely[i]
            width = delx[j]
    else:
        dx = 0.
        width = 0.
    cdata2['iconn'][idx] = lake_cnt[ilak]
    cdata2['belev'][idx] = belev
    cdata2['telev'][idx] = telev
    cdata2['dx'][idx] = dx
    cdata2['width'][idx] = width

# 
tpth = 'mf6.conn.dat'
f = open(tpth, 'w')

f.write('begin lakes\n')
c = '#          lakeno      strt  lakeconn  boundname'
f.write('{}\n'.format(c))
for lake in nlakes:
    f.write('  LAKE {:10d}{:10.3g}{:10d}  LAKE_{:03d}\n'.format(lake, 130., lake_cnt[lake], lake))
f.write('end lakes\n\n')


f.write('begin lake_connections\n')
# header
##   lakeno iconn layer row column       ctype bedleak belev telev  dx width
c = '#          lakeno     iconn     layer       row    ' + \
    'column          ctype    bedleak     belev     '+ \
    'telev        dx     width'
f.write('{}\n'.format(c))
# data
for idx in range(cdata.shape[0]):
    itype = cdata['itype'][idx]
    c = '  LAKE'
    c += ' {:10d}{:10d}{:10d}{:10d}{:10d}'.format(cdata['lake'][idx],
                                                  cdata2['iconn'][idx],
                                                  cdata['k'][idx]+1,
                                                  cdata['i'][idx]+1,
                                                  cdata['j'][idx]+1)
    c += '{:>15s} '.format(dir_dict[itype])
    c += '{:10.3g}'.format(cdata['bedleak'][idx])
    c += '{:10.3g}'.format(cdata2['belev'][idx])
    c += '{:10.3g}'.format(cdata2['telev'][idx])
    c += '{:10.3g}'.format(cdata2['dx'][idx])
    c += '{:10.3g}'.format(cdata2['width'][idx])
    f.write('{}\n'.format(c))
f.write('end lake_connections\n\n')


f.close()

