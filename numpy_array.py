import numpy as np

list = [1,2,3,4,5]

array = np.array(list)

array2 = np.array([[1,2,3,4,5],[6,7,8,9,0]])

print(array2.dtype)
print(array2.shape)
print(array2.ndim)

one = np.ones(5)
zeros = np.zeros(5)

print(one)
print(zeros)

array3 = np.arange(10,22)

print(array3)
print(array3.shape)

# array4 = np.array(list,dtype="str")

# print(array4)

array5 = array3.reshape(6,2)

print(array5)

array6 = np.array([5,2,8,2,9,1,7])

array7 = np.sort(array6)

print(array7)

print(array7[0])

print(array5[2,1])

array8 = array6*10

print(array8)