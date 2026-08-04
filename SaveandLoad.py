import numpy as np

## Saving data to file
array=np.array([[1,2,3],[4,5,6]])
np.save('data',array)
print("Numpy array is saved")

## Loading data from saved file
a=np.load('data.npy')
print("Numpy array is loaded to a")
print(a)

## Saving Multiple Numpy array
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([10,20,30,40])
np.savez('data1',a1,a2)
print("Numpy array were Saved!")

## Loading Multiple Numpy array from saved file
arrays=np.load("data1.npz")
print(arrays)

array1=arrays['arr_0']
array2=arrays['arr_1']
print(array1)
print(array2)