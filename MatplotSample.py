# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:57:39 2018

@author: ethan.kong
"""

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4,5])
plt.ylabel('Some Significant Number')
plt.show()

t = np.arange(0.,5.,0.2)
plt.plot(t,t, 'r--',t,t**2, 'bs', t,t**3, 'g^')
plt.axis([0,6,0,150])