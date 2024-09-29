import numpy
numRow = 3
numCol = 3
# numRow = int(input("Enter number of row: "))
# numCol = int(input("Enter number of column: "))
matrix = [[5, 2, 6], [3, 4, 7], [2, 5, 4]]
temp = []

# # input
# for i in range(numRow):          # A for loop for row entries
#     a =[]
#     for j in range(numCol):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)

# # For printing the matrix

def printMatrix():
    for i in range(numRow):
        for j in range(numCol):
            print(matrix[i][j], end = " ")
        print()

# check if first col of 1st row is 1
if matrix[0][0] == 1:
    print("yes")
else:
    print("no")
    # divide all in row by pivot
    for i in range(0, len(matrix[0])):
        temp.append(matrix[0][i]/matrix[0][0])
    matrix[0] = temp
    printMatrix()

# eliminate all below the pivot to zero
temp =[]
for i in range(0, len(matrix[1])):
    temp.append(matrix[1][i] - (matrix[1][0]/matrix[0][0])*matrix[0][i])
matrix[1] = temp
printMatrix()

temp =[]
for i in range(0, len(matrix[2])):
    temp.append(matrix[2][i] - (matrix[2][0]/matrix[0][0])*matrix[0][i])
matrix[2] = temp
printMatrix()

# 2nd pivot
# check if first col of 2st row is 1
if matrix[1][1] == 1:
    print("yes")
else:
    print("no")
    # divide all in row by pivot
    for i in range(0, len(matrix[1])):
        temp.append(matrix[1][i]/matrix[1][1])
    matrix[1] = temp
    printMatrix()


# eliminate all below the pivot to zero
temp =[]
for i in range(0, len(matrix[2])):
    temp.append(matrix[2][i] - (matrix[2][1]/matrix[1][1])*matrix[2][i])
matrix[2] = temp
printMatrix()