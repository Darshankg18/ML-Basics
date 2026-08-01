import numpy as np

array=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array)) #Sum of the array.
print(np.mean(array)) #Mean(Average) of the array.
print(np.std(array)) #Standard deviation of the array.
print(np.var(array)) #Variance of the array.
print(np.max(array)) # Maximum value in the array.
print(np.min(array)) # Minimum value in the array.
print(np.argmin(array)) # Index of the smallest element in the flattened array.
print(np.argmax(array)) # Index of the largest element in the flattened array.
print(np.sum(array,axis=0)) # Column wise sum.
print(np.sum(array,axis=1)) # Row wise sum.