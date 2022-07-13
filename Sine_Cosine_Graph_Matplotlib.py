#Sine and Cosine Graph
import numpy as np
import matplotlib.pyplot as plt

#creating list of values 
t = np.linspace(-360,360)
x = [i*(np.pi/180) for i in t]
Sin = np.sin(x)
Cos = np.cos(x)

#plot
plt.figure(figsize=(10,5))
plt.plot(t,Sin, color="r", label="Sin(x)")
plt.plot(t,Cos, label="Cos(x)")
plt.xlim(min(t),max(t)) #removing empty break at the begining and end
plt.title("Sin and Cos functions", fontsize=16)
plt.xlabel("X", fontsize=14)
plt.ylabel("Sin and cos value", fontsize=14)
plt.legend(loc="best")
plt.grid()
plt.show()