import pmi
from mpi4py import MPI
import test_pmi_mod

hop = test_pmi_mod.MyTest('hey hey', 5)
hop.do()

hop.show()
hop.fill()
hop.close()
