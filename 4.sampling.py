#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:20:59 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt
f=input("f:")
fs=input("fs:")
f=f*1.0
fs=fs*1.0
print f/fs
t=np.linspace(0,0.01,100)
n=np.linspace(0,12,12)
y=np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show();
k=np.sin(2*np.pi*(f/fs)*n)
plt.stem(n,k)
plt.show();