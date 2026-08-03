import numpy as np

rng=np.random.default_rng()
print(rng.integers(low=1,high=101,size=3))

rng_1=np.random.default_rng()
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)