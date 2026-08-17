import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=np.array([10,15,25,30,40])
plt.grid(axis='y',linewidth=2,color='black',linestyle='dashed')
# plt.grid()
plt.plot(x,y,color="red")
plt.show()