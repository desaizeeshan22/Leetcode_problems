def transpose(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

print(transpose(matrix))