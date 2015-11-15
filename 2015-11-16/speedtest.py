# -*- coding: utf-8 -*-

import numpy as np
import time
import pint as pt

'ndarray with mkl'
nparray = np.ones([1000, 1000])
timebefore = time.time()
nparray += 1.
timeend = time.time()
print(timeend - timebefore)

'mcmatrix'
nparray = np.ones([1000, 1000])
ptarray = pt.mcmatrix(nparray.tolist())
timebefore = time.time()
ptarray += 1.
timeend = time.time()
print(timeend - timebefore)
