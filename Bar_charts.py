import matplotlib.pyplot as plt
import numpy as np
categories=np.array(["Grains","Fruits","Vegetables","Leaves","Dairy","Sweets"])
ate=([4,3,5,2,1,6])
plt.bar(categories,ate,color="#cc04c9")
# plt.barh(categories,ate,color="#cc04c9") #for creating horizontal bar charts
plt.title("Food Consumption")
plt.xlabel("Food")
plt.ylabel("Consumption Quantity")
plt.show()