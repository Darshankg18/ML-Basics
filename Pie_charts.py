import matplotlib.pyplot as plt
import numpy as np
categories=["Freshers",'Sophomores',"Junior","Seniors"]
values=np.array([35,10,30,25])
colors=["red","green","yellow","blue"]
plt.pie(values,labels=categories,autopct="%1.2f%%",colors=colors,
        explode=[0.1,0,0,0],shadow=True,startangle=90)
plt.title("Avengers Collage")
plt.show()