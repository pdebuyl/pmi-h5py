import pmi
from mpi4py import MPI
pmi.exec_('import test_pmi_mod')
import numpy as np
import h5py

class MyTestLocal(object):
    def __init__(self, filename, n):
        self.filename = filename
        self.f = h5py.File('myllfile.h5', 'w', driver='mpio', comm=MPI.COMM_WORLD)
        self.n = n
        self.data = np.random.random(n)
    def do(self):
        print MPI.COMM_WORLD.rank, self.filename
    def show(self):
        print MPI.COMM_WORLD.rank, self.data
    def fill(self):
        self.f.create_dataset('ds1', dtype=self.data.dtype, shape=(MPI.COMM_WORLD.size*self.n,))
        idx_0 = MPI.COMM_WORLD.rank*self.n
        idx_1 = idx_0+self.n
        self.f['ds1'][idx_0:idx_1] = self.data
    def close(self):
        self.f.close()

class MyTest(object):
    __metaclass__ = pmi.Proxy
    pmiproxydefs = {'cls': 'test_pmi_mod.MyTestLocal', 'pmicall': [ 'do', 'show', 'close', 'fill' ]}
