import os
import sys
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.figsize'] = (20.0, 16.0)

import flopy
import flopy.utils.binaryfile as bf

# mf6 
pth = os.path.join('.')

# mf6 parent
hnoflo = -999.
headfile = os.path.join(pth, 'parent.output.hds')
headobj = bf.HeadFile(headfile, precision='double')
phead6 = headobj.get_data(kstpkper=(0, 0))
phead6 = np.ma.masked_where(phead6 == hnoflo, phead6)
gmin = phead6.min()
gmax = phead6.max()
nlayp, nrowp, ncolp = phead6.shape
print('Parent nlay, nrow, ncol: ({}, {}, {})'.format(nlayp, nrowp, ncolp))

# mf6 child
hnoflo = -333.
headfile = os.path.join(pth, 'child.output.hds')
headobj = bf.HeadFile(headfile, precision='double')
chead6 = headobj.get_data(kstpkper=(0, 0))
chead6 = np.ma.masked_where(chead6 == hnoflo, chead6)
gmin = min(gmin, phead6.min())
gmax = max(gmax, phead6.max())
nlayc, nrowc, ncolc = chead6.shape
print('Child nlay, nrow, ncol: ({}, {}, {})'.format(nlayc, nrowc, ncolc))

# mflgr 
pth = os.path.join('.', 'mflgr')

# mf6 parent
hnoflo = -999.
headfile = os.path.join(pth, 'testLgr_3d_parent.hed')
headobj = bf.HeadFile(headfile, precision='double')
pheadlgr = headobj.get_data(kstpkper=(0, 0))
pheadlgr = np.ma.masked_where(pheadlgr == hnoflo, pheadlgr)
gmin = min(gmin, pheadlgr.min())
gmax = max(gmax, pheadlgr.max())

# mf6 child
hnoflo = -333.
headfile = os.path.join(pth, 'testLgr_3d_child.hed')
headobj = bf.HeadFile(headfile, precision='double')
cheadlgr = headobj.get_data(kstpkper=(0, 0))
cheadlgr = np.ma.masked_where(cheadlgr == hnoflo, cheadlgr)
gmin = min(gmin, cheadlgr.min())
gmax = max(gmax, cheadlgr.max())

print('mf6 parent head min/max:', phead6.min(), phead6.max())
print('mf6 child head min/max:', chead6.min(), chead6.max())
print('mflgr parent head min/max:', pheadlgr.min(), pheadlgr.max())
print('mflgr child head min/max:', cheadlgr.min(), cheadlgr.max())

pextent = (0, ncolp * 1500., 0, nrowp * 1200.)
cextent = (2 * 1500., 4 * 1500., 3 * 1200., 5 * 1200.)
print('pextent', pextent)
print('cextent', cextent)

iplot = 1
ilay = 0
#mf5 heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
plt.imshow(chead6[ilay, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 Layer {}'.format(ilay + 1))
iplot += 1

#mflgr heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
plt.imshow(cheadlgr[ilay, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MFLGR Layer {}'.format(ilay + 1))
iplot += 1

#difference heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :] - pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent)
plt.imshow(chead6[ilay, :, :] - cheadlgr[ilay, :, :], interpolation='nearest', extent=cextent)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 - MFLGR Layer {}'.format(ilay + 1))
iplot += 1

ilay = 1
#mf5 heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
plt.imshow(chead6[ilay, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 Layer {}'.format(ilay + 1))
iplot += 1

#mflgr heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
plt.imshow(cheadlgr[4, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MFLGR Layer {}'.format(ilay + 1))
iplot += 1

#difference heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :] - pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent)
plt.imshow(chead6[4, :, :] - cheadlgr[4, :, :], interpolation='nearest', extent=cextent)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 - MFLGR Layer {}'.format(ilay + 1))
iplot += 1

ilay = 2
#mf5 heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
#plt.imshow(chead6[ilay, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 Layer {}'.format(ilay + 1))
iplot += 1

#mflgr heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent, vmin=gmin, vmax=gmax)
#plt.imshow(cheadlgr[ilay, :, :], interpolation='nearest', extent=cextent, vmin=gmin, vmax=gmax)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MFLGR Layer {}'.format(ilay + 1))
iplot += 1

#difference heads
plt.subplot(3, 3, iplot, aspect='equal')
plt.imshow(phead6[ilay, :, :] - pheadlgr[ilay, :, :], interpolation='nearest', extent=pextent)
#plt.imshow(chead6[ilay, :, :] - cheadlgr[ilay, :, :], interpolation='nearest', extent=cextent)
plt.gca().set_xlim(pextent[0], pextent[1])
plt.gca().set_ylim(pextent[2], pextent[3])
plt.colorbar(shrink=0.5)
plt.title('MF 6 - MFLGR Layer {}'.format(ilay + 1))
iplot += 1



fname = 'postprocess.png'
print('saving results to {}'.format(fname))
plt.savefig(fname)
