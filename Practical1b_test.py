# Write a program to perform the Matrix addition, Multiplication and Transpose Operation.
# 3066

def add(X, Y):
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    for r in result:
        print(r)
        
def mul(X, Y):
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):               # rows of X
        for j in range(len(Y[0])):       # cols of Y
            for k in range(len(Y)):      # rows of Y
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)
        
def transpose(matrix):
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(matrix)):               # rows 
        for j in range(len(matrix[0])):       # columns
            result[j][i] = matrix[i][j]
    for r in result:
        print(r)

X = [[1,7,3],
       [4 ,3,6],
       [7 ,8,5]]
Y = [[5,8,1],
       [6,7,3],
       [4,5,9]]

print("X = ",X)
print("Y = ",Y)

print("Addition")       
add(X, Y)
print("Multiplication")
mul(X, Y)
print("Transpose of X")
transpose(X)
print("Transpose of Y")
transpose(Y)
