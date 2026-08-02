import numpy as np

ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])

Teenagers=ages[ages<18]
print(Teenagers)

Adults=ages[ages>=18]
print(Adults)

adults=np.where(ages>=18,ages,0) #To maintain shape of array
print(adults)