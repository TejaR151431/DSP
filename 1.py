import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2,200)
x=np.sin(2*np.pi*t)
n=np.linspace(0,20,20)
s=np.sin(2*np.pi*(0.1)*n)
y=[]
y.append(s[0])
for i in range(1,20,1):
	y.append(y[i-1]+s[i])
plt.subplot(221)
plt.plot(t,x)
plt.subplot(222)
plt.stem(n,s)
plt.subplot(223)
plt.stem(n,y)
plt.show()
