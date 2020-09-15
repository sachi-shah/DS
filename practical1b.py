# Write a program to perform the Matrix addition, Multiplication and Transpose
# Operation.


import numpy as np

M1 = np.array([[3, 6, 9], [5, -10, 15], [-7, 14, 21]])
M2 = np.array([[2, -4, 3], [1, 2, 3], [4, -2, 3]])

print("matrix1 : \n", M1)
print("matrix2 : \n",M2)

M3 = M1 + M2  
print("M1 + M2 : \n",M3)

M4 = M1.dot(M2)  
print("M1 * M2 : \n",M4)

M5 = M1.transpose()
print("Transpose of M1 \n",M5)



