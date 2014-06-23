import pmi
from mpi4py import MPI
import test_pmi_mod

mytest = test_pmi_mod.MyTest('myllfile.h5', 1024)

mytest.show()
mytest.fill()
mytest.close()
