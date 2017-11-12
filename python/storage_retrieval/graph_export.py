#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 200, 0.1)
y = np.sin(x)
#plt.figure(figsize=(1,1))
plt.plot(x,y)
#plt.savefig('graph.png', dpi=10)
plt.show()
