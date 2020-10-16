# Write a program to perform the Matrix addition, Multiplication and Transpose
# Operation.


X = [[1,7,3], [4 ,3,6], [2,8,5]]
Y = [[5,8,1], [6,7,3], [4,5,9]]


def add():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    for r in result:
        print(r)
        
def mul():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):       #rows of X
        for j in range(len(Y[0])):      #cols of Y
            for k in range(len(Y)):      #rows of Y
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)
        
def transpose():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    #transpose of X
    
    for i in range(len(X)):             #rows 
        for j in range(len(X[0])):       # columns
            result[j][i] = X[i][j]
    for r in result:
        print(r)
        
print("X = ",X)
print("Y = ",Y)

print("Addition")       
add()
print("Multiplication")
mul()
print("Transpose of X")
transpose()



