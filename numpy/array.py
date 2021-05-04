import numpy as np

a = np.array([2, 4, 6])
print(a)

b = np.array([[1, 3, 5], [2, 4, 6]])
c = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
print(c)

print(b[0, :]) # index first row and all columns
print(b[1, 2]) # index the second row, third column
print(b[:, 1]) # index the entire second column
