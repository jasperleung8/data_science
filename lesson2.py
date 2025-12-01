import numpy as np

nums = [[1,5,2,7,8,9],[7,3,0,5,4,8]]

arr = np.array(nums)

print(arr.shape)

print(arr.size)

print(arr.ndim)

print(arr.dtype)

nums2 = [7,9,5,3,6,1]

arr2 = np.array(nums2)

print(np.sum(arr2))

print(round(np.mean(arr2),2))

print(np.min(arr2))

print(np.max(arr2))

print(round(np.var(arr2),2))

print(round(np.std(arr2),2))

reshaped = arr2.reshape((2,3))

flaten = reshaped.flatten()

print(flaten)

print(reshaped)