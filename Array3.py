import numpy as np

a1=np.arange(12)
print("Original Array:",a1)

reshape=a1.reshape([4,3])
print("",reshape)

flatten=reshape.flatten()
print("",flatten)

ravel=reshape.ravel()
print("",ravel)

transpose=reshape.T
print("",transpose)