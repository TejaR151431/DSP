#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:17:02 2019

@author: rgukt
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,0.01,100)
f=input("f:")
fs=input("fs:")
y=np.sin(2*np.pi*f*x)
plt.plot(x,y)
plt.show()
z=np.sin(2*np.pi*fs*x)
plt.plot(x,z)
plt.show()
c=y+z
plt.plot(x,c)
plt.show()