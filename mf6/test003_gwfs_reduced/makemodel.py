import sys
pth = 'D:/users/langevin/ModelDevelopment/flopy'
pth = '../../../../flopy'
if pth not in sys.path:
    sys.path.append(pth)

import numpy as np
from flopy.modflow import *

nlay=1
nrow=10
ncol=10
dx=1.
dy=1.
top=1.
botm=[0]
ibound=np.ones((nlay,nrow,ncol),dtype=np.int)
ibound[:,:,0]=-1
ibound[:,:,-1]=-1
strt=np.ones((nlay,nrow,ncol),dtype=np.float)
strt[:,:,0]=10.
strt[:,:,-1]=5.


mf = Modflow('model')
dis = ModflowDis(mf, nlay, nrow, ncol, nper=1, delr=dx, delc=dy, laycbd=0, 
                    top=top, botm=botm, perlen=1.0, nstp=1, 
                    tsmult=1.0, steady=True)
bas = ModflowBas(mf, ibound, strt)
lpf = ModflowLpf(mf, hk=1., vka=1.)
#pcg = ModflowPcg(mf, hclose=1.e-6)
oc = ModflowOc(mf)
#wel = ModflowWel(mf, iwelcb=50, layer_row_column_Q=[lrc_Q])
mf.write_input()