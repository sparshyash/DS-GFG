# NumPy stands for Numerical Python and is used for handling large, multi-dimensional arrays and matrices. Unlike Python's built-in lists NumPy arrays provide efficient storage and faster processing for numerical and scientific computations. It offers functions for linear algebra and random number generation making it important for data science and machine learning.




import numpy as np

import numpy as np

a = [1, 2, 3, 4]
arr = np.array(a)

print("List: ", a)
print("Numpy Array:", arr)
print(type(a))
print(type(arr))


# 2D Array

import numpy as np

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10, 11, 12]
arr = np.array([l1, l2, l3])
print(arr)

#  1 Axis ,  2 Shape 

# Shape 

import numpy as np
arr = np.array([ [0, 4, 2],
                 [3, 4, 5],
                 [23, 4, 5],
                 [2, 34, 5],
                 [5, 6, 7] ])
print(arr.shape)


# Rank -- no of axis (dimensions)
print("Rank of array:", arr.ndim)

# 4 Data Type

import numpy as np

arr1 = np.array([[0, 4, 2]])
arr2 = np.array([0.2, 0.4, 2.4])

print("Data type of array 1:", arr1.dtype)
print("Data type of array 2:", arr2.dtype)


# Creation with Numpy

import numpy as np
arr = np.array([3, 4, 5, 5])
print(arr)



import numpy as np
text = "Geeksforgeeks"
arr = np.fromiter(text, dtype="U2")
print(arr)


import numpy as np
arr = np.arange(1, 20, 2, dtype=np.float32)
print(arr)


import numpy as np
arr = np.linspace(3.5, 10, 3, dtype=np.int32)
print(arr)

import numpy as np
arr = np.empty((4, 3), dtype=np.int32)
print(arr)   # gargbage values


import numpy as np
arr = np.ones((4, 3), dtype=np.int32)
print(arr) # with ones

import numpy as np
arr = np.zeros((4, 3), dtype=np.int32)
print(arr)  # with zeroes

