# Copyright 2014 Pierre de Buyl
#
# This file is part of pmi-h5py
#
# pmi-h5py is free software and is licensed under the modified BSD license (see
# LICENSE file).

import test_pmi_mod

mytest = test_pmi_mod.MyTest('myllfile.h5', 1024)

mytest.fill()
mytest.close()
