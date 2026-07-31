import numpy as np

## Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger array's shape
## The dimensions should have the same size or one of the dimensions has a size of 1
array1=np.array([[1,2,3,4,5]])
array2=np.array([[1],[2],[3],[4],[5]])
print("array1 Shape:",array1.shape)
print("array2 Shape:",array2.shape)
print("Multiplication:",array1*array2)