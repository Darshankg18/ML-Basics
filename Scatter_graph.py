import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,2,3,4,5,6,7,8,9,8])
y=np.array([44,34,56,65,76,67,80,77,90,91,91,85])
x1=np.array([0,1,1,4,3,3,5,6,7,7,8,9])
y1=np.array([37,42,55,53,62,69,71,78,84,89,95,99])
plt.scatter(x,y,color="red",alpha=0.6,s=100,label="Class A")
plt.scatter(x1,y1,color="green",alpha=0.6,s=100,label="Class B")
plt.title("Perfomance")
plt.legend()
plt.xlabel("Hours Studied")
plt.ylabel("Results")
plt.xticks(x)

plt.show()