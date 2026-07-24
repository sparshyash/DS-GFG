import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
x = 10
print(a + x)


import numpy as np
arr = np.array([1, 2, 3])
res = arr + 1  
print(res)

import numpy as np

a = np.array([2, 4, 6])
b = np.array([[1, 3, 5], [7, 9, 11]])
res = a + b
print(res)

import numpy as np

a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)

import numpy as np
m = np.array([[1, 2], [3, 4]])
v = np.array([10, 20])
res = m * v
print(res)

import numpy as np

fd = np.array([ [0.8, 2.9, 3.9],
                [52.4, 23.6, 36.5],
                [55.2, 31.7, 23.9],
                [14.4, 11.0, 4.9] ])

cpg = np.array([9, 4, 4])
res = fd * cpg
print(res)

import numpy as np

temp = np.array([ [30, 32, 34, 33, 31],
                  [25, 27, 29, 28, 26],
                  [20, 22, 24, 23, 21] ])

corr = np.array([1.5, -0.5, 2.0])
res = temp + corr[:, None]
print(res)  #  corr[:, None] turns the 1D array into a column vector.  see ans to understand 


import numpy as np

data = np.array([ [10, 20],
                  [15, 25],
                  [20, 30] ])

m = data.mean(axis=0)
res = data - m
print(res)

print(res.size)