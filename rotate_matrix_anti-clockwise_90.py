

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
def rotate_anticlockwise(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()
    transpose(matrix)
    return matrix


matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

print(rotate_anticlockwise(matrix))