pmi-h5py
========

Copyright © 2014 Pierre de Buyl

pmi-h5py is a short example of using the Parallel Method Invocation to manage
parallel data writing with h5py. 

Example
-------

    mpirun -n 4 python test_pmi.py

Dependencies
------------

pmi-h5py requires
- mpi4py http://mpi4py.scipy.org/
- pmi https://github.com/olenz/pmi
- h5py http://www.h5py.org/ compiled with parallel support

This code is tested with:
- HDF5 1.8.13 and h5py's development version, using OpenMPI 1.8.1
- HDF5 1.8.12 and h5py 2.4.0a0, using OpenMPI 1.6.5

