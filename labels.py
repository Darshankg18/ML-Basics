import matplotlib.pyplot as plt
import numpy as np
x=np.array([21,22,23,24,25])
y=np.array([12,25,34,76,89])
y1=np.array([17,77,36,19,57])
y2=np.array([34,21,73,40,67])
plt.title("Class Size",fontsize=20,fontweight='bold',color='red')
plt.xlabel("Year",fontsize=20,
           fontweight="bold",color="brown")
plt.ylabel("Results",fontsize=20,
           fontweight="bold",color="brown")
plt.tick_params(axis="both",colors='#eb6405') #Axis parameter colour
plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xticks(x)
plt.show()