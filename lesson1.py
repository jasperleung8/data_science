import numpy as np

nums = [1,2,3,4,5,6]

arr = np.array(nums)

print(arr)

nums2 = [[1,2,3],[4,5,6],[7,8,9]]

arr2 = np.array(nums2)

print(arr2)

arr3 = np.arange(1,101)

print(arr3)

arr4 = np.zeros((5,5))

print(arr4)

arr5 = np.ones((5,5))

print(arr5)

arr6 = np.full((7,3),100)

print(arr6)

arr7 = np.eye(7,3)

print(arr7)

print(arr6+arr7)