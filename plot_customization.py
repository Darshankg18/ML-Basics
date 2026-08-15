import matplotlib.pyplot as plt
import numpy as np
x=np.array([21,33,45,18,69])
y=np.array([12,25,34,76,89])
y1=np.array([7,10,6,1,2])
y2=np.array([34,21,73,40,67])
line=dict(marker=".",markersize=20,markerfacecolor='red',
         markeredgecolor="black",
         linestyle='dashed',
         linewidth=3
         )#linestyle='dashed','dotted','dashdot','None','solid'
plt.plot(x,y,**line) 
plt.plot(x,y1,color="purple",**line)
plt.plot(x,y2,color="blue",**line)
plt.show()